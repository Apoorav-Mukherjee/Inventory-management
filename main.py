from Login import Ui_MainWindow_Login
from SignUp import Ui_MainWindow_SignUp
from PyQt5 import QtWidgets
import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow_Login()
        self.ui.setupUi(self)

        self.ui.CreateAccBtn.clicked.connect(self.open_signup_window)
    
    def open_signup_window(self):
        """Hide login and open signup window"""
        self.signup_window = QtWidgets.QMainWindow()  # Create a new window
        self.signup_ui = Ui_MainWindow_SignUp()
        self.signup_ui.setupUi(self.signup_window)
        self.signup_ui.AlreadyAccBtn.clicked.connect(self.open_login_window)

        self.hide()  # Hide the login window
        self.signup_window.show()  # Show the signup window
    
    def open_login_window(self):
        self.login_window = QtWidgets.QMainWindow()
        self.login_ui = Ui_MainWindow_Login()
        self.login_ui.setupUi(self.login_window)

        self.login_ui.CreateAccBtn.clicked.connect(self.open_signup_window)

        self.signup_window.hide()
        self.show()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec_())
