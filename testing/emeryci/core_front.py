
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.widgets.markets.markets_widget import MarketsWidget
from ui.widgets.trade.trade_widget import TradeWidget
from ui.widgets.algorithm_wizard import AlgorithmWizard
from ui.widgets.charts_widget import ChartsWidget
from ui.widgets.database_widget import DatabaseWidget

from ui.widgets.donate_window import DonateWindow
from ui.widgets.news_widget import NewsWidget
from ui.widgets.scripts_widget import ScriptsWidget
from ui.widgets.watchlist_widget import WatchlistWidget
import datetime
import pandas as pd


class FrontZaur(QtWidgets.QMainWindow):
    def __init__(self, datazaur):
        super().__init__()

        self.datazaur = datazaur

        self.apps = {
            'markets': MarketsWidget(),
            'trade': TradeWidget(),
            'charts': ChartsWidget(),
            'watchlist': WatchlistWidget(),
            'wizard': AlgorithmWizard(),
            'news': NewsWidget(),
            'scripts': ScriptsWidget()
        }


        self.setObjectName("self")
        self.resize(1220, 765)

        self.disable_inactive_widgets()
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.radioButton.clicked.connect(self.select_timeframe)
        self.radioButton_2.clicked.connect(self.select_timeframe)
        self.radioButton_3.clicked.connect(self.select_timeframe)

    def disable_inactive_widgets(self):
        self.comboBox_37.setDisabled(True)
        self.dateTimeEdit_3.setEnabled(True)
        self.dateTimeEdit_4.setDisabled(True)
        self.dateTimeEdit_4.setDate(datetime.date.today())

    def open_app(self, name):
        app = self.apps['name']
        self.tabWidget.addTab(app, name)

    def close_app(self):
        current_tab = self.tabWidget

    def search(self):
        symbol = self.lineEdit_7.text()

    def select_timeframe(self):
        if self.radioButton.isChecked():
            self.comboBox_37.setEnabled(True)
            self.dateTimeEdit_3.setDisabled(True)
            self.dateTimeEdit_4.setDisabled(True)
        elif self.radioButton_2.isChecked():
            self.comboBox_37.setDisabled(True)
            self.dateTimeEdit_3.setEnabled(True)
            self.dateTimeEdit_4.setDisabled(True)
        else:
            self.comboBox_37.setDisabled(True)
            self.dateTimeEdit_3.setEnabled(True)
            self.dateTimeEdit_4.setEnabled(True)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))