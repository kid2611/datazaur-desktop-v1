from ui.oldwidgets.frontzaur import FrontZaur
from ui.account_creator import AccountCreator
from PyQt5 import QtWidgets, QtCore
from apps.auth import Authenticator


class LoginScreen(QtWidgets.QWidget):
    def __init__(self, backend):
        super().__init__()
        self.datazaur = backend
        self.auth = Authenticator()
        self.resize(308, 318)
        self.groupBox = QtWidgets.QGroupBox(self)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 291, 301))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_35.setGeometry(QtCore.QRect(10, 70, 271, 31))
        self.lineEdit_35.setInputMask("")
        self.lineEdit_35.setFrame(True)
        self.lineEdit_35.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_36.setGeometry(QtCore.QRect(10, 140, 271, 31))
        self.lineEdit_36.setInputMask("")
        self.lineEdit_36.setFrame(True)
        self.lineEdit_36.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 40, 111, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_33.setGeometry(QtCore.QRect(160, 190, 121, 41))
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_34.setGeometry(QtCore.QRect(10, 190, 121, 41))
        self.pushButton_34.setObjectName("pushButton_34")
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_35.setGeometry(QtCore.QRect(160, 250, 121, 41))
        self.pushButton_35.setObjectName("pushButton_35")

        self.retranslateUi()

        self.pushButton_33.clicked.connect(self.login)
        self.pushButton_34.clicked.connect(self.new_account)
        self.pushButton_35.clicked.connect(self.close)

        QtCore.QMetaObject.connectSlotsByName(self)

    # checks password against hash and logs in
    def login(self):
        error_dialog = QtWidgets.QErrorMessage(self)
        username = self.lineEdit_35.text().lower()
        password = self.lineEdit_36.text()
        if not username:
            error_dialog.showMessage('Please input username.')
        elif not password:
            error_dialog.showMessage('Please input password.')
        elif self.auth.authenticate_user(username, password):
            self.ui = FrontZaur(username, self.datazaur)
            self.ui.show()
            self.close()
        else:
            error_dialog.showMessage('Wrong username or password. Try again.')

    # opens account creator
    def new_account(self):
        self.resize(333, 427)
        self.acc = AccountCreator(self)
        self.acc.show()
        self.groupBox.setVisible(False)


    # binding return key to login
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.login()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Login"))
        self.groupBox.setTitle(_translate("Form", " Datazaur"))
        self.label.setText(_translate("Form", "login"))
        self.label_2.setText(_translate("Form", "password"))
        self.pushButton_33.setText(_translate("Form", "log in"))
        self.pushButton_34.setText(_translate("Form", "new account"))
        self.pushButton_35.setText(_translate("Form", "exit"))

