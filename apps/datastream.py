import quandl
import investpy
import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import zipfile
from urllib import request
import glob


class DataStream:
    def __init__(self):

        self.database = None
        self.datasets = dict()

        self.instrument_types = {'crypto': ['ccxt', 'coinmarketcap', 'investing', 'yahoo'],
                                 'stocks': ['investing', 'yahoo', 'iex', 'eod', 'quandl', 'nasdaq'],
                                 'bonds': ['investing'],
                                 'currencies': ['investpy', 'forex-python'],
                                 'indexes': ['investing', 'quandl'],
                                 'etfs': ['investing'],
                                 'funds': ['investing'],
                                 'fundamentals': ['yahoo', 'investing'],
                                 'certificates': ['investing'],
                                 'macro': ['investing', 'yahoo', 'wb', 'quandl']
                                 }


    # GENERAL METHODS
    def load_api_keys(self, keys):
        pass






    # INVESTING
    def get_calendar(self):
        return investpy.news.economic_calendar()

    def get_etf_list(self, country=None):
        return investpy.get_etfs() if not country else investpy.get_etfs(country)

    def get_etf_values(self, country):
        return investpy.get_etfs_overview(country)

    def get_countries(self, category):
        if category == 'i':
            return investpy.get_index_countries()
        elif category == 'b':
            return investpy.get_bond_countries()
        elif category == 's':
            return investpy.get_stock_countries()
        elif category == 'e':
            return investpy.get_etf_countries()
        else:
            return

    def get_index_data(self, country):
        return investpy.get_indices(country)

    def get_index_values(self, country):
        return investpy.get_indices_overview(country)

    def get_bonds_data(self, country):
        return investpy.get_bonds(country)

    def get_bond_yields(self, country):
        return investpy.get_bonds_overview(country)

    def get_stock_data(self, country):
        return investpy.get_stocks(country)

    def get_stock_prices(self, country):
        return investpy.get_stocks_overview(country)




    # YAHOOO

    # symbols from 2017
    def get_yahoo_symbols(self):
        url = 'https://investexcel.net/wp-content/uploads/2015/01/Yahoo-Ticker-Symbols-September-2017.zip'
        filepath = os.path.join(YAHOO_METADATA_DIR, 'yahoo_all_symbols.zip')
        request.urlretrieve(url, filepath)
        with zipfile.ZipFile(filepath, 'r') as file:
            file.extractall(YAHOO_METADATA_DIR)
        os.remove(filepath)

    def parse_yahoo_symbols(self):
        all_symbols = pd.read_excel(YAHOO_ALL_SYMBOLS_FILE, sheet_name=None, header=3, usecols=[0, 1, 2, 3])
        for category, df in all_symbols.items():
            if category == 'About':
                continue
            df.to_csv(METADATA_DIRS[category.lower()])



    # QUANDL



    # COINMARKETCAP

    def get_coinmarketcap_metadata(self):
        pass

    def get_coinmarket_data(self):
        session = Session()
        session.headers.update(COINMARKETCAP_HEADERS)
        try:
            response = session.get(COINMARKETCAP_LINKS['listings'], params=COINMARKETCAP_PARAMETERS)
            data = pd.DataFrame(json.loads(response.text)['data'])
            print(data)
            data.set_index('cmc_rank', inplace=True)
            info = data.iloc[:, 12]
            market_data = pd.DataFrame(list(map(lambda x: x[COINMARKETCAP_PARAMETERS['convert']], data['quote'])))

            print(info)
            print(market_data)

            return info, market_data

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


    def get_coinmarket_categories(self):
        link = COINMARKETCAP_LINKS['categories']
        cls = COINMARKETCAP_CLASSES['class']
        req = requests.get(link)
        soup = BeautifulSoup(req.text, HTML_PARSER)
        categories = soup.select(f'.{cls}')
        return categories

    def filter_coins_by_category(self, category):
        link = COINMARKETCAP_LINKS['view'] + category.lower().replace(' ', '-')
        cls = COINMARKETCAP_CLASSES['elements']
        req = requests.get(link)
        soup = BeautifulSoup(req.text, HTML_PARSER)
        filtered_coins = soup.select(f'.{cls}')
        return filtered_coins


    # EOD

    @staticmethod
    def extract_ticker(text):
        return text.split('/')[-1].split('.')[0]


    def get_eod_tickers(self):
        for exchange in EOD_EXCHANGES:
            link = EOD_SYMBOLS_LINK.replace('<TICKER>', exchange)
            req = requests.get(link)
            soup = BeautifulSoup(req.text, 'html.parser')
            links = soup.find_all('loc')
            tickers = [self.extract_ticker(link.text) for link in links]
            self.tickers['eod'][exchange] = tickers
            df = pd.DataFrame(data={exchange: tickers})
            path = f'{STOCK_METADATA}_EOD_tickers_{exchange}.csv'
            df.to_csv(path)



    # CCXT
    def ccxt_exchanges(self):
        pass

    # WORLD BANK


    # PANDAS DATAREADER


    # FED










    def scrap_headlines(self, website, cls=None, tag=None):
        req = requests.get(website)
        soup = BeautifulSoup(req.text, HTML_PARSER)



    def check_connections(self):
        return True


    def get_security_symbol(self, name):
        symbol = 1
        return symbol


    def get_data(self, db_code, dataset_code, params=None):
        query = db_code + '/' + dataset_code
        return quandl.get(query, authtoken=quandl.ApiConfig.api_key)

    def load_database(self):
        if self.filepaths['config_file_name'] in os.listdir(self.filepaths['config_dir']):
            print('db from file')
            self.database = pd.read_csv(self.filepaths['config_filepath'], index_col=0)
        else:
            print('db from net')
            self.database = self.save_database()


    def load_metadata(self):
        pass


    def fetch_dataset(self, index):
        database_code = self.get_database_code(index=index)
        zip_file_name = self.database.loc[index, 'name'] + '.csv.zip'
        file_url = f'https://www.quandl.com/api/v3/databases/{database_code}/metadata?api_key={quandl.ApiConfig.api_key}'
        zip_file_path = os.path.join(self.filepaths['datasets_dir'], zip_file_name)
        request.urlretrieve(file_url, zip_file_path)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(self.filepaths['datasets_dir'])
        os.remove(zip_file_path)
        latest_file = max(glob.glob(os.path.join(self.filepaths['datasets_dir'], '*')), key=os.path.getctime)
        self.datasets[database_code] = latest_file
        metadata = pd.read_csv(latest_file, index_col=None)
        return metadata

    def get_dataset_code(self, db_code, name=None, index=None):
        metadata = pd.read_csv(self.datasets[db_code], index_col=None)
        if name is not None:
            return metadata[metadata['name']==name]['code']
        elif index is not None:
            return metadata.loc[index, 'code']

    def get_database_code(self, db_name=None, index=None):
        if db_name is not None:
            return self.database[self.database['name'] == db_name]['database_code']
        elif index is not None:
            return self.database.loc[index, 'database_code']

    def get_dataset_data(self, db_code, dataset_index=None, dataset_code=None, dataset_name=None):
        dataset_file = pd.read_csv(self.datasets[db_code], index_col=None)
        if dataset_index is not None:
            return dataset_file.loc[dataset_index]
        elif dataset_code is not None:
            return dataset_file[dataset_file['code'] == dataset_code]
        elif dataset_name is not None:
            return dataset_file[dataset_name['name'] == dataset_name]


    def save_database(self):
        current_page = 1
        url = f'https://www.quandl.com/api/v3/databases?current_page={current_page}&api_key={quandl.ApiConfig.api_key}'
        self.database = pd.DataFrame(columns=['id', 'name', 'database_code', 'description', 'datasets_count',
                                              'downloads', 'premium', 'image', 'favorite', 'url_name', 'exclusive'])
        while True:
            data = json.loads(requests.get(url).text)['databases']
            print(data)
            database = pd.DataFrame(columns=['id', 'name', 'database_code', 'description', 'datasets_count',
                                              'downloads', 'premium', 'image', 'favorite', 'url_name', 'exclusive'],
                                    data=data)

            print(database)
            if len(database) == 0:
                print('break')
                break
            else:
                free_data = database[database['premium'] == False]
                self.database = self.database.append(free_data, ignore_index=True)
                current_page += 1
                url = f'https://www.quandl.com/api/v3/databases?current_page={current_page}&api_key={quandl.ApiConfig.api_key}'

        self.database.reset_index(drop=True, inplace=True)
        self.database.to_csv(self.filepaths['config_filepath'])
        print(self.database)
        return self.database







