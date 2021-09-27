import ccxt
import datetime
import time
import pandas as pd
from sqlalchemy.orm import Session


class ArbitrageBot:
    def __init__(self, backend):
        self.backend = backend
        self.exchanges = {}
        self.currency = None
        self.tickers = []


    def new_algorithm(self, **kwargs):
        self.backend.db.new_arbitrage_algorithm(**kwargs)

    def config_algorithm(self, **kwargs):
        self.backend.db.config_arbitrage_algorithm(**kwargs)

    def add_currency(self, currency):
        self.currency = currency


    def add_tickers(self, tickers):
        self.tickers += tickers



    def add_exchange(self, exchange_id):
        if exchange_id in self.exchanges.keys():
            return
        else:
            exchange = getattr('ccxt', exchange_id)({'enableRateLimit': True, 'options': {'defaultType': 'future'}})
            self.exchanges[exchange_id] = exchange


    def connect_to_exchanges(self):
        for exchange in self.exchanges.values():
            t = datetime.datetime.now().timestamp()
            exchange.load_markets()
            print(f'Exchange:{exchange.id} loaded markets in {datetime.datetime.now().timestamp() - t} sec.')


    def find_quotes(self, coin, quote_currency):
        quotes = {exchange: [] for exchange in self.exchanges.keys()}
        self.connect_to_exchanges()
        for exchange in self.exchanges:
            quotes[exchange.id] += [ticker for ticker in exchange.symbols if ticker.split('/')[0] == coin and
                                    ticker.split('/')[1] == quote_currency]
        return quotes


    def monitor_tickers(self, coin, quote_currency, refresh_rate=15):
        quotes = self.find_quotes(coin, quote_currency)
        print(quotes)
        df = pd.DataFrame(columns=pd.MultiIndex.from_tuples((self.exchanges.keys(), ('bid', 'ask'))))
        print(df)

        while True:

            for exchange, quote in quotes.items():
                t = datetime.datetime.now().timestamp()
                data = self.exchanges[exchange].fetch_ticker(quote)
                print(data)
                df.loc[t, [exchange, 'bid']] = data.loc[quote, 'bid']


            time.sleep(refresh_rate)

