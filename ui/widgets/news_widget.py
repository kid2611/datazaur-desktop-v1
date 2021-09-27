
from PyQt5 import QtCore, QtGui, QtWidgets


class NewsWidget(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setObjectName("NEWS")
        self.resize(1086, 655)
        self.widget = QtWidgets.QWidget(self)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1076, 651))
        self.widget.setObjectName("widget")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_38.setGeometry(QtCore.QRect(898, 5, 175, 26))
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.line_9 = QtWidgets.QFrame(self.widget)
        self.line_9.setGeometry(QtCore.QRect(875, -7, 10, 41))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.tableView_8 = QtWidgets.QTableView(self.widget)
        self.tableView_8.setGeometry(QtCore.QRect(4, 38, 1069, 608))
        self.tableView_8.setObjectName("tableView_8")
        self.pushButton_45 = QtWidgets.QPushButton(self.widget)
        self.pushButton_45.setGeometry(QtCore.QRect(5, 5, 106, 26))
        font = QtGui.QFont()
        font.setFamily("FixedsysTTF")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(4)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setStyleSheet("font: 32 11pt \"FixedsysTTF\";")
        self.pushButton_45.setObjectName("pushButton_45")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_45.setText(_translate("Form", "WEBSITES"))



