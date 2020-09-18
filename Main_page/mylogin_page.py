import sys
import my_login
from PyQt4 import QtCore, QtGui
import global_var
import global_test_var as GV


class login_page(QtGui.QMainWindow, my_login.Ui_MainWindow): 
        def __init__(self):
                super(self.__class__,self).__init__()
                self.setupUi(self)
                self.pushButton.clicked.connect(self.Login_btn)


        def Login_btn(self,event):
                username = str(self.uid_lineEdit.text())
                self.pw_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
                password=self.pw_lineEdit.text()
                if(username=="Kalptech" and password=="7"):
                        print("Valid User")
                        global_var.state_machine=2
                        global_var.state_machine_flag=1
                        
                else:
                        print("Invalid User")
                self.uid_lineEdit.clear()
                self.pw_lineEdit.clear()

                

##def main():
##    app = QtGui.QApplication(sys.argv)
##    window = login_page()
##    window.show()
##    app.exec_()
##
##if __name__ == '__main__':
##    main()
##
##    
