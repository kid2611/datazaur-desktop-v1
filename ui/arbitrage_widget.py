# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arbitrage_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(949, 647)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 0, 946, 641))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 75, 171, 191))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.tableView_10 = QtWidgets.QTableView(self.groupBox_3)
        self.tableView_10.setGeometry(QtCore.QRect(10, 60, 126, 121))
        self.tableView_10.setObjectName("tableView_10")
        self.pushButton_48 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_48.setGeometry(QtCore.QRect(145, 30, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_48.setCheckable(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_49.setGeometry(QtCore.QRect(145, 60, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_49.setObjectName("pushButton_49")
        self.comboBox_18 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_18.setGeometry(QtCore.QRect(10, 30, 126, 24))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_18.setFont(font)
        self.comboBox_18.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_18.setObjectName("comboBox_18")
        self.pushButton_56 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_56.setGeometry(QtCore.QRect(145, 90, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_57.setGeometry(QtCore.QRect(145, 120, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_57.setObjectName("pushButton_57")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(5, 10, 126, 25))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.pushButton_59 = QtWidgets.QPushButton(self.widget)
        self.pushButton_59.setGeometry(QtCore.QRect(210, 40, 96, 26))
        self.pushButton_59.setStyleSheet("")
        self.pushButton_59.setObjectName("pushButton_59")
        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(0, 65, 311, 16))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.line_3.setFont(font)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(135, 10, 171, 25))
        self.lineEdit_5.setStyleSheet("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.groupBox_9 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_9.setGeometry(QtCore.QRect(325, 445, 411, 186))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("")
        self.groupBox_9.setObjectName("groupBox_9")
        self.tabWidget_9 = QtWidgets.QTabWidget(self.groupBox_9)
        self.tabWidget_9.setGeometry(QtCore.QRect(5, 25, 306, 156))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget_9.setFont(font)
        self.tabWidget_9.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.tabWidget_9.setObjectName("tabWidget_9")
        self.tab_30 = QtWidgets.QWidget()
        self.tab_30.setObjectName("tab_30")
        self.listWidget_9 = QtWidgets.QListWidget(self.tab_30)
        self.listWidget_9.setGeometry(QtCore.QRect(3, 3, 296, 119))
        self.listWidget_9.setObjectName("listWidget_9")
        self.tabWidget_9.addTab(self.tab_30, "")
        self.tab_31 = QtWidgets.QWidget()
        self.tab_31.setObjectName("tab_31")
        self.listWidget_10 = QtWidgets.QListWidget(self.tab_31)
        self.listWidget_10.setGeometry(QtCore.QRect(3, 3, 296, 119))
        self.listWidget_10.setObjectName("listWidget_10")
        self.tabWidget_9.addTab(self.tab_31, "")
        self.widget1 = QtWidgets.QWidget()
        self.widget1.setObjectName("widget1")
        self.listWidget_12 = QtWidgets.QListWidget(self.widget1)
        self.listWidget_12.setGeometry(QtCore.QRect(3, 3, 296, 119))
        self.listWidget_12.setObjectName("listWidget_12")
        self.tabWidget_9.addTab(self.widget1, "")
        self.tab_32 = QtWidgets.QWidget()
        self.tab_32.setObjectName("tab_32")
        self.listWidget_11 = QtWidgets.QListWidget(self.tab_32)
        self.listWidget_11.setGeometry(QtCore.QRect(3, 3, 296, 119))
        self.listWidget_11.setObjectName("listWidget_11")
        self.tabWidget_9.addTab(self.tab_32, "")
        self.layoutWidget_2 = QtWidgets.QWidget(self.groupBox_9)
        self.layoutWidget_2.setGeometry(QtCore.QRect(320, 45, 82, 131))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_62 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_62.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_62.setObjectName("pushButton_62")
        self.verticalLayout.addWidget(self.pushButton_62)
        self.pushButton_63 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_63.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_63.setObjectName("pushButton_63")
        self.verticalLayout.addWidget(self.pushButton_63)
        self.pushButton_65 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_65.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_65.setObjectName("pushButton_65")
        self.verticalLayout.addWidget(self.pushButton_65)
        self.pushButton_64 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_64.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.pushButton_64.setObjectName("pushButton_64")
        self.verticalLayout.addWidget(self.pushButton_64)
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setGeometry(QtCore.QRect(5, 270, 306, 366))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.tableView_11 = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_11.setGeometry(QtCore.QRect(10, 65, 286, 291))
        self.tableView_11.setObjectName("tableView_11")
        self.pushButton_50 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_50.setGeometry(QtCore.QRect(275, 35, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_50.setCheckable(True)
        self.pushButton_50.setObjectName("pushButton_50")
        self.pushButton_54 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_54.setGeometry(QtCore.QRect(240, 35, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_60 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_60.setGeometry(QtCore.QRect(10, 30, 121, 26))
        self.pushButton_60.setStyleSheet("")
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_55 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_55.setGeometry(QtCore.QRect(205, 35, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setStyleSheet("font: 63 10pt \"Ubuntu Bold\";")
        self.pushButton_55.setObjectName("pushButton_55")
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setGeometry(QtCore.QRect(180, 75, 131, 66))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_19 = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_19.setGeometry(QtCore.QRect(10, 30, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_19.setFont(font)
        self.comboBox_19.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_19.setObjectName("comboBox_19")
        self.groupBox_6 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_6.setGeometry(QtCore.QRect(180, 145, 131, 66))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.comboBox_20 = QtWidgets.QComboBox(self.groupBox_6)
        self.comboBox_20.setGeometry(QtCore.QRect(10, 30, 111, 24))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_20.setFont(font)
        self.comboBox_20.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_20.setObjectName("comboBox_20")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(307, 0, 10, 73))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox_7 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_7.setGeometry(QtCore.QRect(325, 10, 276, 271))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.groupBox_7.setFont(font)
        self.groupBox_7.setStyleSheet("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_6.setGeometry(QtCore.QRect(195, 30, 71, 25))
        self.lineEdit_6.setStyleSheet("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_7.setGeometry(QtCore.QRect(195, 65, 71, 25))
        self.lineEdit_7.setStyleSheet("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_8.setGeometry(QtCore.QRect(195, 100, 71, 25))
        self.lineEdit_8.setStyleSheet("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox_7)
        self.label_4.setGeometry(QtCore.QRect(10, 30, 146, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_7)
        self.label_5.setGeometry(QtCore.QRect(10, 65, 146, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_7)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 181, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.comboBox_21 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_21.setGeometry(QtCore.QRect(160, 135, 106, 24))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_21.setFont(font)
        self.comboBox_21.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_21.setObjectName("comboBox_21")
        self.comboBox_21.addItem("")
        self.label_7 = QtWidgets.QLabel(self.groupBox_7)
        self.label_7.setGeometry(QtCore.QRect(10, 135, 146, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.comboBox_22 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_22.setGeometry(QtCore.QRect(160, 170, 106, 24))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_22.setFont(font)
        self.comboBox_22.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_22.setObjectName("comboBox_22")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.comboBox_22.addItem("")
        self.label_8 = QtWidgets.QLabel(self.groupBox_7)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 126, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setGeometry(QtCore.QRect(10, 205, 76, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("")
        self.label_9.setObjectName("label_9")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit_9.setGeometry(QtCore.QRect(195, 205, 71, 25))
        self.lineEdit_9.setStyleSheet("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_7)
        self.label_10.setGeometry(QtCore.QRect(10, 240, 101, 25))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("")
        self.label_10.setObjectName("label_10")
        self.comboBox_23 = QtWidgets.QComboBox(self.groupBox_7)
        self.comboBox_23.setGeometry(QtCore.QRect(160, 240, 106, 24))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_23.setFont(font)
        self.comboBox_23.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_23.setObjectName("comboBox_23")
        self.comboBox_23.addItem("")
        self.comboBox_23.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(180, 215, 131, 66))
        self.groupBox.setObjectName("groupBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setGeometry(QtCore.QRect(10, 30, 111, 26))
        self.spinBox_2.setMaximum(3600)
        self.spinBox_2.setProperty("value", 15)
        self.spinBox_2.setObjectName("spinBox_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setGeometry(QtCore.QRect(325, 295, 281, 136))
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_66 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_66.setGeometry(QtCore.QRect(15, 35, 156, 36))
        self.pushButton_66.setStyleSheet("")
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_61 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_61.setGeometry(QtCore.QRect(115, 85, 156, 36))
        self.pushButton_61.setStyleSheet("")
        self.pushButton_61.setObjectName("pushButton_61")
        self.pushButton_67 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_67.setGeometry(QtCore.QRect(15, 85, 91, 36))
        self.pushButton_67.setStyleSheet("")
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_68 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_68.setGeometry(QtCore.QRect(180, 35, 91, 36))
        self.pushButton_68.setStyleSheet("")
        self.pushButton_68.setObjectName("pushButton_68")
        self.groupBox_17 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_17.setGeometry(QtCore.QRect(610, 10, 206, 149))
        font = QtGui.QFont()
        self.groupBox_17.setFont(font)
        self.groupBox_17.setStyleSheet("")
        self.groupBox_17.setObjectName("groupBox_17")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_17)
        self.formLayout.setContentsMargins(3, 3, 3, 3)
        self.formLayout.setObjectName("formLayout")
        self.label_44 = QtWidgets.QLabel(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.label_44.setObjectName("label_44")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.comboBox_16 = QtWidgets.QComboBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_16.setFont(font)
        self.comboBox_16.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_16.setObjectName("comboBox_16")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_16)
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.radioButton_6.setChecked(True)
        self.radioButton_6.setObjectName("radioButton_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.radioButton_6)
        self.comboBox_12 = QtWidgets.QComboBox(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.comboBox_12.setFont(font)
        self.comboBox_12.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.comboBox_12.setObjectName("comboBox_12")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBox_12)
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.radioButton_7.setObjectName("radioButton_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.radioButton_7)
        self.dateTimeEdit_3 = QtWidgets.QDateTimeEdit(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEdit_3.setFont(font)
        self.dateTimeEdit_3.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit_3)
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setStyleSheet("font: 10pt \"Ubuntu\";")
        self.radioButton_8.setObjectName("radioButton_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.radioButton_8)
        self.dateTimeEdit_4 = QtWidgets.QDateTimeEdit(self.groupBox_17)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.dateTimeEdit_4.setFont(font)
        self.dateTimeEdit_4.setStyleSheet("font: 8pt \"Ubuntu\";")
        self.dateTimeEdit_4.setObjectName("dateTimeEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.dateTimeEdit_4)

        self.retranslateUi(Form)
        self.tabWidget_9.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_3.setTitle(_translate("Form", "  exchanges"))
        self.pushButton_48.setText(_translate("Form", "+"))
        self.pushButton_49.setText(_translate("Form", "X"))
        self.pushButton_56.setText(_translate("Form", "S"))
        self.pushButton_57.setText(_translate("Form", "C"))
        self.label_3.setText(_translate("Form", "algorithm name"))
        self.pushButton_59.setText(_translate("Form", "save"))
        self.groupBox_9.setTitle(_translate("Form", " database"))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_30), _translate("Form", "algorithms"))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_31), _translate("Form", "exchanges"))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.widget1), _translate("Form", "quotes"))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_32), _translate("Form", "configs"))
        self.pushButton_62.setText(_translate("Form", "save"))
        self.pushButton_63.setText(_translate("Form", "load"))
        self.pushButton_65.setText(_translate("Form", "info"))
        self.pushButton_64.setText(_translate("Form", "delete"))
        self.groupBox_4.setTitle(_translate("Form", " quotes"))
        self.pushButton_50.setText(_translate("Form", "X"))
        self.pushButton_54.setText(_translate("Form", "i"))
        self.pushButton_60.setText(_translate("Form", "find quotes"))
        self.pushButton_55.setText(_translate("Form", "S"))
        self.groupBox_5.setTitle(_translate("Form", " coin"))
        self.groupBox_6.setTitle(_translate("Form", "  quote currency"))
        self.groupBox_7.setTitle(_translate("Form", " parameters"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p>Percentage difference between lowest/highest price and consensus level (e.g. entry value of 10 means opening long (short) position when lowest (highest) price is at least 10% lower (higher) than consensus value.</p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Form", "entry level (% diff)"))
        self.label_5.setText(_translate("Form", "take profit (% diff)"))
        self.label_6.setText(_translate("Form", "stop loss (% drawdown)"))
        self.comboBox_21.setItemText(0, _translate("Form", "Volume-Weighted Average Price"))
        self.label_7.setText(_translate("Form", "consensus method"))
        self.comboBox_22.setItemText(0, _translate("Form", "long"))
        self.comboBox_22.setItemText(1, _translate("Form", "short"))
        self.comboBox_22.setItemText(2, _translate("Form", "long and short"))
        self.label_8.setText(_translate("Form", "position side(s)"))
        self.label_9.setText(_translate("Form", "leverage"))
        self.label_10.setText(_translate("Form", "market type"))
        self.comboBox_23.setItemText(0, _translate("Form", "spot"))
        self.comboBox_23.setItemText(1, _translate("Form", "futures"))
        self.groupBox.setTitle(_translate("Form", " refresh rate (s)"))
        self.groupBox_2.setTitle(_translate("Form", " actions"))
        self.pushButton_66.setText(_translate("Form", "start monitoring"))
        self.pushButton_61.setText(_translate("Form", "start trading"))
        self.pushButton_67.setText(_translate("Form", "config"))
        self.pushButton_68.setText(_translate("Form", "backtest"))
        self.groupBox_17.setTitle(_translate("Form", "timeframe"))
        self.label_44.setText(_translate("Form", "interval"))
        self.radioButton_6.setText(_translate("Form", "last"))
        self.radioButton_7.setText(_translate("Form", "since"))
        self.radioButton_8.setText(_translate("Form", "range"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
