import pandas as pd
import numpy as np
from PyQt5.QtWidgets import QApplication
import ccxt
import datetime
import statsmodels.tsa.api as tsa
import time
import yaml
import base64
import os
import hashlib
from apps.database import Database
from datastream import DataStream
from source.statarb_algo import StatArbAlgorithm
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet



class Datazaur(QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.ui = None
        self.user = None
        self.exchanges = dict()
        self.current_exchange = None
        self.current_ticker = None

        self.db = Database()
        self.holdings = {'cash': 0}
        self.algorithm_running = False
        self.algorithms = dict()

        self.config_dir = os.path.join(os.path.dirname(os.getcwd()), '../settings')

        self.datastream = DataStream()

        self.config = None
        self.static = None
        self.load_config()

        self.history = pd.DataFrame(columns=self.config['TABLES']['ohlc'].keys())



    # loads settings from file
    def load_config(self):
        with open(os.path.join(os.getcwd(), 'settings', 'config.yaml'), 'r') as config:
            self.config = yaml.safe_load(config)


    # creates necessary directories
    def setup_dirs(self):
        pass


    # connects to exchange
    def connect_exchange(self, exchange_id):
        if exchange_id in self.exchanges.keys():
            return self.exchanges[exchange_id]
        else:
            self.current_exchange = self.exchanges[exchange_id] = getattr(ccxt, exchange_id)({'enableRateLimit': True,
                                                                                'options': {'defaultType': 'future'}})
            try:
                self.current_exchange.load_markets()
            except Exception as e:
                print(f'connection failed - error {e}')
            return self.current_exchange

    # selects exchange
    def select_exchange(self, exchange_id):
        self.current_exchange = self.exchanges[exchange_id]

    # selects ticker
    def select_ticker(self, ticker):
        self.current_ticker = ticker

    # deletes exchange
    def delete_exchange(self, exchange_id):
        del self.exchanges[exchange_id]



    # checks if table is in database, else returns False
    def find_table(self, table_name):
        query = self.db.get_tables_list()
        if not query or not query[0]:
            print('no tables in db')
            return False
        else:
            flatted_list = []
            for row in query:
                flatted_list.append(row[0])
            if table_name in flatted_list:
                print(f'table {table_name} found')
                return True
            else:
                print('no such table')
                return False

    # gets data - first checks in database then adds most recent data points
    def get_data(self, exchange, ticker, interval, since):
        table_name = ticker + '_' + exchange + '_' + interval
        if self.find_table(table_name):
            oldest_timestamp = self.db.cursor.execute(f"""SELECT MIN("Date") FROM "{table_name}";""").fetchall()[0][0]
            if (since + 3600000) >= oldest_timestamp:
                df = pd.DataFrame(self.db.cursor.execute(f"""SELECT * FROM "{table_name}" WHERE Date >= "{since}";""").fetchall())
                since2 = self.db.cursor.execute(f"""SELECT MAX("Date") FROM "{table_name}";""").fetchall()[0][0]
                df2 = pd.DataFrame(self.get_data_since(exchange, ticker, interval, since2))
                df = df.append(df2)
            else:
                print('downloading1')
                df = self.get_data_since(exchange, ticker, interval, since)
        else:
            print('downloading2')
            df = self.get_data_since(exchange, ticker, interval, since)

        df.columns = self.config['OHLC_COLUMNS']
        df.drop_duplicates(subset='Date', inplace=True)
        df.to_sql(table_name, self.db.connection, if_exists='replace', index=False, dtype={'Date': 'INTEGER',
                                                                                           'Open': 'REAL',
                                                                                           'High': 'REAL',
                                                                                           'Low': 'REAL',
                                                                                           'Close': 'REAL',
                                                                                           'Volume': 'REAL'})
        self.db.connection.commit()
        df.set_index('Date', inplace=True)
        df.name = ticker + '_' + exchange + '_' + interval
        return df

    # gets data from a given start date
    def get_data_since(self, exchange_id, ticker, interval, since):
        exchange = self.exchanges[exchange_id]
        data = []
        count = 0
        while True:
            d2 = exchange.fetch_ohlcv(ticker, interval, since)
            data += d2
            count += 1
            if len(d2) <= 1:
                break
            else:
                since = d2[-1][0]
        df = pd.DataFrame(data)
        df.drop_duplicates(subset=0, inplace=True)
        df.name = ticker + '_' + exchange.id + '_' + interval
        #df.set_index(0, inplace=True)
        return df

    # gets data for multiple assets
    def get_data2(self, exchange, symbols, interval, since):
        df0 = pd.DataFrame()
        for symbol in symbols:
            try:
                df = self.get_data(exchange, symbol, interval, since)
                df0[symbol] = df['Close']
            except Exception as e:
                print(f'Error {e}')
                continue

        df0.dropna(inplace=True)
        return df0

    # returns weighted average and standard deviation
    @staticmethod
    def weighted_avg_and_std(values, weights):
        average = np.average(values, weights=weights)
        variance = np.average((values - average) ** 2, weights=weights)
        return average, np.sqrt(variance)

    # returns total price of 1 unit of spread
    @staticmethod
    def get_spread_price(prices, params):
        price = 0
        for i, v in params.items():
            price += abs(v) * prices[i]
        return price

    # returns total value of 1 unit of spread
    @staticmethod
    def get_spread_val(prices, params):
        price = 0
        for i, v in params.items():
            price += v * prices[i]
        return price

    # adjusts trade size
    def adjust_trade_size(self, cash, prices, params):
        spread_price = self.get_spread_price(prices, params)
        return cash/spread_price

    # opens a long position on spread
    def buy_spread(self, exchange, algorithm, prices, timestamp):
        ratio = self.adjust_trade_size(self.holdings['cash'], prices, algorithm.params)
        for i, v in algorithm.params.items():
            if v > 0:
                self.exchanges[exchange].create_limit_buy_order(i, abs(v*ratio), prices[i])
                self.holdings[i] = v * ratio

            elif v < 0:
                self.exchanges[exchange].create_limit_sell_order(i, abs(v*ratio), prices[i])
                self.holdings[i] = -v * ratio
            self.history.loc[len(self.history)] = [timestamp, i, v*ratio, prices[i],
                                                       (abs(v*ratio)*prices[i]).__round__(2), '', '', '']


    # opens a short position on spread
    def sell_spread(self, exchange, algorithm, prices, timestamp):
        ratio = self.adjust_trade_size(self.holdings['cash'], prices, algorithm.params)
        for i, v in algorithm.params.items():
            if v > 0:
                order = self.exchanges[exchange].create_limit_sell_order(i, abs(v*ratio), prices[i])
                self.holdings[i] = -v * ratio
            elif v < 0:
                order = self.exchanges[exchange].create_limit_buy_order(i, abs(v*ratio), prices[i])
                self.holdings[i] = v * ratio

            self.history.loc[len(self.history)] = [timestamp, i, v*ratio, prices[i],
                                                       (abs(v*ratio)*prices[i]).__round__(2), '', '', '']

    #closes all open trades
    def exit_trades(self, timestamp, exchange, algorithm, prices):
        for k, v in self.holdings.items():
            if v > 0 and k != 'cash':
                self.exchanges[exchange].create_limit_sell_order(k, v, prices[k])
                self.holdings['cash'] += v * prices[k]
                self.holdings[k] = 0
            elif v < 0 and k != 'cash':
                self.exchanges[exchange].create_limit_buy_order(k, v, prices[k])
                self.holdings['cash'] += v * prices[k]
                self.holdings[k] = 0

            self.history.loc[len(self.history)] = [timestamp, k, v, prices[k],
                                               (abs(v) * prices[k]).__round__(2), '', '', '']

    # returns spread values
    @staticmethod
    def get_spread(df, params):
        spread = np.array(np.zeros(len(df)))
        for col in df.columns:
            spread += df[col]*params[col]
        print(spread)
        return spread

    # calculate spread value, mean, standard deviation and z-score for a given dataframe
    def prepare_df(self, df, params, interval, refresh_rate):
        df['spread'] = self.get_spread(df, params)
        df['spread_mean'] = df['spread'].mean()
        df['spread_std'] = df['spread'].std()
        df['z_score'] = ((df['spread'] - df['spread_mean']) / df['spread_std']).astype('float64')
        interval_secs = self.get_time_in_ms(interval)/1000
        weight = interval_secs / refresh_rate
        df['weight'] = weight
        return df

    # start trading using selected algorithm
    def trade_live(self, window, algorithm, cash, interval='30m', timeframe='3M', refresh_rate=10):
        since = self.get_since(timeframe)
        df = self.get_data2(self.current_exchange.id, list(algorithm.params.index), interval, since)
        df = self.prepare_df(df, algorithm.params, interval, refresh_rate)
        self.holdings['cash'] = cash
        trade_open = False
        self.algorithm_running = True

        while self.algorithm_running:
            data = pd.DataFrame(self.current_exchange.fetch_tickers(algorithm.params.index)).loc[['timestamp', 'last'], :]
            timestamp = data.loc['timestamp', algorithm.params.index[0]]
            df.loc[timestamp] = data.loc['last']
            df.loc[timestamp, 'spread'] = self.get_spread_val(data.loc['last'], algorithm.params)
            df.loc[timestamp, 'weight'] = 1
            avg, std = self.weighted_avg_and_std(df['spread'], df['weight'])
            df.loc[timestamp, 'spread_mean'] = avg
            df.loc[timestamp, 'spread_std'] = std
            df.loc[timestamp, 'z_score'] = (df.loc[timestamp, 'spread'] - df.loc[timestamp, 'spread_mean']) / df.loc[timestamp, 'spread_std']

            if df.loc[timestamp, 'z_score'] > algorithm.entry_z and not trade_open:
                self.sell_spread(self.current_exchange.id, algorithm, df.loc[timestamp], timestamp)
                trade_open = True
                positions = self.get_positions(self.current_exchange.id)
                window.tableView_2.setModel(PandasModel(positions))

            elif df.loc[timestamp, 'z_score'] < -algorithm.entry_z and not trade_open:
                self.buy_spread(self.current_exchange.id, algorithm, df.loc[timestamp], timestamp)
                trade_open = True
                positions = self.get_positions(self.current_exchange.id)
                window.tableView_2.setModel(PandasModel(positions))

            df['exit calc'] = df['z_score'] * df['z_score'].shift(1)
            if df.loc[timestamp, 'exit calc'] < 0 and trade_open:
                self.exit_trades(timestamp, self.current_exchange.id, algorithm, df.loc[timestamp])
                trade_open = False
                positions = self.get_positions(self.current_exchange.id)
                window.tableView_2.setModel(PandasModel(positions))

            time.sleep(refresh_rate)

        self.exit_trades(df.index[-1], self.current_exchange.id, algorithm, df.loc[timestamp])
        date = str(datetime.datetime.today())[:16]
        self.history.to_csv(f'trade_history_{date}.csv')

    # adds natural logarithms
    @staticmethod
    def add_logs(df):
        cols = df.columns
        df[f'log_{cols[0]}'] = np.log(df[cols[0]])
        df[f'log_{cols[1]}'] = np.log(df[cols[1]])
        df[f'log_return{cols[0]}'] = df[f'log_{cols[0]}'] - df[f'log_{cols[0]}'].shift()
        df[f'log_return{cols[1]}'] = df[f'log_{cols[1]}'] - df[f'log_{cols[1]}'].shift()
        return df

    # returns percentage returns with base 100
    @staticmethod
    def get_base_100_returns(df):
        df0 = pd.DataFrame()
        for col in df.columns:
            df0[col] = 100 * df[col] / (df[col].iloc[0])
        return df0

    # adds z-score to dataframe
    @staticmethod
    def get_z_score(df, window=''):
        if window == '':
            df['spread_ma'] = df['spread'].mean()
            df['ma_stdev'] = df['spread'].std()
        else:
            df['spread_ma'] = df['spread'].rolling(window=window).mean()
            df['ma_stdev'] = df['spread'].rolling(window=window).std()
        df['z_score'] = ((df['spread'] - df['spread_ma']) / df['ma_stdev']).astype('float64')
        return df




    # loads last settings from database for current user
    def load_config2(self):
        user_id = self.db.execute_read_query(f"""SELECT id FROM users WHERE username="{self.user}";""")
        if not user_id:
            return
        else:
            last_config_id = self.db.execute_read_query(f"""SELECT MAX("config_id")
                                                            FROM users_config
                                                            WHERE user_id="{user_id}";""")[0]
            if not last_config_id:
                self.tests_config = self.config['TESTS_CONFIG']
            else:
                config = self.db.execute_query(f"""SELECT * FROM settings WHERE id="{last_config_id}";""")[0][1:]
                for k, v in zip(self.config['TESTS_CONFIG.keys()'], config):
                    self.tests_config[k] = v


    # saves settings for cointegration stat_tests
    def save_config(self, settings):
        self.tests_config.update(settings)
        self.db.save_config(self.user, )


    # ADF test wrapper
    @staticmethod
    def adf_test(data, reg='c', lag='AIC', maxlag=None):
        if maxlag:
            return tsa.adfuller(data.dropna(), regression=reg, maxlag=maxlag)[1].__round__(3)
        else:
            return tsa.adfuller(data.dropna(), regression=reg, autolag=lag)[1].__round__(3)

    # KPSS test wrapper
    @staticmethod
    def kpss_test(data, reg='c', lag='auto', maxlag=None):
        if maxlag:
            return tsa.kpss(data.dropna(), regression=reg, nlags=maxlag)[1].__round__(3)
        else:
            return tsa.kpss(data.dropna(), regression=reg, nlags=lag)[1].__round__(3)

    # ADF + KPSS stat_tests
    def test_stationarity(self, df, adf=True, kpss=True):
        results = pd.DataFrame(index=['ADF-test', 'KPSS-test'], columns=['H0'], data={'H0': ['Unit root is present',
                                      'Time series is stationary']})
        for col in df.columns:
            if adf:
                results.loc['ADF-test', col] = self.adf_test(df[col], reg=self.adf_kpss_config['adf_reg'],
                                                             lag=self.adf_kpss_config['adf_autolag'],
                                                             maxlag=self.adf_kpss_config['adf_max'])
            if kpss:
                results.loc['KPSS-test', col] = self.kpss_test(df[col], reg=self.adf_kpss_config['kpss_reg'],
                                                               lag=self.adf_kpss_config['kpss_autolag'],
                                                               maxlag=self.adf_kpss_config['kpss_max'])
        return results

    # OLS model wrapper
    @staticmethod
    def OLS_model(df, const):
        df.dropna(inplace=True)
        y = df.iloc[:, 0]
        if const:
            x = tsa.stattools.add_constant(df.iloc[:, 1:])
        else:
            x = df.iloc[:, 1:]
        model = tsa.stattools.OLS(y, x, missing='drop', hasconst=const)
        results = model.fit()
        summary = results.summary()
        return results, summary

    # returns correlations matrix
    @staticmethod
    def get_corr_matrix(df):
        matrix = pd.DataFrame(columns=df.columns, index=df.columns)
        matrix.index.name = 'corr matrix'
        for col in df.columns:
            for col2 in df.columns:
                matrix.loc[col, col2] = df[col].corr(df[col2]).__round__(3)
        return matrix

    # Engle-Granger test for cointegration
    def engle_granger_coint(self, df, const, adf_reg='c', adf_autolag='AIC', adf_maxlag=None):
        results, summary = self.OLS_model(df, const)
        adf_resid = tsa.stattools.coint(df.iloc[:, 0], df.iloc[:, 1:], trend=adf_reg, autolag=adf_autolag,
                                                                              return_results=False)[1].__round__(3)
        kpss_resid = self.kpss_test(results.resid)
        params = pd.Series({df.columns[0]: 1}).append(-results.params)
        return pd.Series({'ADF resid': adf_resid, 'KPSS resid': kpss_resid}, name='coint stat_tests'), summary, params, results.resid

    # saves algorithm
    def save_algorithm(self, algorithm):
        self.algorithms[algorithm.name] = algorithm
        self.ui.trade_panel.save_algo(algorithm.name)
        self.db.save_algorithm(algorithm)

    # deletes algorithm
    def delete_algorithms(self, algorithm_name):
        self.algorithms.__delitem__(algorithm_name)
        self.ui.trade_panel.reload_algorithms()
        self.db.delete_algorithm(algorithm_name)

    # derives encryption key from password
    @staticmethod
    def derive_key(password, salt):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
        key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
        return key

    # encrypts symmetrically
    def symmetric_encrypt(self, data, password, salt):
        key = self.derive_key(password, salt)
        fernet = Fernet(key)
        return fernet.encrypt(data.encode())

    # decrypts symmetrically
    def symmetric_decrypt(self, data, password, salt):
        key = self.derive_key(password, salt)
        fernet = Fernet(key)
        return fernet.decrypt(data).decode()

    # adds API keys to database (encrypted)
    def add_keys(self, pubkey, privkey, password):
        salt = os.urandom(32)
        self.current_exchange.apiKey = pubkey
        self.current_exchange.secret = privkey
        pub2 = self.symmetric_encrypt(pubkey, password, salt)
        priv2 = self.symmetric_encrypt(privkey, password, salt)
        self.db.add_keys(self.user, self.current_exchange.id, pub2, priv2, salt)

    # returns SHA3_512 hash after 100000 iterations with salt
    @staticmethod
    def hash_password(text, salt):
        for i in range(100000):
            text = hashlib.sha3_512((text + salt).encode()).hexdigest()
        return text

    # adds username, hash and salt to database
    def add_hash(self, username, password):
        salt = os.urandom(32).hex()
        hsh = self.hash_password(password, salt)
        self.db.add_hash(username, hsh, salt)

    # gets user's hash and salt from database, then hashes entered password using user's hash and compares hashes
    def compare_hashes(self, username, password):
        query = self.db.get_hash(username)
        if not query:
            return False
        else:
            salt = query[0][1]
            hashed_password = self.hash_password(password, salt)
            return hashed_password == query[0][0]

    # logs in and loads API keys and algorithms
    def login(self, username, password):
        self.user = username
        self.load_algorithms(username)
        self.load_keys(username, password)

    # loads user's API keys from database
    def load_keys(self, username, password):
        keys = self.db.get_api_keys(username)
        if not keys:
            print('no keys in db')
            return False
        else:
            for item in keys:
                self.connect_exchange(keys[0][0])
                pubkey = self.symmetric_decrypt(item[1], password, item[-1])
                privkey = self.symmetric_decrypt(item[2], password, item[-1])
                self.exchanges[item[0]].apiKey = pubkey
                self.exchanges[item[0]].secret = privkey

    # loads current user's algorithms
    def load_algorithms(self, username):
        algorithm_list = self.db.execute_read_query(f"""SELECT * FROM algorithms WHERE username="{username}"; """)
        #print(algorithm_list)
        if not algorithm_list:
            print('no algos')
            return False
        else:
            for row in algorithm_list:
                params = pd.Series(index=row[1][1:-1].replace("'", "").split(), data=row[2][1:-1].split())
                algorithm = StatArbAlgorithm(row[0], params, row[3], row[4])
                self.algorithms[row[0]] = algorithm

    # gets account balance from exchange
    def fetch_balance(self, exchange_id):
        df = pd.DataFrame(self.exchanges[exchange_id].fetch_balance()).transpose()
        df = df[['free', 'used', 'total']]
        df = df[df['total'] != 0]
        df.dropna(inplace=True)
        return df

    # gets open positions from exchange
    def get_positions(self, exchange_id):
        df = pd.DataFrame(self.exchanges[exchange_id].fetchPositions())
        df = df[df['initialMargin'] != '0']
        return df





