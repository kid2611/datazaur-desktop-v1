# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'charts_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(954, 661)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(5, 5, 951, 656))
        self.widget.setObjectName("widget")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 5, 51, 21))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget)
        self.pushButton_8.setGeometry(QtCore.QRect(795, 5, 21, 21))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setGeometry(QtCore.QRect(5, 5, 56, 21))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget)
        self.pushButton_13.setGeometry(QtCore.QRect(924, 5, 21, 21))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.widget)
        self.tabWidget_2.setGeometry(QtCore.QRect(5, 32, 940, 621))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(720, 5, 71, 21))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_6 = QtWidgets.QComboBox(self.widget)
        self.comboBox_6.setGeometry(QtCore.QRect(80, 5, 56, 21))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")

        self.retranslateUi(Form)
        self.tabWidget_2.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "CLEAR"))
        self.pushButton_8.setText(_translate("Form", "+"))
        self.comboBox_5.setItemText(0, _translate("Form", "12H"))
        self.comboBox_5.setItemText(1, _translate("Form", "1D"))
        self.comboBox_5.setItemText(2, _translate("Form", "2D"))
        self.comboBox_5.setItemText(3, _translate("Form", "3D"))
        self.comboBox_5.setItemText(4, _translate("Form", "4D"))
        self.comboBox_5.setItemText(5, _translate("Form", "5D"))
        self.comboBox_5.setItemText(6, _translate("Form", "6D"))
        self.comboBox_5.setItemText(7, _translate("Form", "1W"))
        self.comboBox_5.setItemText(8, _translate("Form", "2W"))
        self.comboBox_5.setItemText(9, _translate("Form", "3W"))
        self.comboBox_5.setItemText(10, _translate("Form", "1M"))
        self.comboBox_5.setItemText(11, _translate("Form", "2M"))
        self.comboBox_5.setItemText(12, _translate("Form", "3M"))
        self.comboBox_5.setItemText(13, _translate("Form", "4M"))
        self.comboBox_5.setItemText(14, _translate("Form", "5M"))
        self.comboBox_5.setItemText(15, _translate("Form", "6M"))
        self.comboBox_5.setItemText(16, _translate("Form", "9M"))
        self.comboBox_5.setItemText(17, _translate("Form", "1Y"))
        self.comboBox_5.setItemText(18, _translate("Form", "2Y"))
        self.comboBox_5.setItemText(19, _translate("Form", "3Y"))
        self.comboBox_5.setItemText(20, _translate("Form", "5Y"))
        self.comboBox_5.setItemText(21, _translate("Form", "10Y"))
        self.comboBox_5.setItemText(22, _translate("Form", "ALL"))
        self.pushButton_13.setText(_translate("Form", "X"))
        self.comboBox_3.setItemText(0, _translate("Form", "MACD"))
        self.comboBox_3.setItemText(1, _translate("Form", "RSI"))
        self.comboBox_3.setItemText(2, _translate("Form", "BOLLINGER BANDS"))
        self.comboBox_3.setItemText(3, _translate("Form", "STOCHASTIC OSCILLATOR"))
        self.comboBox_3.setItemText(4, _translate("Form", "EMA"))
        self.comboBox_3.setItemText(5, _translate("Form", "SMA"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
