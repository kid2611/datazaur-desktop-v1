# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ultimate_front_nowidgets.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1204, 725)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1196, 681))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_13 = QtWidgets.QFrame(self.frame)
        self.frame_13.setGeometry(QtCore.QRect(230, 0, 966, 681))
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.tabWidget = QtWidgets.QTabWidget(self.frame_13)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 966, 681))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("\n"
"selection-background-color: rgb(114, 159, 207);")
        self.tabWidget.setObjectName("tabWidget")
        self.frame_14 = QtWidgets.QFrame(self.frame)
        self.frame_14.setGeometry(QtCore.QRect(0, 0, 226, 681))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.line_2 = QtWidgets.QFrame(self.frame_14)
        self.line_2.setGeometry(QtCore.QRect(219, 0, 16, 49))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label = QtWidgets.QLabel(self.frame_14)
        self.label.setGeometry(QtCore.QRect(9, 10, 216, 36))
        font = QtGui.QFont()
        font.setFamily("Fixedsys Excelsior 3.01")
        font.setPointSize(38)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("font: 75 italic 38pt \"Fixedsys Excelsior 3.01\";\n"
"\n"
"")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.frame_14)
        self.groupBox.setGeometry(QtCore.QRect(5, 58, 216, 616))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(5, 30, 206, 581))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget_3 = QtWidgets.QListWidget(self.widget)
        self.listWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listWidget_3.setObjectName("listWidget_3")
        self.verticalLayout.addWidget(self.listWidget_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_37 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout.addWidget(self.pushButton_37, 0, 0, 1, 1)
        self.pushButton_39 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_39.setObjectName("pushButton_39")
        self.gridLayout.addWidget(self.pushButton_39, 0, 1, 1, 1)
        self.pushButton_36 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_36.setObjectName("pushButton_36")
        self.gridLayout.addWidget(self.pushButton_36, 1, 0, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout.addWidget(self.pushButton_38, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox_10 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_10.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.groupBox_10.setObjectName("groupBox_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_10)
        self.gridLayout_6.setContentsMargins(-1, -1, 3, 3)
        self.gridLayout_6.setHorizontalSpacing(3)
        self.gridLayout_6.setVerticalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_42 = QtWidgets.QLabel(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.label_42.setObjectName("label_42")
        self.gridLayout_6.addWidget(self.label_42, 0, 0, 1, 2)
        self.comboBox_13 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_13.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_13.setObjectName("comboBox_13")
        self.gridLayout_6.addWidget(self.comboBox_13, 0, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout_6.addWidget(self.radioButton_3, 1, 0, 1, 1)
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout_6.addWidget(self.radioButton_4, 2, 0, 1, 1)
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.radioButton_5.setObjectName("radioButton_5")
        self.gridLayout_6.addWidget(self.radioButton_5, 3, 0, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.groupBox_10)
        self.comboBox_9.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_9.setObjectName("comboBox_9")
        self.gridLayout_6.addWidget(self.comboBox_9, 1, 2, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_6.addWidget(self.dateTimeEdit, 2, 2, 1, 1)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(self.groupBox_10)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.gridLayout_6.addWidget(self.dateTimeEdit_2, 3, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_10)
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_35.setGeometry(QtCore.QRect(165, 60, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.pushButton_35.setObjectName("pushButton_35")
        self.line = QtWidgets.QFrame(self.frame_14)
        self.line.setGeometry(QtCore.QRect(1, 40, 225, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1204, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuWidgets = QtWidgets.QMenu(self.menubar)
        self.menuWidgets.setObjectName("menuWidgets")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuStats = QtWidgets.QMenu(self.menubar)
        self.menuStats.setObjectName("menuStats")
        self.menuModels = QtWidgets.QMenu(self.menuStats)
        self.menuModels.setObjectName("menuModels")
        self.menuCorrelograms = QtWidgets.QMenu(self.menuStats)
        self.menuCorrelograms.setObjectName("menuCorrelograms")
        self.menuStationarity = QtWidgets.QMenu(self.menuStats)
        self.menuStationarity.setObjectName("menuStationarity")
        self.menuCointegration = QtWidgets.QMenu(self.menuStats)
        self.menuCointegration.setObjectName("menuCointegration")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionContribute = QtWidgets.QAction(MainWindow)
        self.actionContribute.setObjectName("actionContribute")
        self.actionDonate = QtWidgets.QAction(MainWindow)
        self.actionDonate.setObjectName("actionDonate")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionDatabase = QtWidgets.QAction(MainWindow)
        self.actionDatabase.setObjectName("actionDatabase")
        self.actionOptions_Calculator = QtWidgets.QAction(MainWindow)
        self.actionOptions_Calculator.setObjectName("actionOptions_Calculator")
        self.actionCrypto_Wallet = QtWidgets.QAction(MainWindow)
        self.actionCrypto_Wallet.setObjectName("actionCrypto_Wallet")
        self.actionBlockchain_Explorer = QtWidgets.QAction(MainWindow)
        self.actionBlockchain_Explorer.setObjectName("actionBlockchain_Explorer")
        self.actionOLS = QtWidgets.QAction(MainWindow)
        self.actionOLS.setObjectName("actionOLS")
        self.actionACF = QtWidgets.QAction(MainWindow)
        self.actionACF.setObjectName("actionACF")
        self.actionPACF = QtWidgets.QAction(MainWindow)
        self.actionPACF.setObjectName("actionPACF")
        self.actionADF_test = QtWidgets.QAction(MainWindow)
        self.actionADF_test.setObjectName("actionADF_test")
        self.actionKPSS_test = QtWidgets.QAction(MainWindow)
        self.actionKPSS_test.setObjectName("actionKPSS_test")
        self.actionEngle_Granger = QtWidgets.QAction(MainWindow)
        self.actionEngle_Granger.setObjectName("actionEngle_Granger")
        self.actionJohansen = QtWidgets.QAction(MainWindow)
        self.actionJohansen.setObjectName("actionJohansen")
        self.actionDescriptive_statistics = QtWidgets.QAction(MainWindow)
        self.actionDescriptive_statistics.setObjectName("actionDescriptive_statistics")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionReport_a_bug = QtWidgets.QAction(MainWindow)
        self.actionReport_a_bug.setObjectName("actionReport_a_bug")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionAccount = QtWidgets.QAction(MainWindow)
        self.actionAccount.setObjectName("actionAccount")
        self.actionOpen_database = QtWidgets.QAction(MainWindow)
        self.actionOpen_database.setObjectName("actionOpen_database")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.menuFile.addAction(self.actionOpen_database)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionMinimize)
        self.menuFile.addAction(self.actionClose)
        self.menuWidgets.addAction(self.actionDatabase)
        self.menuWidgets.addAction(self.actionOptions_Calculator)
        self.menuWidgets.addAction(self.actionCrypto_Wallet)
        self.menuWidgets.addAction(self.actionBlockchain_Explorer)
        self.menuSettings.addAction(self.actionSettings)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionAccount)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionContribute)
        self.menuHelp.addAction(self.actionDonate)
        self.menuHelp.addAction(self.actionReport_a_bug)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menuModels.addAction(self.actionOLS)
        self.menuCorrelograms.addAction(self.actionACF)
        self.menuCorrelograms.addAction(self.actionPACF)
        self.menuStationarity.addAction(self.actionADF_test)
        self.menuStationarity.addAction(self.actionKPSS_test)
        self.menuCointegration.addAction(self.actionEngle_Granger)
        self.menuCointegration.addAction(self.actionJohansen)
        self.menuStats.addAction(self.actionDescriptive_statistics)
        self.menuStats.addAction(self.menuModels.menuAction())
        self.menuStats.addAction(self.menuCorrelograms.menuAction())
        self.menuStats.addAction(self.menuStationarity.menuAction())
        self.menuStats.addAction(self.menuCointegration.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuWidgets.menuAction())
        self.menubar.addAction(self.menuStats.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Datazaur"))
        self.label.setText(_translate("MainWindow", "DATAZAUR"))
        self.groupBox.setTitle(_translate("MainWindow", " SEARCH   "))
        self.pushButton_5.setText(_translate("MainWindow", "CLEAR"))
        self.pushButton.setText(_translate("MainWindow", "SEARCH"))
        self.pushButton_37.setText(_translate("MainWindow", "QUOTES"))
        self.pushButton_39.setText(_translate("MainWindow", "CHART"))
        self.pushButton_36.setText(_translate("MainWindow", "ADD TO VARS"))
        self.pushButton_38.setText(_translate("MainWindow", "INFO"))
        self.groupBox_10.setTitle(_translate("MainWindow", " TIMEFRAME"))
        self.label_42.setText(_translate("MainWindow", "  INTERVAL"))
        self.radioButton_3.setText(_translate("MainWindow", "LAST"))
        self.radioButton_4.setText(_translate("MainWindow", "SINCE"))
        self.radioButton_5.setText(_translate("MainWindow", "RANGE"))
        self.pushButton_35.setText(_translate("MainWindow", "FILTERS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuWidgets.setTitle(_translate("MainWindow", "Widgets"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuStats.setTitle(_translate("MainWindow", "Stats"))
        self.menuModels.setTitle(_translate("MainWindow", "Models"))
        self.menuCorrelograms.setTitle(_translate("MainWindow", "Correlograms"))
        self.menuStationarity.setTitle(_translate("MainWindow", "Stationarity"))
        self.menuCointegration.setTitle(_translate("MainWindow", "Cointegration"))
        self.actionHelp.setText(_translate("MainWindow", "Manual"))
        self.actionContribute.setText(_translate("MainWindow", "Contribute"))
        self.actionDonate.setText(_translate("MainWindow", "Donate"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionDatabase.setText(_translate("MainWindow", "Database"))
        self.actionOptions_Calculator.setText(_translate("MainWindow", "Options Calculator"))
        self.actionCrypto_Wallet.setText(_translate("MainWindow", "Crypto Wallet"))
        self.actionBlockchain_Explorer.setText(_translate("MainWindow", "Blockchain Explorer"))
        self.actionOLS.setText(_translate("MainWindow", "OLS"))
        self.actionACF.setText(_translate("MainWindow", "ACF"))
        self.actionPACF.setText(_translate("MainWindow", "PACF"))
        self.actionADF_test.setText(_translate("MainWindow", "ADF-test"))
        self.actionKPSS_test.setText(_translate("MainWindow", "KPSS-test"))
        self.actionEngle_Granger.setText(_translate("MainWindow", "Engle-Granger"))
        self.actionJohansen.setText(_translate("MainWindow", "Johansen"))
        self.actionDescriptive_statistics.setText(_translate("MainWindow", "Descriptive statistics"))
        self.actionSave.setText(_translate("MainWindow", "Save.."))
        self.actionSettings.setText(_translate("MainWindow", "Theme"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionReport_a_bug.setText(_translate("MainWindow", "Report a bug"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionAccount.setText(_translate("MainWindow", "Account"))
        self.actionOpen_database.setText(_translate("MainWindow", "Open database"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
