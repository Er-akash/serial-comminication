import sys
import glob
import serial
import threading
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import QThread
import time
import datetime
global source_path
global serial_data
global ser
global serial_data_buffer
serial_data_buffer='\0'
s ='\0'
ser=0
import KalpSetup
##from welcome import Ui_MainWindow

ports = glob.glob('/dev/tty[A-Za-z]*')
##print(ports)

class Setup(QtGui.QMainWindow, KalpSetup.Ui_MainWindow):
        @pyqtSlot() 
        def __init__(self):
                super(self.__class__,self).__init__()
                self.setupUi(self)
##                self.pushButton_10.clicked.connect(self.about)
##                result=self.serial_ports()
##                print(result)
                ports = glob.glob('/dev/tty[A-Za-z]*')
                result=[]
                global s
                for port in ports:
                        try:
                                ser=serial.Serial(port, baudrate=9600, bytesize=8, parity='N', stopbits=1,timeout=0.009,xonxoff=0)
                                result.append(port)
                                ser.write(bytes(4)) 
                        except (OSError, serial.SerialException):
                               pass
                print(result)
                           

                self.Name.addItems(result)
                self.Name.setCurrentIndex(0)
                
                        
                list = ["4800", "9600", "14400", "19200","38400","56000","57600","115200"]
                self.Baud.addItems(list)
                self.Baud.setCurrentIndex(1)
                list1 = ["7","8"]
                self.Data_Size.addItems(list1)
                self.Data_Size.setCurrentIndex(0)
                list2 = ["none","even","odd","mark"]
                self.Parity.addItems(list2)
                self.Parity.setCurrentIndex(1)
                list3 = ["OFF","RTS/CTS","Xon/Xoff"]
                self.Handshake.addItems(list3)
                self.Handshake.setCurrentIndex(0)
                list4 = ["Free","PortStore test","Data","Setup"]
                self.Mode.addItems(list4)
                self.Mode.setCurrentIndex(0)

                self.Open_3.clicked.connect(self.open)
                self.pushButton_11.clicked.connect(self.browse)
##                text= print("com port is open")
##                self.textEdit.append(str(text))
                self.pushButton.clicked.connect(self.data_send)



        def open(self):
                global ser
                button_status=self.Open_3.text()
                print(button_status)
                self.textEdit.setFocus()
                
                compo = self.Name.currentIndex()
                compo=int(compo)
##                compo = self.Name.currentText()
##                print("compo",compo)
                if(button_status=='Open'):
                        try:
                                text= "serial port "+self.Name.currentText()+ " is opened \n"
                                self.textEdit.append(str(text))
                                print("text",text)
                                ser = serial.Serial(ports[compo])
                                self.Open_3.setText("close")
                               
                                self.Name.setEnabled(False)
                                self.Baud.setEnabled(False)
                                self.Data_Size.setEnabled(False)
                                self.Parity.setEnabled(False)
                                self.Handshake.setEnabled(False)
                                self.Mode.setEnabled(False)
                                try:
                                    thread= threading.Thread(target =self.serial_receive)
                                    thread.start()
                                except:
                                    print("Caught an exception")
                                    time.sleep(0.1)
                                    try:
                                        thread= threading.Thread(target =self.serial_receive, args = ())
                                        thread.start()
                                    except:
                                        print("Caught an exception-1")
                                        time.sleep(0.1)
                        except (OSError, serial.SerialException):
                                pass

                else:
                    try:
                        #ser= serial.Serial(ports[compo])
                        ser.close()
                        self.Open_3.setText("Open") 
                        text1= "serial port "+self.Name.currentText()+ " is closed \n"
                        self.textEdit.append(str(text1))
                    except (OSError, serial.SerialException):
                        pass
                    
                    self.Name.setEnabled(True)
                    self.Baud.setEnabled(True)
                    self.Data_Size.setEnabled(True)
                    self.Parity.setEnabled(True)
                    self.Handshake.setEnabled(True)
                    self.Mode.setEnabled(True)
                       
        def serial_receive(self):
                global serial_data
                global serial_data_buffer
                global ser
                compo = self.Name.currentText()
                print("compo",compo)
                brate = self.Baud.currentText()
##                brate=int(brate)
                print("baudrate",brate)
                parit = self.Parity.currentText()
                print("Parity",parit)
                if (parit=="none"):
                        parity=serial.PARITY_NONE
                elif (parit=="even"):
                        parity=serial.PARITY_EVEN
                elif (parit=="odd"):
                        parity=serial.PARITY_ODD
                elif (parit=="mark"):
                        parity=serial.PARITY_MARK
                dataSize = self.Data_Size.currentText()
                dataSize=int(dataSize)
                print("Size",dataSize)
                try:
                        ser=serial.Serial(compo, baudrate=brate, bytesize=dataSize, parity=parity, stopbits=1,timeout=0.1,xonxoff=0)
                        while True:
        ##                        ser.write(b'hell')
                                serial_data=ser.read()
                                print(serial_data)
                                print(type(serial_data))
                               
                                try:
                                        
                                         y=serial_data.decode("utf-8")
                                         print(type(y))
                                         if len(serial_data)>0:
                                                 print("akash",y)
                                                 self.textEdit.insertPlainText(str(y))
                                except:
                                        print("Settings Do not Matched")
                except:
                        print("Settings Do not Matched")
                
        def data_send(self):
                global ser
                compo = self.Name.currentText()
                print("compo",compo)
                brate = self.Baud.currentText()
##                brate=int(brate)
                print("baudrate",brate)
                parit = self.Parity.currentText()
                print("Parity",parit)
                if (parit=="none"):
                        parity=serial.PARITY_NONE
                elif (parit=="even"):
                        parity=serial.PARITY_EVEN
                elif (parit=="odd"):
                        parity=serial.PARITY_ODD
                elif (parit=="mark"):
                        parity=serial.PARITY_MARK
                dataSize = self.Data_Size.currentText()
                dataSize=int(dataSize)
                print("Size",dataSize)
                
                ser=serial.Serial(compo, baudrate=brate, bytesize=dataSize, parity=parity, stopbits=1,timeout=0.1,xonxoff=0)

                input_data=self.lineEdit_2.text()     
                input_data=str(input_data)
                print(type(input_data))
                self.z=input_data.encode("utf-8")
                print("print",self.z.hex())
                print(self.checkBox.isChecked())
                if (self.checkBox.isChecked()==True):
                        self.z.hex()
                        convert=self.z.hex().encode('utf-8')
                        ser.write(convert)
                else:
                        ser.write(self.z)
                print("send")
                print(self.z)

                

                

        def browse(self):
                global ser
                global source_path
                source_path='\0'
                file_ext='*'
                file_ext+=self.comboBox.currentText()
                self.setdatentime()
                try:
                    fname = QFileDialog.getOpenFileName(self, 'Open file', '/home/pi/Desktop/Akash/Main_page/files', str(file_ext))
                    source_path=fname
                    source_path = str(source_path)

                    f = open(fname, 'rb')
                    data = f.read()
                    data_read=data.decode("utf-8")
                    self.textEdit.setPlainText(str(data_read))
                    a=data_read.encode("utf-8")
                    print(type(a))
                    ser.write(a)
                    print("value",a)
                    self.textEdit_2.setText(fname)
                    
                except IOError:
                    print('data=0')
                    data=0
        def setdatentime(self):
                x=datetime.datetime.now()
                print(x)
                file1 = open("/home/pi/Desktop/Akash/Main_page/files/time.txt","r+")
                file1.write(str(x))
                file1.close()
                
##        def about(self):
####                print("hello")
##                self.welcomeWindowShow()
##
##        def welcomeWindowShow(self):
##                self.welcomeWindow = QtGui.QMainWindow()
##                self.ui = Ui_MainWindow()
##                self.ui.setupUi(self.welcomeWindow)
##                self.welcomeWindow.show()

##if __name__ == "__main__":
##        app = QtGui.QApplication(sys.argv)
##        window = Setup()
##        window.show()
##        sys.exit(app.exec_())

