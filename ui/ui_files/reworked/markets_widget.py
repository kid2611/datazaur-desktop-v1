# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rework_markets.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(957, 682)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 5, 951, 671))
        self.tabWidget.setMinimumSize(QtCore.QSize(600, 400))
        self.tabWidget.setMaximumSize(QtCore.QSize(951, 680))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(5, 10, 941, 626))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableView_2 = QtWidgets.QTableView(self.tab_8)
        self.tableView_2.setGeometry(QtCore.QRect(5, 5, 926, 586))
        self.tableView_2.setObjectName("tableView_2")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tableView_3 = QtWidgets.QTableView(self.tab_9)
        self.tableView_3.setGeometry(QtCore.QRect(5, 5, 926, 586))
        self.tableView_3.setObjectName("tableView_3")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(760, 5, 176, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.frame_7 = QtWidgets.QFrame(self.tab_2)
        self.frame_7.setGeometry(QtCore.QRect(0, 0, 946, 636))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.tabWidget_7 = QtWidgets.QTabWidget(self.frame_7)
        self.tabWidget_7.setGeometry(QtCore.QRect(195, 10, 751, 626))
        self.tabWidget_7.setObjectName("tabWidget_7")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.tableView_16 = QtWidgets.QTableView(self.tab_20)
        self.tableView_16.setGeometry(QtCore.QRect(0, 0, 746, 591))
        self.tableView_16.setObjectName("tableView_16")
        self.tabWidget_7.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.tableView_17 = QtWidgets.QTableView(self.tab_21)
        self.tableView_17.setGeometry(QtCore.QRect(0, 0, 746, 591))
        self.tableView_17.setObjectName("tableView_17")
        self.tabWidget_7.addTab(self.tab_21, "")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_14.setGeometry(QtCore.QRect(791, 7, 151, 25))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_9 = QtWidgets.QLabel(self.frame_7)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 51, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_7)
        self.label_10.setGeometry(QtCore.QRect(10, 45, 51, 17))
        self.label_10.setObjectName("label_10")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame_7)
        self.groupBox_8.setGeometry(QtCore.QRect(5, 320, 186, 311))
        self.groupBox_8.setObjectName("groupBox_8")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.groupBox_8)
        self.lineEdit_15.setGeometry(QtCore.QRect(10, 30, 166, 25))
        self.lineEdit_15.setClearButtonEnabled(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.listWidget_4 = QtWidgets.QListWidget(self.groupBox_8)
        self.listWidget_4.setGeometry(QtCore.QRect(10, 60, 166, 206))
        self.listWidget_4.setObjectName("listWidget_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_8)
        self.pushButton_8.setGeometry(QtCore.QRect(13, 274, 161, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.comboBox_15 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_15.setGeometry(QtCore.QRect(85, 40, 101, 25))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 946, 636))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.frame_2)
        self.tabWidget_4.setGeometry(QtCore.QRect(195, 10, 751, 626))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tableView_6 = QtWidgets.QTableView(self.tab_12)
        self.tableView_6.setGeometry(QtCore.QRect(0, 0, 746, 591))
        self.tableView_6.setObjectName("tableView_6")
        self.tabWidget_4.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tableView_7 = QtWidgets.QTableView(self.tab_13)
        self.tableView_7.setGeometry(QtCore.QRect(0, 0, 746, 591))
        self.tableView_7.setObjectName("tableView_7")
        self.tabWidget_4.addTab(self.tab_13, "")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(791, 7, 151, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 51, 17))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(10, 45, 51, 17))
        self.label_8.setObjectName("label_8")
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox_3.setGeometry(QtCore.QRect(5, 320, 186, 311))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(10, 30, 166, 25))
        self.lineEdit_8.setClearButtonEnabled(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setGeometry(QtCore.QRect(10, 60, 166, 206))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(13, 274, 161, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox_12 = QtWidgets.QComboBox(self.frame_2)
        self.comboBox_12.setGeometry(QtCore.QRect(85, 40, 101, 25))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.groupBox = QtWidgets.QGroupBox(self.tab_4)
        self.groupBox.setGeometry(QtCore.QRect(5, 10, 936, 626))
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(5, 65, 926, 556))
        self.tableView.setObjectName("tableView")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(5, 30, 111, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(800, 30, 131, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(125, 30, 71, 25))
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(345, 30, 71, 25))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(206, 30, 21, 21))
        self.label.setObjectName("label")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(225, 30, 111, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        self.dateEdit.setGeometry(QtCore.QRect(450, 30, 106, 25))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(570, 30, 156, 25))
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(780, 20, 16, 46))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(425, 20, 16, 46))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.frame_4 = QtWidgets.QFrame(self.tab_5)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 946, 636))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(782, 5, 161, 25))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.tabWidget_6 = QtWidgets.QTabWidget(self.frame_4)
        self.tabWidget_6.setGeometry(QtCore.QRect(0, 15, 946, 621))
        self.tabWidget_6.setObjectName("tabWidget_6")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.tableView_10 = QtWidgets.QTableView(self.tab_16)
        self.tableView_10.setGeometry(QtCore.QRect(10, 5, 926, 576))
        self.tableView_10.setObjectName("tableView_10")
        self.tabWidget_6.addTab(self.tab_16, "")
        self.tab_17 = QtWidgets.QWidget()
        self.tab_17.setObjectName("tab_17")
        self.tableView_11 = QtWidgets.QTableView(self.tab_17)
        self.tableView_11.setGeometry(QtCore.QRect(0, 5, 941, 581))
        self.tableView_11.setObjectName("tableView_11")
        self.tabWidget_6.addTab(self.tab_17, "")
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_4)
        self.comboBox_3.setGeometry(QtCore.QRect(670, 5, 86, 25))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_3.setGeometry(QtCore.QRect(595, 5, 71, 23))
        self.checkBox_3.setObjectName("checkBox_3")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.frame_3 = QtWidgets.QFrame(self.tab_6)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 946, 636))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.frame_3)
        self.tabWidget_5.setGeometry(QtCore.QRect(195, 15, 751, 621))
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.tableView_8 = QtWidgets.QTableView(self.tab_14)
        self.tableView_8.setGeometry(QtCore.QRect(5, 5, 741, 581))
        self.tableView_8.setObjectName("tableView_8")
        self.tabWidget_5.addTab(self.tab_14, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.tableView_9 = QtWidgets.QTableView(self.tab_15)
        self.tableView_9.setGeometry(QtCore.QRect(5, 5, 741, 581))
        self.tableView_9.setObjectName("tableView_9")
        self.tabWidget_5.addTab(self.tab_15, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tableView_12 = QtWidgets.QTableView(self.tab_18)
        self.tableView_12.setGeometry(QtCore.QRect(5, 5, 741, 581))
        self.tableView_12.setObjectName("tableView_12")
        self.tabWidget_5.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.tableView_13 = QtWidgets.QTableView(self.tab_19)
        self.tableView_13.setGeometry(QtCore.QRect(5, 5, 741, 581))
        self.tableView_13.setObjectName("tableView_13")
        self.tabWidget_5.addTab(self.tab_19, "")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(790, 12, 151, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_4.setGeometry(QtCore.QRect(5, 380, 186, 251))
        self.groupBox_4.setObjectName("groupBox_4")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(10, 30, 166, 25))
        self.lineEdit_10.setClearButtonEnabled(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.listWidget_3 = QtWidgets.QListWidget(self.groupBox_4)
        self.listWidget_3.setGeometry(QtCore.QRect(10, 60, 166, 151))
        self.listWidget_3.setObjectName("listWidget_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_4.setGeometry(QtCore.QRect(13, 215, 161, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_5.setGeometry(QtCore.QRect(5, 5, 186, 376))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_15 = QtWidgets.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(10, 30, 46, 25))
        self.label_15.setObjectName("label_15")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_4.setGeometry(QtCore.QRect(115, 30, 66, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_17 = QtWidgets.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 65, 51, 25))
        self.label_17.setObjectName("label_17")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_5.setGeometry(QtCore.QRect(80, 65, 101, 25))
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
        self.label_18 = QtWidgets.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 100, 61, 25))
        self.label_18.setObjectName("label_18")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_6.setGeometry(QtCore.QRect(80, 100, 101, 25))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_7 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_7.setGeometry(QtCore.QRect(60, 30, 46, 25))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 340, 161, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_19 = QtWidgets.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(10, 135, 66, 25))
        self.label_19.setObjectName("label_19")
        self.comboBox_8 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_8.setGeometry(QtCore.QRect(80, 135, 101, 25))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_20 = QtWidgets.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(10, 170, 66, 25))
        self.label_20.setObjectName("label_20")
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_9.setGeometry(QtCore.QRect(80, 170, 101, 25))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_21 = QtWidgets.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(10, 205, 66, 25))
        self.label_21.setObjectName("label_21")
        self.comboBox_10 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_10.setGeometry(QtCore.QRect(80, 205, 101, 25))
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.label_22 = QtWidgets.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(10, 240, 66, 25))
        self.label_22.setObjectName("label_22")
        self.comboBox_11 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_11.setGeometry(QtCore.QRect(80, 240, 101, 25))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox.setGeometry(QtCore.QRect(10, 275, 101, 23))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_5)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 310, 116, 23))
        self.checkBox_2.setObjectName("checkBox_2")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.frame_5 = QtWidgets.QFrame(self.tab_7)
        self.frame_5.setGeometry(QtCore.QRect(0, 5, 946, 631))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_6.setGeometry(QtCore.QRect(335, 5, 606, 121))
        self.groupBox_6.setObjectName("groupBox_6")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_6)
        self.textBrowser.setGeometry(QtCore.QRect(5, 25, 596, 91))
        self.textBrowser.setObjectName("textBrowser")
        self.groupBox_7 = QtWidgets.QGroupBox(self.frame_5)
        self.groupBox_7.setGeometry(QtCore.QRect(335, 135, 606, 491))
        self.groupBox_7.setObjectName("groupBox_7")
        self.tableView_14 = QtWidgets.QTableView(self.groupBox_7)
        self.tableView_14.setGeometry(QtCore.QRect(5, 25, 596, 461))
        self.tableView_14.setObjectName("tableView_14")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_12.setGeometry(QtCore.QRect(780, 128, 156, 25))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setGeometry(QtCore.QRect(5, 5, 326, 631))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.comboBox_14 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_14.setGeometry(QtCore.QRect(95, 45, 121, 25))
        self.comboBox_14.setObjectName("comboBox_14")
        self.label_23 = QtWidgets.QLabel(self.frame_6)
        self.label_23.setGeometry(QtCore.QRect(10, 10, 51, 25))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.frame_6)
        self.label_24.setGeometry(QtCore.QRect(10, 45, 66, 25))
        self.label_24.setObjectName("label_24")
        self.tableView_15 = QtWidgets.QTableView(self.frame_6)
        self.tableView_15.setGeometry(QtCore.QRect(10, 155, 306, 461))
        self.tableView_15.setObjectName("tableView_15")
        self.comboBox_13 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_13.setGeometry(QtCore.QRect(95, 10, 121, 25))
        self.comboBox_13.setObjectName("comboBox_13")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.comboBox_13.addItem("")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_13.setGeometry(QtCore.QRect(160, 125, 156, 25))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setGeometry(QtCore.QRect(228, 90, 86, 25))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_7.setGeometry(QtCore.QRect(228, 55, 86, 25))
        self.pushButton_7.setObjectName("pushButton_7")
        self.tabWidget.addTab(self.tab_7, "")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("Form", "market data"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("Form", "info"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "crypto"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_20), _translate("Form", "values"))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_21), _translate("Form", "info"))
        self.label_9.setText(_translate("Form", "filters"))
        self.label_10.setText(_translate("Form", "sector"))
        self.groupBox_8.setTitle(_translate("Form", "   countries"))
        self.pushButton_8.setText(_translate("Form", "get indexes"))
        self.comboBox_15.setItemText(0, _translate("Form", "energy"))
        self.comboBox_15.setItemText(1, _translate("Form", "technology"))
        self.comboBox_15.setItemText(2, _translate("Form", "industrials"))
        self.comboBox_15.setItemText(3, _translate("Form", "retail"))
        self.comboBox_15.setItemText(4, _translate("Form", "healthcare"))
        self.comboBox_15.setItemText(5, _translate("Form", "military"))
        self.comboBox_15.setItemText(6, _translate("Form", "finance"))
        self.comboBox_15.setItemText(7, _translate("Form", "mining"))
        self.comboBox_15.setItemText(8, _translate("Form", "services"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "indexes"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_12), _translate("Form", "values"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_13), _translate("Form", "info"))
        self.label_7.setText(_translate("Form", "filters"))
        self.label_8.setText(_translate("Form", "sector"))
        self.groupBox_3.setTitle(_translate("Form", "   countries"))
        self.pushButton_3.setText(_translate("Form", "get stonks"))
        self.comboBox_12.setItemText(0, _translate("Form", "energy"))
        self.comboBox_12.setItemText(1, _translate("Form", "technology"))
        self.comboBox_12.setItemText(2, _translate("Form", "industrials"))
        self.comboBox_12.setItemText(3, _translate("Form", "retail"))
        self.comboBox_12.setItemText(4, _translate("Form", "healthcare"))
        self.comboBox_12.setItemText(5, _translate("Form", "military"))
        self.comboBox_12.setItemText(6, _translate("Form", "finance"))
        self.comboBox_12.setItemText(7, _translate("Form", "mining"))
        self.comboBox_12.setItemText(8, _translate("Form", "services"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "equities"))
        self.groupBox.setTitle(_translate("Form", "   cross currency rates, historical rates and converter"))
        self.label.setText(_translate("Form", "="))
        self.pushButton.setText(_translate("Form", "get historical rates"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "FX"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_16), _translate("Form", "values"))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_17), _translate("Form", "info"))
        self.comboBox_3.setItemText(0, _translate("Form", "metals"))
        self.comboBox_3.setItemText(1, _translate("Form", "softs"))
        self.comboBox_3.setItemText(2, _translate("Form", "meats"))
        self.comboBox_3.setItemText(3, _translate("Form", "energy"))
        self.comboBox_3.setItemText(4, _translate("Form", "grain"))
        self.checkBox_3.setText(_translate("Form", "group"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "commodities"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_14), _translate("Form", "sovereign"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_15), _translate("Form", "corporate "))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_18), _translate("Form", "municipal"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_19), _translate("Form", "agencies"))
        self.groupBox_4.setTitle(_translate("Form", "   countries"))
        self.pushButton_4.setText(_translate("Form", "get bonds"))
        self.groupBox_5.setTitle(_translate("Form", "  filters"))
        self.label_15.setText(_translate("Form", "rating"))
        self.comboBox_4.setItemText(0, _translate("Form", "IG"))
        self.comboBox_4.setItemText(1, _translate("Form", "HY"))
        self.comboBox_4.setItemText(2, _translate("Form", "AAA"))
        self.comboBox_4.setItemText(3, _translate("Form", "AA+"))
        self.comboBox_4.setItemText(4, _translate("Form", "AA"))
        self.comboBox_4.setItemText(5, _translate("Form", "AA-"))
        self.comboBox_4.setItemText(6, _translate("Form", "A+"))
        self.comboBox_4.setItemText(7, _translate("Form", "A"))
        self.comboBox_4.setItemText(8, _translate("Form", "A-"))
        self.comboBox_4.setItemText(9, _translate("Form", "BBB+"))
        self.comboBox_4.setItemText(10, _translate("Form", "BBB"))
        self.comboBox_4.setItemText(11, _translate("Form", "BBB-"))
        self.comboBox_4.setItemText(12, _translate("Form", "BB+"))
        self.comboBox_4.setItemText(13, _translate("Form", "BB"))
        self.comboBox_4.setItemText(14, _translate("Form", "BB-"))
        self.comboBox_4.setItemText(15, _translate("Form", "B+"))
        self.comboBox_4.setItemText(16, _translate("Form", "B"))
        self.comboBox_4.setItemText(17, _translate("Form", "B-"))
        self.comboBox_4.setItemText(18, _translate("Form", "CCC+"))
        self.comboBox_4.setItemText(19, _translate("Form", "CCC"))
        self.comboBox_4.setItemText(20, _translate("Form", "CCC-"))
        self.comboBox_4.setItemText(21, _translate("Form", "CC"))
        self.comboBox_4.setItemText(22, _translate("Form", "C"))
        self.comboBox_4.setItemText(23, _translate("Form", "D"))
        self.label_17.setText(_translate("Form", "sector"))
        self.comboBox_5.setItemText(0, _translate("Form", "energy"))
        self.comboBox_5.setItemText(1, _translate("Form", "technology"))
        self.comboBox_5.setItemText(2, _translate("Form", "industrials"))
        self.comboBox_5.setItemText(3, _translate("Form", "retail"))
        self.comboBox_5.setItemText(4, _translate("Form", "healthcare"))
        self.comboBox_5.setItemText(5, _translate("Form", "military"))
        self.comboBox_5.setItemText(6, _translate("Form", "finance"))
        self.comboBox_5.setItemText(7, _translate("Form", "mining"))
        self.comboBox_5.setItemText(8, _translate("Form", "services"))
        self.label_18.setText(_translate("Form", "currency"))
        self.comboBox_7.setItemText(0, _translate("Form", ">"))
        self.comboBox_7.setItemText(1, _translate("Form", ">="))
        self.comboBox_7.setItemText(2, _translate("Form", "<"))
        self.comboBox_7.setItemText(3, _translate("Form", "<="))
        self.comboBox_7.setItemText(4, _translate("Form", "="))
        self.comboBox_7.setItemText(5, _translate("Form", "+/- 1 notch"))
        self.pushButton_5.setText(_translate("Form", "apply filters"))
        self.label_19.setText(_translate("Form", "seniority"))
        self.comboBox_8.setItemText(0, _translate("Form", "senior secured"))
        self.comboBox_8.setItemText(1, _translate("Form", "senior unsecured"))
        self.comboBox_8.setItemText(2, _translate("Form", "junior"))
        self.comboBox_8.setItemText(3, _translate("Form", "junior subordinated"))
        self.label_20.setText(_translate("Form", "type"))
        self.comboBox_9.setItemText(0, _translate("Form", "plain vanilla fixed rate"))
        self.comboBox_9.setItemText(1, _translate("Form", "floating rate"))
        self.comboBox_9.setItemText(2, _translate("Form", "convertible"))
        self.comboBox_9.setItemText(3, _translate("Form", "perpetual"))
        self.comboBox_9.setItemText(4, _translate("Form", "inflation-linked"))
        self.comboBox_9.setItemText(5, _translate("Form", "zero-coupon"))
        self.label_21.setText(_translate("Form", "duration"))
        self.comboBox_10.setItemText(0, _translate("Form", "Certificate of Deposit"))
        self.comboBox_10.setItemText(1, _translate("Form", "Bill ( < 1Y )"))
        self.comboBox_10.setItemText(2, _translate("Form", "Note ( 1-5Y )"))
        self.comboBox_10.setItemText(3, _translate("Form", "Bond ( 5Y+ )"))
        self.label_22.setText(_translate("Form", "options"))
        self.comboBox_11.setItemText(0, _translate("Form", "call"))
        self.comboBox_11.setItemText(1, _translate("Form", "put"))
        self.comboBox_11.setItemText(2, _translate("Form", "call + put"))
        self.checkBox.setText(_translate("Form", "structured"))
        self.checkBox_2.setText(_translate("Form", "collateralized"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "fixed income"))
        self.groupBox_6.setTitle(_translate("Form", "  description"))
        self.groupBox_7.setTitle(_translate("Form", "  datasets"))
        self.label_23.setText(_translate("Form", "source"))
        self.label_24.setText(_translate("Form", "category"))
        self.comboBox_13.setItemText(0, _translate("Form", "Investing.com"))
        self.comboBox_13.setItemText(1, _translate("Form", "Yahoo"))
        self.comboBox_13.setItemText(2, _translate("Form", "Quandl"))
        self.pushButton_6.setText(_translate("Form", "search"))
        self.pushButton_7.setText(_translate("Form", "chart"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "macro"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
