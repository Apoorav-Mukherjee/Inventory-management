from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from database import register_user

class Ui_MainWindow_SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(718, 545)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BackgroundWidget = QtWidgets.QWidget(self.centralwidget)
        self.BackgroundWidget.setGeometry(QtCore.QRect(0, 0, 711, 561))
        self.BackgroundWidget.setObjectName("BackgroundWidget")
        self.BackgroundWidget.setStyleSheet("""
                        QWidget {
                                background: rgb(182, 204, 240);
                                            }
        """)
        
        self.SignUpWidget = QtWidgets.QWidget(self.centralwidget)
        self.SignUpWidget.setGeometry(QtCore.QRect(210, 70, 281, 361))
        self.SignUpWidget.setObjectName("SignUpWidget")
        self.SignUpWidget.setStyleSheet("""
                    QWidget {
                                background:white; 
                                border-radius:15px;
                                        }
        """)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0, 180))  # Black semi-transparent shadow
        self.SignUpWidget.setGraphicsEffect(shadow)

        self.SignUpLabel = QtWidgets.QLabel(self.SignUpWidget)
        self.SignUpLabel.setGeometry(QtCore.QRect(108, 40, 85, 35))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.SignUpLabel.setFont(font)
        self.SignUpLabel.setObjectName("SignUpLabel")
        self.UsernameInput = QtWidgets.QLineEdit(self.SignUpWidget)
        self.UsernameInput.setGeometry(QtCore.QRect(60, 80, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(10)
        self.UsernameInput.setFont(font)
        self.UsernameInput.setObjectName("UsernameInput")
        self.EmailInput = QtWidgets.QLineEdit(self.SignUpWidget)
        self.EmailInput.setGeometry(QtCore.QRect(60, 115, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(10)
        self.EmailInput.setFont(font)
        self.EmailInput.setObjectName("EmailInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.SignUpWidget)
        self.PasswordInput.setGeometry(QtCore.QRect(60, 150, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(10)
        self.PasswordInput.setFont(font)
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.PasswordInput.setObjectName("PasswordInput")
        self.CheckPass = QtWidgets.QLineEdit(self.SignUpWidget)
        self.CheckPass.setGeometry(QtCore.QRect(60, 185, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(10)
        self.CheckPass.setFont(font)
        self.CheckPass.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.CheckPass.setObjectName("CheckPass")
        self.AgreeCheckBox = QtWidgets.QCheckBox(self.SignUpWidget)
        self.AgreeCheckBox.setEnabled(True)
        self.AgreeCheckBox.setGeometry(QtCore.QRect(70, 240, 171, 31))
        self.AgreeCheckBox.setAcceptDrops(False)
        self.AgreeCheckBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.AgreeCheckBox.setChecked(False)
        self.AgreeCheckBox.setTristate(False)
        self.AgreeCheckBox.setObjectName("AgreeCheckBox")
        self.SignUpBtn = QtWidgets.QPushButton(self.SignUpWidget)
        self.SignUpBtn.setGeometry(QtCore.QRect(44, 280, 201, 35))
        self.SignUpBtn.setObjectName("SignUpBtn")
        self.SignUpBtn.clicked.connect(self.signup)

        self.SignUpBtn.setStyleSheet("""
               QPushButton {
                background-color: #73a4f5;
                color: white;
                font-weight:bold;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkblue;
            }
        """)

        self.AlreadyAccLabel = QtWidgets.QLabel(self.SignUpWidget)
        self.AlreadyAccLabel.setGeometry(QtCore.QRect(60, 320, 171, 16))
        self.AlreadyAccLabel.setObjectName("AlreadyAccLabel")

        InputBoxes = [self.UsernameInput,self.EmailInput,self.PasswordInput,self.CheckPass]

        for field in InputBoxes:
            field.setStyleSheet("""
                               QLineEdit {
                            border: 2px solid gray;
                            border-radius: 10px;
                            padding: 5px;
            }
            """)        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.SignUpLabel.setText(_translate("MainWindow", "SignUp"))
        self.UsernameInput.setPlaceholderText(_translate("MainWindow", "Username"))
        self.EmailInput.setPlaceholderText(_translate("MainWindow", "Email"))
        self.PasswordInput.setPlaceholderText(_translate("MainWindow", "Password"))
        self.CheckPass.setPlaceholderText(_translate("MainWindow", "Re-enter Password "))
        self.AgreeCheckBox.setText(_translate("MainWindow", "By Checking this you agree\n"
"to our Agrrements and policies"))
        self.SignUpBtn.setText(_translate("MainWindow", "Sign Up"))
        self.AlreadyAccLabel.setText(_translate("MainWindow", "Already Have an Account ? Sign in"))

    def signup(self):
        username = self.UsernameInput.text()
        email = self.EmailInput.text()
        password = self.PasswordInput.text()
        confirm_pass = self.CheckPass.text()

        if password != confirm_pass:
            QtWidgets.QMessageBox.warning(None, "Error", "Passwords do not match!")
            return

        if register_user(username, email, password):
            QtWidgets.QMessageBox.information(None, "Success", "Account Created Successfully!")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Username or Email already exists!")

def Main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_SignUp()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    Main()
    
