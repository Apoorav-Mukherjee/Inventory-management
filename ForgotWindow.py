from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect,QLineEdit,QMessageBox
from PyQt5.QtGui import QPixmap,QIcon
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(266, 284)
        Form.setMinimumSize(QtCore.QSize(266, 284))
        Form.setMaximumSize(QtCore.QSize(266, 284))
        
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        Form.setFont(font)
        self.Background = QtWidgets.QLabel(Form)
        self.Background.setGeometry(QtCore.QRect(0, 0, 261, 281))
        self.Background.setText("")
        self.Background.setScaledContents(True)
        self.Background.setPixmap(QPixmap("TextureBackground.jpg"))

        self.Background.setObjectName("Background")
        self.ForgotCard = QtWidgets.QWidget(Form)
        self.ForgotCard.setGeometry(QtCore.QRect(50, 30, 171, 201))
        self.ForgotCard.setStyleSheet("QWidget {\n"
        "        background:white;\n"
        "        border-radius:15px;\n"
        "}")

        # Add Shadow Effect to Login Page Card
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(QtGui.QColor(0, 0, 0, 180))  # Black semi-transparent shadow
        self.ForgotCard.setGraphicsEffect(shadow)

        self.ForgotCard.setObjectName("ForgotCard")
        self.UpdateLabel = QtWidgets.QLabel(self.ForgotCard)
        self.UpdateLabel.setGeometry(QtCore.QRect(0, 10, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Cascadia Mono")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.UpdateLabel.setFont(font)
        self.UpdateLabel.setObjectName("UpdateLabel")
        self.UsernameInput = QtWidgets.QLineEdit(self.ForgotCard)
        self.UsernameInput.setGeometry(QtCore.QRect(30, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        self.UsernameInput.setFont(font)
        self.UsernameInput.setStyleSheet("QLineEdit {\n"
        "        border: 2px solid grey;\n"
        "        border-radius: 5px;\n"
        "}")
        self.UsernameInput.setText("")
        self.UsernameInput.setObjectName("UsernameInput")
        self.PasswordInput = QtWidgets.QLineEdit(self.ForgotCard)
        self.PasswordInput.setGeometry(QtCore.QRect(30, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code Light")
        self.PasswordInput.setFont(font)
        self.PasswordInput.setStyleSheet("QLineEdit {\n"
        "        border: 2px solid grey;\n"
        "        border-radius: 5px;\n"
        "}")
        self.PasswordInput.setText("")
        self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordInput.setObjectName("PasswordInput")
        self.SubmitBtn = QtWidgets.QPushButton(self.ForgotCard)
        self.SubmitBtn.setGeometry(QtCore.QRect(50, 150, 81, 31))
        self.SubmitBtn.clicked.connect(self.UpdatePass)

        font = QtGui.QFont()
        font.setFamily("Cascadia Mono SemiBold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.SubmitBtn.setFont(font)
        self.SubmitBtn.setStyleSheet("QPushButton {\n"
        "        border-radius:10px;\n"
        "        background:#ff6e63;\n"
        "        color:white;\n"
        "}\n"
        "QPushButton:hover{\n"
        "        background:#fa4739;\n"
        "}")
        self.SubmitBtn.setObjectName("SubmitBtn")
        
        self.PasswordEye = QtWidgets.QPushButton(self.ForgotCard)
        self.PasswordEye.setGeometry(QtCore.QRect(130, 110, 15, 15))
        self.PasswordEye.setStyleSheet("QPushButton {\n"
        "        border:none;\n"
        "}")
        self.PasswordEye.setText("")
        self.PasswordEye.setCheckable(True)
        self.PasswordEye.setObjectName("PasswordEye")
        self.PasswordEye.setIcon(QIcon("eye.png"))
        self.PasswordEye.clicked.connect(self.toggle_password_visibility)

        

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def toggle_password_visibility(self):
        if self.PasswordEye.isChecked():
            self.PasswordEye.setIcon(QIcon("open-eye.png"))
            self.PasswordInput.setEchoMode(QLineEdit.Normal)
        else:
            self.PasswordEye.setIcon(QIcon("eye.png"))
            self.PasswordInput.setEchoMode(QLineEdit.Password)
        

    def UpdatePass(self):
        username = self.UsernameInput.text()
        if not username:
            QMessageBox.warning(self.ForgotCard,"Error","All Fields Are Required Please Enter a Valid Username!")
            return
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?",(username,))
        user = cursor.fetchone()
        conn.close()

        if (user is not None):
            QMessageBox.critical(self.ForgotCard,"Error",f"User not found with username {username}")
            return
        password = self.PasswordInput.text()

        if not password:
            QMessageBox.warning(self.ForgotCard,"Error","All Fields Are Required Please Enter a Valid Password!")
            return
        
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET password = ? WHERE username = ?",(password,username))
        conn.commit()
        conn.close() 
        QMessageBox.information(self.ForgotCard,"Success","Successfully changed password!")
        


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Update Password"))
        self.UpdateLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Update Your Password</span></p></body></html>"))
        self.UsernameInput.setPlaceholderText(_translate("Form", "Username"))
        self.PasswordInput.setPlaceholderText(_translate("Form", "New Password"))
        self.SubmitBtn.setText(_translate("Form", "Submit"))
        self.SubmitBtn.setShortcut(_translate("Form", "Return"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
