import pandas
from pandas import DataFrame


class Portfolio:
    def __init__(self, name, currency='USD'):
        self.name = name
        self.currency = currency
        self.assets = DataFrame(data=None, columns=[], dtyoe=float)
        self.value = 0


    def add_asset(self, asset_id, amount, source):
        self.assets[asset_id] = amount
