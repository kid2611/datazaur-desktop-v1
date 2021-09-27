

from PyQt5 import QtCore, QtGui, QtWidgets


class CalendarWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setObjectName("Form")
        self.resize(952, 677)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(-5, 0, 951, 676))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setGeometry(QtCore.QRect(10, 70, 936, 606))
        self.tableView.setObjectName("tableView")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(805, 35, 141, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 35, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(155, 35, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(250, 35, 81, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 35, 51, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(405, 35, 96, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(640, 35, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(355, 35, 46, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_5.setGeometry(QtCore.QRect(585, 35, 46, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_5.setFont(font)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(760, 35, 25, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_6.setGeometry(QtCore.QRect(675, 35, 76, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.comboBox_6.setFont(font)
        self.comboBox_6.setObjectName("comboBox_6")
        self.line = QtWidgets.QFrame(self.groupBox)
        self.line.setGeometry(QtCore.QRect(783, 25, 26, 46))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.groupBox)
        self.line_2.setGeometry(QtCore.QRect(335, 25, 16, 46))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(510, 35, 66, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "   economic calendar"))
        self.label.setText(_translate("Form", "filters"))
        self.comboBox_4.setItemText(0, _translate("Form", "Telegram"))
        self.comboBox_4.setItemText(1, _translate("Form", "SMS"))
        self.comboBox_4.setItemText(2, _translate("Form", "email"))
        self.pushButton.setText(_translate("Form", "+"))
        self.label_2.setText(_translate("Form", "alerts"))
        self.comboBox_5.setItemText(0, _translate("Form", "1h"))
        self.comboBox_5.setItemText(1, _translate("Form", "15 min"))
        self.comboBox_5.setItemText(2, _translate("Form", "30 min"))
        self.comboBox_5.setItemText(3, _translate("Form", "2h"))
        self.comboBox_5.setItemText(4, _translate("Form", "3h"))
        self.comboBox_5.setItemText(5, _translate("Form", "4h"))
        self.comboBox_5.setItemText(6, _translate("Form", "6h"))
        self.comboBox_5.setItemText(7, _translate("Form", "8h"))
        self.comboBox_5.setItemText(8, _translate("Form", "12h"))
        self.comboBox_5.setItemText(9, _translate("Form", "1d"))
        self.comboBox_5.setItemText(10, _translate("Form", "2d"))
        self.comboBox_5.setItemText(11, _translate("Form", "3d"))
        self.comboBox_5.setItemText(12, _translate("Form", "4d"))
        self.comboBox_5.setItemText(13, _translate("Form", "5d"))
        self.comboBox_5.setItemText(14, _translate("Form", "1w"))
        self.comboBox_5.setItemText(15, _translate("Form", "2w"))
        self.comboBox_5.setItemText(16, _translate("Form", "3w"))
        self.comboBox_5.setItemText(17, _translate("Form", "1M"))
        self.comboBox_5.setItemText(18, _translate("Form", "2M"))
        self.pushButton_2.setText(_translate("Form", "X"))
        self.label_3.setText(_translate("Form", "reminder"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = CalendarWidget(app)

    Form.show()
    sys.exit(app.exec_())