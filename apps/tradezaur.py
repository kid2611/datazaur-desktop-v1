import ccxt
import yaml
import os
import pandas as pd
import ccxt


class TradeZaur:
    def __init__(self):
        self.exchanges = {}
        self.algorithms = {}


    def load_algorithms(self):
        pass

    def load_config(self):
        with open('settings/config.yaml') as config:
            self.config = yaml.safe_load(config)


    # connects to exchange
    def connect_exchange(self, exchange_id):
        if exchange_id in self.exchanges.keys():
            return self.exchanges[exchange_id]
        else:
            self.current_exchange = self.exchanges[exchange_id] = getattr(ccxt, exchange_id)({'enableRateLimit': True,
                                                                                'options': {'defaultType': 'future'}})
            self.exchanges[exchange_id] = self.current_exchange
            try:
                self.current_exchange.load_markets()
            except Exception as e:
                print(f'connection failed - error {e}')
            return self.current_exchange


    def buy(self, ticker, exchange, amount, price):
        pass

    def sell(self, ticker, exchange, amount, price):
        pass

    def buy_spread(self, **kwargs):
        pass

    def sell_spread(self, **kwargs):
        pass

    def close_trade(self, ticker, exchange, price, amount=1):
        pass

    def close_all_trades(self):
        pass




    def start_algorithm(self, algorithm_name):
        pass


    def stop_algorithm(self, algorithm_name):
        pass


    def stop_all_algorithms(self):
        pass


    def save_history(self):
        pass


    def load_history(self):
        pass



    def save_config(self):
        pass

    def save_algorithm(self, name):
        path = os.path.join(os.path.dirname(os.getcwd()), self.config['PATHS']['data']['algorithms'])

        with open(self.config['PATHS']['data']['algorithms'], 'r+'):
            pass


    def add_endo(self, ticker, exchange):
        pass

    def add_exog(self, ticker, exchange):
        pass

    # def toggle_const(self):
    #     self.const = not self.const
    #
    # def remove_variable(self, symbol):
    #     del self.variables[symbol]




    def adf_test(self):
        pass

    def kpss_test(self):
        pass

    def eg_test(self):
        pass

    def johansen_test(self):
        pass

    def backtest(self):
        pass


