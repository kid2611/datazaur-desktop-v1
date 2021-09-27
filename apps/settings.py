import json



class Settings:
    def __init__(self, name, open_charts, default_crypto, default_fiat, theme, font, auto_login, saved_exchanges,
                 default_widgets,
                 adf_config, kpss_config, johansen_config, macd_config, rsi_config, stoch_config, bollinger_config,
                 vwap_config, moving_averages,
                 store_metadata, store_crypto, store_equities, store_indexes, store_fi, store_fx, store_macro,
                 store_statistical_tests, store_backtests, store_trade_history,
                 autodelete_data, autodelete_data_peroid, autodelete_metadata, autodelete_metadata_peroid):

        self.name = name
        self.open_charts = open_charts
        self.default_crypto = default_crypto
        self.default_fiat = default_fiat
        self.theme = theme
        self.font = font
        self.auto_login = auto_login
        self.saved_exchanges = saved_exchanges
        self.default_widgets = default_widgets

        self.adf_config = adf_config
        self.kpss_config = kpss_config
        self.johansen_config = johansen_config
        self.macd_config = macd_config
        self.rsi_config = rsi_config
        self.stoch_config = stoch_config
        self.bollinger_config = bollinger_config
        self.vwap_config = vwap_config
        self.moving_averages = moving_averages

        self.store_metadata = store_metadata
        self.store_crypto = store_crypto
        self.store_equities = store_equities
        self.store_indexes = store_indexes
        self.store_fi = store_fi
        self.store_fx = store_fx
        self.store_macro = store_macro
        self.store_statistical_tests = store_statistical_tests
        self.store_backtests = store_backtests
        self.store_trade_history = store_trade_history
        self.autodelete_data = autodelete_data
        self.autodelete_data_peroid = autodelete_data_peroid
        self.autodelete_metadata = autodelete_metadata
        self.autodelete_metadata_peroid = autodelete_metadata_peroid


    def save_to_file(self):
        pass






