# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(978, 661)
        self.tabWidget_4 = QtWidgets.QTabWidget(Form)
        self.tabWidget_4.setGeometry(QtCore.QRect(0, 0, 971, 656))
        self.tabWidget_4.setStyleSheet("font: 12pt \"Ubuntu\";")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_4.setGeometry(QtCore.QRect(80, 5, 96, 25))
        self.comboBox_4.setObjectName("comboBox_4")
        self.label_6 = QtWidgets.QLabel(self.tab_16)
        self.label_6.setGeometry(QtCore.QRect(10, 5, 66, 25))
        self.label_6.setObjectName("label_6")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_16)
        self.comboBox_5.setGeometry(QtCore.QRect(275, 5, 86, 25))
        self.comboBox_5.setObjectName("comboBox_5")
        self.label_7 = QtWidgets.QLabel(self.tab_16)
        self.label_7.setGeometry(QtCore.QRect(200, 5, 76, 25))
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(self.tab_16)
        self.frame.setGeometry(QtCore.QRect(0, 35, 966, 586))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(5, 0, 956, 581))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(120, 260))
        self.groupBox_4.setMaximumSize(QtCore.QSize(216, 650))
        self.groupBox_4.setSizeIncrement(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setAutoFillBackground(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableView_19 = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_19.setGeometry(QtCore.QRect(7, 30, 172, 546))
        self.tableView_19.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView_19.setObjectName("tableView_19")
        self.tableView_19.horizontalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(120, 260))
        self.groupBox_5.setMaximumSize(QtCore.QSize(216, 600))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.tableView_3 = QtWidgets.QTableView(self.groupBox_5)
        self.tableView_3.setGeometry(QtCore.QRect(7, 30, 172, 546))
        self.tableView_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView_3.setObjectName("tableView_3")
        self.tableView_3.horizontalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_6.setMinimumSize(QtCore.QSize(120, 260))
        self.groupBox_6.setMaximumSize(QtCore.QSize(216, 600))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.tableView_5 = QtWidgets.QTableView(self.groupBox_6)
        self.tableView_5.setGeometry(QtCore.QRect(7, 30, 172, 546))
        self.tableView_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView_5.setObjectName("tableView_5")
        self.tableView_5.horizontalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_7.setMinimumSize(QtCore.QSize(120, 260))
        self.groupBox_7.setMaximumSize(QtCore.QSize(216, 600))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_7.setFont(font)
        self.groupBox_7.setObjectName("groupBox_7")
        self.tableView_4 = QtWidgets.QTableView(self.groupBox_7)
        self.tableView_4.setGeometry(QtCore.QRect(7, 30, 172, 546))
        self.tableView_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView_4.setObjectName("tableView_4")
        self.tableView_4.horizontalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.groupBox_7)
        self.groupBox_8 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_8.setEnabled(True)
        self.groupBox_8.setMinimumSize(QtCore.QSize(120, 260))
        self.groupBox_8.setMaximumSize(QtCore.QSize(216, 600))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("")
        self.groupBox_8.setObjectName("groupBox_8")
        self.tableView_6 = QtWidgets.QTableView(self.groupBox_8)
        self.tableView_6.setGeometry(QtCore.QRect(7, 30, 172, 546))
        self.tableView_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableView_6.setObjectName("tableView_6")
        self.tableView_6.horizontalHeader().setVisible(False)
        self.horizontalLayout.addWidget(self.groupBox_8)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_16)
        self.pushButton_5.setGeometry(QtCore.QRect(400, 5, 96, 26))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("font: 11pt \"Ubuntu\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_16)
        self.lineEdit_2.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.tabWidget_4.addTab(self.tab_16, "")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.tabWidget_10 = QtWidgets.QTabWidget(self.tab_18)
        self.tabWidget_10.setGeometry(QtCore.QRect(0, 5, 966, 616))
        self.tabWidget_10.setStyleSheet("font: 63 11pt \"FixedsysTTF\";")
        self.tabWidget_10.setObjectName("tabWidget_10")
        self.tab_33 = QtWidgets.QWidget()
        self.tab_33.setObjectName("tab_33")
        self.tableView = QtWidgets.QTableView(self.tab_33)
        self.tableView.setGeometry(QtCore.QRect(3, 4, 956, 581))
        self.tableView.setObjectName("tableView")
        self.tabWidget_10.addTab(self.tab_33, "")
        self.tab_34 = QtWidgets.QWidget()
        self.tab_34.setObjectName("tab_34")
        self.tableView_31 = QtWidgets.QTableView(self.tab_34)
        self.tableView_31.setGeometry(QtCore.QRect(3, 4, 956, 581))
        self.tableView_31.setObjectName("tableView_31")
        self.tabWidget_10.addTab(self.tab_34, "")
        self.tab_35 = QtWidgets.QWidget()
        self.tab_35.setObjectName("tab_35")
        self.tableView_32 = QtWidgets.QTableView(self.tab_35)
        self.tableView_32.setGeometry(QtCore.QRect(3, 4, 956, 581))
        self.tableView_32.setObjectName("tableView_32")
        self.tabWidget_10.addTab(self.tab_35, "")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_18)
        self.lineEdit_3.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.tabWidget_4.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.tableView_7 = QtWidgets.QTableView(self.tab_19)
        self.tableView_7.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_7.setObjectName("tableView_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_19)
        self.lineEdit_4.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(self.tab_19)
        self.label_8.setGeometry(QtCore.QRect(5, 5, 66, 25))
        self.label_8.setObjectName("label_8")
        self.comboBox_6 = QtWidgets.QComboBox(self.tab_19)
        self.comboBox_6.setGeometry(QtCore.QRect(75, 5, 96, 25))
        self.comboBox_6.setObjectName("comboBox_6")
        self.tabWidget_4.addTab(self.tab_19, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_20)
        self.lineEdit_5.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.tableView_8 = QtWidgets.QTableView(self.tab_20)
        self.tableView_8.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_8.setObjectName("tableView_8")
        self.label_9 = QtWidgets.QLabel(self.tab_20)
        self.label_9.setGeometry(QtCore.QRect(5, 5, 66, 25))
        self.label_9.setObjectName("label_9")
        self.comboBox_7 = QtWidgets.QComboBox(self.tab_20)
        self.comboBox_7.setGeometry(QtCore.QRect(75, 5, 96, 25))
        self.comboBox_7.setObjectName("comboBox_7")
        self.tabWidget_4.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_21)
        self.lineEdit_6.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.tableView_9 = QtWidgets.QTableView(self.tab_21)
        self.tableView_9.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_9.setObjectName("tableView_9")
        self.label_13 = QtWidgets.QLabel(self.tab_21)
        self.label_13.setGeometry(QtCore.QRect(5, 5, 66, 25))
        self.label_13.setObjectName("label_13")
        self.comboBox_11 = QtWidgets.QComboBox(self.tab_21)
        self.comboBox_11.setGeometry(QtCore.QRect(75, 5, 96, 25))
        self.comboBox_11.setObjectName("comboBox_11")
        self.tabWidget_4.addTab(self.tab_21, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.tab)
        self.dateTimeEdit.setGeometry(QtCore.QRect(845, 5, 116, 26))
        self.dateTimeEdit.setStyleSheet("font: 9pt \"Ubuntu\";")
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(700, 5, 136, 26))
        self.checkBox.setObjectName("checkBox")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(10, 5, 67, 26))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(180, 5, 66, 26))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab)
        self.comboBox_3.setGeometry(QtCore.QRect(275, 5, 66, 26))
        self.comboBox_3.setObjectName("comboBox_3")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(250, 5, 26, 26))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(80, 5, 91, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(345, 5, 21, 26))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(15)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 63 15pt \"FixedsysTTF\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(365, 5, 146, 26))
        self.label_5.setObjectName("label_5")
        self.tableView_10 = QtWidgets.QTableView(self.tab)
        self.tableView_10.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_10.setObjectName("tableView_10")
        self.tabWidget_4.addTab(self.tab, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.comboBox = QtWidgets.QComboBox(self.tab_23)
        self.comboBox.setGeometry(QtCore.QRect(60, 5, 101, 25))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.tab_23)
        self.label.setGeometry(QtCore.QRect(5, 5, 51, 25))
        self.label.setObjectName("label")
        self.tableView_11 = QtWidgets.QTableView(self.tab_23)
        self.tableView_11.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_11.setObjectName("tableView_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.tab_23)
        self.lineEdit_7.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.tabWidget_4.addTab(self.tab_23, "")
        self.tab_24 = QtWidgets.QWidget()
        self.tab_24.setObjectName("tab_24")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.tab_24)
        self.lineEdit_8.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.tableView_12 = QtWidgets.QTableView(self.tab_24)
        self.tableView_12.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_12.setObjectName("tableView_12")
        self.label_10 = QtWidgets.QLabel(self.tab_24)
        self.label_10.setGeometry(QtCore.QRect(5, 5, 66, 25))
        self.label_10.setObjectName("label_10")
        self.comboBox_8 = QtWidgets.QComboBox(self.tab_24)
        self.comboBox_8.setGeometry(QtCore.QRect(75, 5, 96, 25))
        self.comboBox_8.setObjectName("comboBox_8")
        self.tabWidget_4.addTab(self.tab_24, "")
        self.tab_25 = QtWidgets.QWidget()
        self.tab_25.setObjectName("tab_25")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.tab_25)
        self.lineEdit_9.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.tableView_13 = QtWidgets.QTableView(self.tab_25)
        self.tableView_13.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_13.setObjectName("tableView_13")
        self.label_11 = QtWidgets.QLabel(self.tab_25)
        self.label_11.setGeometry(QtCore.QRect(5, 5, 66, 25))
        self.label_11.setObjectName("label_11")
        self.comboBox_9 = QtWidgets.QComboBox(self.tab_25)
        self.comboBox_9.setGeometry(QtCore.QRect(75, 5, 96, 25))
        self.comboBox_9.setObjectName("comboBox_9")
        self.tabWidget_4.addTab(self.tab_25, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab_22)
        self.lineEdit_10.setGeometry(QtCore.QRect(820, 5, 131, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.tableView_14 = QtWidgets.QTableView(self.tab_22)
        self.tableView_14.setGeometry(QtCore.QRect(5, 35, 959, 586))
        self.tableView_14.setObjectName("tableView_14")
        self.label_12 = QtWidgets.QLabel(self.tab_22)
        self.label_12.setGeometry(QtCore.QRect(5, 5, 66, 25))
        self.label_12.setObjectName("label_12")
        self.comboBox_10 = QtWidgets.QComboBox(self.tab_22)
        self.comboBox_10.setGeometry(QtCore.QRect(75, 5, 96, 25))
        self.comboBox_10.setObjectName("comboBox_10")
        self.tabWidget_4.addTab(self.tab_22, "")

        self.retranslateUi(Form)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_10.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_6.setText(_translate("Form", "country"))
        self.label_7.setText(_translate("Form", "currency"))
        self.groupBox_4.setTitle(_translate("Form", "  crypto"))
        self.groupBox_5.setTitle(_translate("Form", " indexes"))
        self.groupBox_6.setTitle(_translate("Form", " forex"))
        self.groupBox_7.setTitle(_translate("Form", " bonds"))
        self.groupBox_8.setTitle(_translate("Form", " commodities"))
        self.pushButton_5.setText(_translate("Form", "settings"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), _translate("Form", "mix"))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_33), _translate("Form", "prices"))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_34), _translate("Form", "info"))
        self.tabWidget_10.setTabText(self.tabWidget_10.indexOf(self.tab_35), _translate("Form", "global metrics"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_18), _translate("Form", "crypto"))
        self.label_8.setText(_translate("Form", "country"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_19), _translate("Form", "stocks"))
        self.label_9.setText(_translate("Form", "country"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_20), _translate("Form", "indexes"))
        self.label_13.setText(_translate("Form", "country"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_21), _translate("Form", "bonds"))
        self.checkBox.setText(_translate("Form", "historical rates"))
        self.label_2.setText(_translate("Form", "convert"))
        self.label_3.setText(_translate("Form", "to"))
        self.label_4.setText(_translate("Form", "="))
        self.label_5.setText(_translate("Form", "TextLabel"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab), _translate("Form", "forex"))
        self.label.setText(_translate("Form", "group"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_23), _translate("Form", "commodities"))
        self.label_10.setText(_translate("Form", "country"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_24), _translate("Form", "ETFs"))
        self.label_11.setText(_translate("Form", "country"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_25), _translate("Form", "funds"))
        self.label_12.setText(_translate("Form", "country"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_22), _translate("Form", "certificates"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
