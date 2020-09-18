# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my_login.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1440, 800)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(238, 238, 238);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(246, 216, 171, 41))
        self.label_9.setStyleSheet(_fromUtf8("font: 25 28pt \"Roboto [GOOG]\";"))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 274, 381, 21))
        self.label_4.setStyleSheet(_fromUtf8("font: 25 14pt \"Roboto [GOOG]\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.uid_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.uid_lineEdit.setGeometry(QtCore.QRect(300, 351, 221, 21))
        self.uid_lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.uid_lineEdit.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 12pt \"Roboto [GOOG]\";\n"
"background-color: rgbA(255, 255, 255,0);\n"
""))
        self.uid_lineEdit.setObjectName(_fromUtf8("uid_lineEdit"))
        self.pw_lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.pw_lineEdit.setGeometry(QtCore.QRect(300, 411, 221, 21))
        self.pw_lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pw_lineEdit.setStyleSheet(_fromUtf8("border-radius: 1px;\n"
"font: 12pt \"Roboto [GOOG]\";\n"
"background-color: rgbA(255, 255, 255,0);"))
        self.pw_lineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.pw_lineEdit.setObjectName(_fromUtf8("pw_lineEdit"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 344, 32, 32))
        self.label_2.setStyleSheet(_fromUtf8("background-image:url(/home/pi/Desktop/Akash/Main_page/logos/uid.png);"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../../../AWHT/UI_files/final_assets/uid.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 404, 32, 32))
        self.label.setStyleSheet(_fromUtf8("background-image:url(/home/pi/Desktop/Akash/Main_page/logos/pw.png);"))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("../../../AWHT/UI_files/final_assets/pw.png")))
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(250, 377, 361, 16))
        self.line.setSizeIncrement(QtCore.QSize(0, 0))
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(250, 437, 361, 16))
        self.line_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.line_2.setFrameShadow(QtGui.QFrame.Plain)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(248, 484, 164, 60))
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(_fromUtf8("background-image:url(/home/pi/Desktop/Akash/Main_page/logos/btn_normal.png);\n"
"font: 18pt \"Roboto [GOOG]\";\n"
"color: rgb(255, 255, 255);"))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_9.setText(_translate("MainWindow", "Welcome,", None))
        self.label_4.setText(_translate("MainWindow", "Please enter your ID & Password to Continue", None))
        self.uid_lineEdit.setPlaceholderText(_translate("MainWindow", "Username", None))
        self.pw_lineEdit.setPlaceholderText(_translate("MainWindow", "Password", None))
        self.pushButton.setText(_translate("MainWindow", "Login", None))

