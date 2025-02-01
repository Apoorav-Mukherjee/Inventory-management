from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect
from database import register_user

class Ui_MainWindow_SignUp(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500,500)
        MainWindow.setWindowTitle("SignUp Page")
        MainWindow.setMinimumSize(500,500)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.BackgroundWidget = QtWidgets.QWidget(self.centralwidget)
        self.BackgroundWidget.setGeometry(QtCore.QRect(0, 0, 719, 561))
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
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        
        # Eye button (for password visibility toggle)
        self.showPassBtn = QtWidgets.QPushButton(self.SignUpWidget)
        self.showPassBtn.setGeometry(QtCore.QRect(215, 155, 20, 20))
        self.showPassBtn.setObjectName("showPassBtn")
        self.showPassBtn.setCheckable(True)  # Button toggles on/off
        self.showPassBtn.setIcon(QtGui.QIcon("eye.png"))  # Set initial icon (closed eye)
        self.showPassBtn.setIconSize(QtCore.QSize(20, 20))  # Set icon size to 20x20
        self.showPassBtn.setStyleSheet("""
                                       QPushButton{
                                       border: none;
                                       }
                                        """)  # No border for cleaner UI
        self.showPassBtn.clicked.connect(self.toggle_password_visibility)

        
        self.CheckPass = QtWidgets.QLineEdit(self.SignUpWidget)
        self.CheckPass.setGeometry(QtCore.QRect(60, 185, 181, 30))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        font.setPointSize(10)
        self.CheckPass.setFont(font)
        self.CheckPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.CheckPass.setObjectName("CheckPass")

        self.showCheckPassBtn = QtWidgets.QPushButton(self.SignUpWidget)
        self.showCheckPassBtn.setGeometry(QtCore.QRect(215, 190, 20, 20))
        self.showCheckPassBtn.setObjectName("showCheckPassBtn")
        self.showCheckPassBtn.setCheckable(True)  # Button toggles on/off
        self.showCheckPassBtn.setIcon(QtGui.QIcon("eye.png"))  # Set initial icon (closed eye)
        self.showCheckPassBtn.setIconSize(QtCore.QSize(20, 20))  # Set icon size to 20x20
        self.showCheckPassBtn.setStyleSheet("""
                                       QPushButton{
                                       border: none;
                                       }
                                        """)  # No border for cleaner UI
        self.showCheckPassBtn.clicked.connect(self.CheckPassVisibilityToggle)

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

        self.AlreadyAccBtn = QtWidgets.QPushButton(self.SignUpWidget)
        self.AlreadyAccBtn.setGeometry(QtCore.QRect(60, 320, 171, 16))
        self.AlreadyAccBtn.setObjectName("AlreadyAccBtn")

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

        self.center_login_card()  # Centers it when the app starts
        MainWindow.resizeEvent = self.resizeEvent  # Attach resize event

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
        self.AlreadyAccBtn.setText(_translate("MainWindow", "Already Have an Account ? Sign in"))

    def center_login_card(self):
            """ Dynamically centers the login card when the window resizes """
            window_width = self.centralwidget.width()
            window_height = self.centralwidget.height()

            card_width = self.SignUpWidget.width()
            card_height = self.SignUpWidget.height()

            # Calculate the new position to keep it centered
            new_x = (window_width - card_width) // 2
            new_y = (window_height - card_height) // 2

            self.SignUpWidget.setGeometry(new_x, new_y, card_width, card_height)

    def resize_background(self):
        """Dynamically resizes the background"""
        window_width = self.centralwidget.width()
        window_height = self.centralwidget.height()

        self.BackgroundWidget.setGeometry(0,0,window_width,window_height)


    def resizeEvent(self, event):
            """ Calls the center_login_card() whenever the window resizes """
            self.center_login_card()
            self.resize_background()
            event.accept()

    def CheckPassVisibilityToggle(self):
        """Toggle the password visibility when the eye button is clicked"""
        if self.showCheckPassBtn.isChecked():
            self.CheckPass.setEchoMode(QtWidgets.QLineEdit.Normal)  # Show password
            self.showCheckPassBtn.setIcon(QtGui.QIcon("open-eye.png"))  # Change to open eye icon
        else:
            self.CheckPass.setEchoMode(QtWidgets.QLineEdit.Password)  # Hide password
            self.showCheckPassBtn.setIcon(QtGui.QIcon("eye.png"))  # Change back to closed eye icon

    
    def toggle_password_visibility(self):
        """Toggle the password visibility when the eye button is clicked"""
        if self.showPassBtn.isChecked():
            self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)  # Show password
            self.showPassBtn.setIcon(QtGui.QIcon("open-eye.png"))  # Change to open eye icon
        else:
            self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)  # Hide password
            self.showPassBtn.setIcon(QtGui.QIcon("eye.png"))  # Change back to closed eye icon

    def signup(self):
        username = self.UsernameInput.text()
        email = self.EmailInput.text()
        password = self.PasswordInput.text()
        confirm_pass = self.CheckPass.text()

        if not self.AgreeCheckBox.isChecked():
            QtWidgets.QMessageBox.warning(None,"Not Agreed","Please Check The Agree Box to Continue")
            return

        if password != confirm_pass:
            QtWidgets.QMessageBox.warning(None, "Error", "Passwords do not match!")
            return

        if register_user(username, email, password):
            QtWidgets.QMessageBox.information(None, "Success", "Account Created Successfully!")
        else:
            QtWidgets.QMessageBox.warning(None, "Error", "Username or Email already exists!")


if __name__ == "__main__":
    def Main():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow_SignUp()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    Main()