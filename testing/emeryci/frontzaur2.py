
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.widgets.markets.markets_widget import MarketsWidget
from ui.widgets.trade.trade_widget import TradeWidget
from ui.widgets.algorithm_wizard import AlgorithmWizard
from ui.widgets.charts_widget import ChartsWidget
from ui.widgets.database_widget import DatabaseWidget
from ui.widgets.date_selector import DateSelector
from ui.widgets.donate_window import DonateWindow
from ui.widgets.news_widget import NewsWidget
from ui.widgets.scripts_widget import ScriptsWidget
from ui.widgets.watchlist_widget import WatchlistWidget




class FrontZaur(QtWidgets.QMainWindow):
    def __init__(self, datazaur):
        super().__init__()
        self.datazaur = datazaur

        self.markets = MarketsWidget()
        self.trade = TradeWidget()
        self.markets = MarketsWidget()
        self.markets = MarketsWidget()
        self.markets = MarketsWidget()
        self.markets = MarketsWidget()
        self.markets = MarketsWidget()
        self.wallet = MarketsWidget()





        self.widgets = {}


















