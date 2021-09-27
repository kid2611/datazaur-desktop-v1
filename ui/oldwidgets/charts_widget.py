

from my_charts import OHLCChart
from PyQt5 import QtCore, QtGui, QtWidgets


class ChartsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("Charts")
        self.resize(951, 659)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 951, 656))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.tabWidget = QtWidgets.QTabWidget(self.frame)
        self.tabWidget.setGeometry(QtCore.QRect(0, 40, 951, 616))
        self.tabWidget.setObjectName("tabWidget")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(5, 10, 66, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame)
        self.comboBox_2.setGeometry(QtCore.QRect(105, 10, 61, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame)
        self.comboBox_3.setGeometry(QtCore.QRect(645, 10, 86, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(740, 10, 25, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(775, 10, 56, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 10, 25, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def ohlc_chart(self, title, df):
        chart = OHLCChart(self.tabWidget, df)
        self.tabWidget.addTab(chart, title)

    def close_tab(self):
        self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Charts"))
        self.pushButton.setText(_translate("Form", "+"))
        self.pushButton_2.setText(_translate("Form", "clear"))
        self.pushButton_3.setText(_translate("Form", "X"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    charts = ChartsWidget(None)
    charts.show()
    sys.exit(app.exec_())
