
from PyQt5 import QtWidgets, QtCore
from apps.datazaur import Datazaur
from apps.arbitrage import ArbitrageBot
from apps.datazaur import Datazaur
from apps.datazaur import Datazaur
from ui.newfront88 import Ui_MainWindow as Ui_View
from ui.newtrade88 import Ui_Form as Ui_Trade
from ui.newmonitor88 import Ui_Form as Ui_Monitor
from ui.newalgos88 import Ui_Form as Ui_Algorithms
from ui.newexplo88 import Ui_Form as Ui_Explorer
from ui.newnews88 import Ui_Form as Ui_News
from ui.newtrends88 import Ui_Form as Ui_Trends
from ui.newcalendar88 import Ui_Form as Ui_Calendar
from ui.arbitrage_widget import Ui_Form as Ui_Arbitrage
import time
import investpy
from models.dataframemodel import DataFrameModel
import pandas as pd


class Controller:
    def __init__(self, backend, view):
        self.backend = backend
        self.view = view

        trade = QtWidgets.QWidget(self.view.tabWidget)
        trade_ui = Ui_Trade()
        trade_ui.setupUi(trade)

        monitor = QtWidgets.QWidget(self.view.tabWidget)
        monitor_ui = Ui_Monitor()
        monitor_ui.setupUi(monitor)

        algorithms = QtWidgets.QWidget(self.view.tabWidget)
        algorithms_ui = Ui_Algorithms()
        algorithms_ui.setupUi(algorithms)

        arbitrage = QtWidgets.QWidget(self.view.tabWidget)
        arbitrage_ui = Ui_Arbitrage()
        arbitrage_ui.setupUi(arbitrage)

        explorer = QtWidgets.QWidget(self.view.tabWidget)
        explorer_ui = Ui_Explorer()
        explorer_ui.setupUi(explorer)

        news = QtWidgets.QWidget(self.view.tabWidget)
        news_ui = Ui_News()
        news_ui.setupUi(news)

        trends = QtWidgets.QWidget(self.view.tabWidget)
        trends_ui = Ui_Trends()
        trends_ui.setupUi(trends)

        calendar = QtWidgets.QWidget(self.view.tabWidget)
        calendar_ui = Ui_Calendar()
        calendar_ui.setupUi(calendar)

        self.view.tabWidget.addTab(monitor, 'monitor')
        self.view.tabWidget.addTab(trade, 'trade')
        self.view.tabWidget.addTab(algorithms, 'algorithms')
        self.view.tabWidget.addTab(arbitrage, 'arbitrage')
        self.view.tabWidget.addTab(explorer, 'macro')
        self.view.tabWidget.addTab(news, 'news')
        self.view.tabWidget.addTab(calendar, 'calendar')
        self.view.tabWidget.addTab(trends, 'trends')









if __name__ == "__main__":
    import sys
    app = Datazaur(sys.argv)
    view = QtWidgets.QMainWindow()
    view.setGeometry(QtCore.QRect(0, 0, 950, 700))
    ui = Ui_View()
    ui.setupUi(view)
    controller = Controller(app, ui)
    view.show()

    sys.exit(app.exec_())
