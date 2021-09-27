import pandas as pd
import numpy as np
import statsmodels.tsa.api as tsa
import ccxt

from ..source.time_units_map import TIME_MAP

class Calculator:
    def __init__(self):
        pass


    # converts timeframe from string code (e.g. '3M', '1H', etc.) to number in miliseconds
    @staticmethod
    def string_time_to_ms(timeframe):
        print(timeframe)
        return int(timeframe[:-1]) * TIME_MAP[timeframe[-1]]

    # convert timeframe to start date in UNIX timestamp (in miliseconds)

    def get_since(self, timeframe):
        return ccxt.Exchange.milliseconds() - self.string_time_to_ms(timeframe)

    def descriptive_stats(self, df):
        pass

    def adf_test(self, df):
        pass

    def kpss_test(self, df):
        pass

    def ols_model(self, df):
        pass

    def engle_granger(self, df):
        pass

    def johansen(self, df):
        pass

    def acf(self, df):
        pass

    def pacf(self, df):
        pass
