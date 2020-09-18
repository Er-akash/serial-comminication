import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QThread
import time
import threading
from PyQt4.QtCore import QThread
from global_files import*
from  message_fun import *
import global_var
import global_test_var as GV
import serial
import my_main
import KalpSetupmain
import mylogin_page

##import threading
##try:
##    thread1 = threading.Thread(target = recieve_msg, args = ())
##    thread1.start()
##    
##except:
##    print("Caught an exception")
##    time.sleep(0.1)
##    try:
##        thread1 = threading.Thread(target = recieve_msg, args = ())
##        thread1.start()
##    except:
##        print("Caught an exception-1")
##        time.sleep(0.1)


class Ui_MainWindow(QtGui.QMainWindow, my_main.Ui_MainWindow): 
        def __init__(self,p1,p2):
                super(Ui_MainWindow,self).__init__()
                self.setupUi(self)
                self.p1=p1
                self.p2=p2
                self.label_6.mousePressEvent=self.home_page
                self.label_5.mousePressEvent=self.shutdwn_system
        def home_page(self,event):
                self.test.setWidget(self.p1)
                print("login page")
                self.label_4.setText("Login Page")
        def shutdwn_system(self,event):
                os.system("sudo shutdown -h now")



        @pyqtSlot() 
        def date_time_update(self):
                currentDate=datetime.now()
                ##        print(currentDate)
                Hrs_Min=currentDate.strftime("%H:%M")
                self.label_2.setText(Hrs_Min)
                mon_yr=currentDate.strftime("%d %B %Y") #%B to get December  %b-Dec
                self.label_3.setText(mon_yr)
                day=currentDate.strftime("%A")
                self.label.setText(day)

                GV.HMS=currentDate.strftime("%H:%M:%S")
                GV.hrs=currentDate.strftime("%H")
                GV.mint=currentDate.strftime("%M")
                GV.sec=currentDate.strftime("%S")
                GV.DMY=currentDate.strftime("%d/%m/%Y")
                GV.date=currentDate.strftime("%d")
                GV.mon=currentDate.strftime("%m")
                GV.year=currentDate.strftime("%Y")
                GV.week_no=currentDate.strftime("%W")
                GV.week_day=currentDate.strftime("%w")

                if(global_var.state_machine_flag==1):
                        global_var.state_machine_flag=0
                        if(global_var.state_machine==1):
                                self.test.setWidget(self.p1)
                        elif(global_var.state_machine==2):
                                self.test.setWidget(self.p2)
                                self.label_4.setText("Serial Dashboard")
                                                    
                                        
                
                        
                

def main():
        app = QtGui.QApplication(sys.argv)
        
        p1 = mylogin_page.login_page()
        p2 = KalpSetupmain.Setup()
       
        GUI = Ui_MainWindow(p1,p2)
        GUI.test.setWidget(p1)
        GUI.show()

        timer = QTimer()
        GUI.connect(timer,SIGNAL("timeout()"),GUI,SLOT("date_time_update()"))
        timer.start(100)

        app.exec_()



if __name__ == "__main__":
    main()
