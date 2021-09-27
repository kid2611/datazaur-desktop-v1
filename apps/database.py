import sqlite3


class Database:
    def __init__(self, database='database0.db'):
        self.database = database
        self.connection = None
        self.connected = False
        self.cursor = False
        self.connect()
        self.create_tables()

    # connects to the database
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database)
            self.connected = True
            self.cursor = self.connection.cursor()
            print('Connection success')
        except sqlite3.Error or sqlite3.OperationalError as e:
            self.connected = False
            print(f'the error {e} occured')

    # closes connection to the database
    def disconnect(self):
        self.connection.commit()
        self.connection.close()
        self.connected = False

    # wrapper function to initialize database on first login (or if for whatever reason such tables don't exist)
    # creates tables for users' data (logins, hashed passwords and salts), exchanges' API keys, algorithms' data
    def create_tables(self):
        self.create_users_table()
        self.create_keys_table()
        self.create_algorithms_table()
        self.create_config_tables()

    # creates table for algorithms' data
    def create_algorithms_table(self):
        create_algorithms_table_query = """ 
        CREATE TABLE IF NOT EXISTS algorithms (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        coins TEXT,
        params TEXT,
        entry_z REAL,
        stop_loss_z REAL
        );
        """
        try:
            self.cursor.execute(create_algorithms_table_query)
            self.connection.commit()
            print('query executed create algo tables')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # creates table for users, hashes and salts
    def create_users_table(self):
        create_users_table_query = """ 
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        hash TEXT,
        salt TEXT
        );
        """
        try:
            self.cursor.execute(create_users_table_query)
            self.connection.commit()
            print('query executed create users table')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # creates table for API keys
    def create_keys_table(self):
        keys_table_query = """ 
        CREATE TABLE IF NOT EXISTS keys (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        exchange TEXT,
        public_key TEXT,
        private_key TEXT,
        salt TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
        );
        """
        try:
            self.cursor.execute(keys_table_query)
            self.connection.commit()
            print('query executed create keys table')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # creates table for statistical stat_tests (ADF, KPSS, JOHANSEN) and table linking users with configs (many to many)
    def create_config_tables(self):
        config_table_query = f"""
        CREATE TABLE IF NOT EXISTS config (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        johansen_det_order INTEGER DEFAULT 0,
        johansen_n_lags INTEGER DEFAULT 144,
        adf_reg TEXT DEFAULT 'c',
        adf_autolag TEXT DEFAULT 'AIC',
        adf_maxlag INTEGER DEFAULT 0,
        kpss_reg TEXT DEFAULT 'c',
        kpss_autolag TEXT DEFAULT 'auto',
        kpss_maxlag INTEGER DEFAULT 0
        );
        """
        config_users_table_query = f"""
        CREATE TABLE IF NOT EXISTS users_config (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        config_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(config_id) REFERENCES config(id)
        );
        """
        for query in [config_table_query, config_users_table_query]:
            try:
                self.cursor.execute(query)
                self.connection.commit()
                print('created cfg table')
            except sqlite3.Error or sqlite3.OperationalError as e:
                print(f'error {e}')

    # creates pricing data table
    def create_data_table(self, exchange, ticker, interval):
        table_name = ticker + '_' + exchange + '_' + interval
        create_data_table_query = f"""
        CREATE TABLE IF NOT EXISTS '{table_name}' (
        timestamp INTEGER PRIMARY KEY,
        open REAL,
        high REAL,
        low REAL,
        close REAL,
        volume REAL
        );
        """
        self.cursor = self.connection.cursor()
        try:
            self.cursor.execute(create_data_table_query)
            self.connection.commit()
            print('data table created')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')

    # saves stat_tests' settings for current user
    def save_config(self, username, config):
        user_id = self.execute_read_query(f"""SELECT id FROM users WHERE username="{username}";""")[0][0]
        config_keys = tuple(config.keys())
        config_values = tuple(config.values())
        placeholder = tuple(len(config) * ['?'])
        save_config_query = f"""
        INSERT INTO config "{config_keys}"
        VALUES "{placeholder}";
        """
        try:
            self.cursor.execute(save_config_query, config_values)
            self.connection.commit()
            config_id = self.execute_read_query(f"""SELECT MAX("id") FROM config;""")[0][0]
            link_config_to_user_query = f"""
            INSERT INTO users_config ("{user_id}", "{config_id}")
            VALUES (?, ?);
            """
            self.cursor.execute(link_config_to_user_query)
            self.connection.commit()
            print(f'config saved for {username}')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')
            return False

    # saves an algorithm
    def save_algorithm(self, algorithm):
        params = (algorithm.name, str(algorithm.params.index.values), str(algorithm.params.values), algorithm.entry_z,
                  algorithm.stop_loss_z)
        save_algorithm_query = """
        INSERT INTO algorithms (name, coins, params, entry_z, stop_loss_z)
        VALUES (?, ?, ?, ?, ?);
        """
        try:
            self.cursor.execute(save_algorithm_query, params)
            self.connection.commit()
            print('algo saved')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # deletes an algorithm
    def delete_algorithm(self, algorithm_name):
        delete_query = f"""
        DELETE FROM algorithms
        WHERE name = "{algorithm_name}"
        """
        try:
            self.cursor.execute(delete_query)
            self.connection.commit()
            print('algo deleted')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')

    # adds login, hash and salt to the database
    def add_hash(self, username, hsh, salt):
        add_hash_query = """
        INSERT INTO 
        users (username, hash, salt)
        VALUES 
        (?, ?, ?); 
        """
        try:
            self.cursor.execute(add_hash_query, (username, hsh, salt))
            self.connection.commit()
            print('hash added')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # gets hash and salt from database
    def get_hash(self, username):
        get_hash_query = f"""
        SELECT hash, salt
        FROM users
        WHERE username = "{username}";
        """
        results = None
        try:
            return self.cursor.execute(get_hash_query).fetchall()
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # adds exchange API keys to database
    def add_keys(self, username, exchange, public_key, private_key, salt):
        add_keys_query = """
        INSERT INTO 
        keys (username, exchange, public_key, private_key, salt)
        VALUES 
        (?, ?, ?, ?, ?); 
        """
        try:
            self.cursor.execute(add_keys_query, (username, exchange, public_key, private_key, salt))
            self.connection.commit()
            print('keys added')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # returns API keys of given user
    def get_api_keys(self, username):
        get_api_keys_query = f"""
        SELECT exchange, public_key, private_key, salt
        FROM api_keys
        WHERE username = "{username}";
        """
        try:
            return self.cursor.execute(get_api_keys_query).fetchall()
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')

    # inserts pricing data (OHLC) to the database
    def insert_data(self, exchange, ticker, frequency, data):
        self.create_data_table(exchange, ticker, frequency)
        table_name = exchange + '_' + ticker + '_' + frequency
        insert_data_query = f"""
        INSERT INTO  "{table_name}" (timestamp, open, high, low, close, volume)
        VALUES (?, ?, ?, ?, ?, ?);
        """
        self.cursor = self.connection.cursor()
        try:
            self.cursor.executemany(insert_data_query, data)
            self.connection.commit()
            print('data inserted')
            return True
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')
            return False

    # returns pricing data
    def get_data(self, exchange, ticker, interval, since):
        table_name = ticker + '_' + exchange + '_' + interval
        get_data_query = f"""
        SELECT timestamp, open, high, low, close, volume
        FROM "{table_name}"
        WHERE "timestamp" >= "{since}";
        """
        self.cursor = self.connection.cursor()
        try:
            return self.execute_read_query(get_data_query)
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')

    # drops table
    def drop_table(self, table_name):
        delete_query = f"""
        DROP TABLE "{table_name}"
        """
        try:
            self.execute_query(delete_query)
            print('table dropped')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')

    # deletes pricing data
    def delete_data(self, exchange, ticker, frequency, start_date, end_date):
        table_name = exchange + '_' + ticker + '_' + frequency
        delete_query = f"""
        DELETE FROM "{table_name}"
        WHERE timestamp >= "{start_date}" AND timestamp <= "{end_date}";
        """
        try:
            self.execute_query(delete_query)
            print('data deleted')
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')

    # returns list of tables
    def get_tables_list(self):
        query = f"""
        SELECT name FROM sqlite_master 
        WHERE type = "table" 
        AND name NOT LIKE "sqlite_%"
        ORDER BY 1;
        """
        try:
            return self.execute_read_query(query)
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e}')

    # executes sqlite3 query
    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            print('query executed')
            return True
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')
            return False

    # executes sqlite3 read query
    def execute_read_query(self, query):
        try:
            return self.cursor.execute(query).fetchall()
        except sqlite3.Error or sqlite3.OperationalError as e:
            print(f'error {e} occured')
            return False


