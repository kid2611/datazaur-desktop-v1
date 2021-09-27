import yfinance
from PyQt5 import QtWidgets, QtCore
from pandasmodel import PandasModel
import pandas as pd
from ui.components.my_charts import OHLCChart
from ui.components.my_tables import MyTable


# widget fetching historical stock prices and fundamental data (financial statements, shareholder info, ESG info,
#
class FundamentalsWindow(QtWidgets.QWidget):
    def __init__(self, ticker):
        super().__init__()
        self.setStyleSheet("background-color: rgb(6, 14, 32);\n"
                            "color: rgb(255, 255, 255);\n"
                            "font: 75 11pt \"Ubuntu Bold\";")
        self.data = yfinance.Ticker(ticker)
        self.ticker = ticker
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 931, 531))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 921, 511))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.MyTable_6 = MyTable(self.tab_2)
        self.MyTable_6.setGeometry(QtCore.QRect(3, 3, 861, 480))
        self.MyTable_6.setObjectName("MyTable_6")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 871, 496))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.MyTable_3 = MyTable(self.tab_7)
        self.MyTable_3.setGeometry(QtCore.QRect(10, 10, 851, 480))
        self.MyTable_3.setObjectName("MyTable_3")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.MyTable_4 = MyTable(self.tab_8)
        self.MyTable_4.setGeometry(QtCore.QRect(10, 10, 851, 480))
        self.MyTable_4.setObjectName("MyTable_4")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.MyTable_5 = MyTable(self.tab_9)
        self.MyTable_5.setGeometry(QtCore.QRect(10, 10, 851, 480))
        self.MyTable_5.setObjectName("MyTable_5")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.MyTable = MyTable(self.tab_4)
        self.MyTable.setGeometry(QtCore.QRect(10, 10, 361, 480))
        self.MyTable.setObjectName("MyTable")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 0, 443, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.MyTable_7 = MyTable(self.groupBox_4)
        self.MyTable_7.setGeometry(QtCore.QRect(10, 30, 411, 136))
        self.MyTable_7.setObjectName("MyTable_7")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_4.setGeometry(QtCore.QRect(10, 165, 780, 308))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.MyTable_12 = MyTable(self.tab_15)
        self.MyTable_12.setGeometry(QtCore.QRect(10, 10, 721, 308))
        self.MyTable_12.setObjectName("MyTable_12")
        self.tabWidget_4.addTab(self.tab_15, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.MyTable_13 = MyTable(self.tab_16)
        self.MyTable_13.setGeometry(QtCore.QRect(10, 10, 721, 310))
        self.MyTable_13.setObjectName("MyTable_13")
        self.tabWidget_4.addTab(self.tab_16, "")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.MyTable_8 = MyTable(self.tab_6)
        self.MyTable_8.setGeometry(QtCore.QRect(10, 10, 391, 460))
        self.MyTable_8.setObjectName("MyTable_8")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.MyTable_9 = MyTable(self.tab_12)
        self.MyTable_9.setGeometry(QtCore.QRect(10, 10, 441, 460))
        self.MyTable_9.setObjectName("MyTable_9")
        self.tabWidget.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.MyTable_10 = MyTable(self.tab_13)
        self.MyTable_10.setGeometry(QtCore.QRect(10, 10, 531, 460))
        self.MyTable_10.setObjectName("MyTable_10")
        self.tabWidget.addTab(self.tab_13, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_14)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 10, 171, 480))
        self.groupBox_3.setObjectName("groupBox_3")
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 151, 451))
        self.listWidget.setObjectName("listWidget")
        self.tabWidget.addTab(self.tab_14, "")

        self.fill_data()
        self.format_tables()
        self.retranslateUi()

        QtCore.QMetaObject.connectSlotsByName(self)

    def fill_data(self):
        stock_prices = pd.DataFrame(yfinance.download(self.ticker))[['Open', 'High', 'Low', 'Close', 'Volume']]
        stock_prices.index = pd.to_datetime(stock_prices.index).view('int64') / 1000000
        chart = OHLCChart(self.tab_10, stock_prices)
        chart.setGeometry(QtCore.QRect(3, 3, 882, 423))
        chart.graph.resize(882, 423)
        info = pd.DataFrame(self.data.info.items())
        self.MyTable_6.setModel(PandasModel(info))

        for df in [self.data.balance_sheet, self.data.financials, self.data.cashflow]:
            df.columns = map(lambda x: str(x)[:10], df.columns)

        divs = self.data.actions
        divs.index = map(lambda x: str(x)[:10], divs.index)

        for table, df in zip([self.MyTable_3, self.MyTable_4, self.MyTable_5, self.MyTable, self.MyTable_7,
                              self.MyTable_12, self.MyTable_13, self.MyTable_8, self.MyTable_9,
                              self.MyTable_10], [self.data.balance_sheet, self.data.financials, self.data.cashflow,
                                                   divs, self.data.major_holders, self.data.institutional_holders,
                                                   self.data.mutualfund_holders, self.data.sustainability,
                                                   self.data.calendar, self.data.recommendations]):
            table.setModel(PandasModel(df))

    def format_tables(self):
        for table in [self.MyTable_4, self.MyTable_5]:
            for i in range(4):
                table.setColumnWidth(i, 125)
                self.MyTable_3.setColumnWidth(i, 150)

        for table in [self.MyTable_6, self.MyTable_7]:
            table.horizontalHeader().hide()

        for table in [self.MyTable_6, self.MyTable_7, self.MyTable_12, self.MyTable_13]:
            table.verticalHeader().hide()

        self.MyTable.setColumnWidth(1, 130)
        self.MyTable_6.setColumnWidth(0, 200)
        self.MyTable_6.setColumnWidth(1, 600)
        self.MyTable_7.setColumnWidth(1, 262)
        self.MyTable_12.setColumnWidth(0, 220)
        self.MyTable_13.setColumnWidth(0, 220)
        self.MyTable_12.setColumnWidth(4, 140)
        self.MyTable_13.setColumnWidth(4, 140)
        self.MyTable_8.setColumnWidth(0, 170)
        self.MyTable_10.setColumnWidth(0, 150)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", self.ticker))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("Form", "stock"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("Form", "bonds"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "market data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "info"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("Form", "balance sheet"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "income statement"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Form", "cashflow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "financials"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "dividends & splits"))
        self.groupBox_4.setTitle(_translate("Form", "breakdown"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_15), _translate("Form", "institutional holders"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), _translate("Form", "mutual funds"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "holders"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "sustainablity"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_12), _translate("Form", "calendar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_13), _translate("Form", "analysis"))
        self.groupBox_3.setTitle(_translate("Form", "options expiration dates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_14), _translate("Form", "options"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = FundamentalsWindow("AAPL")
    ui.show()
    sys.exit(app.exec_())

