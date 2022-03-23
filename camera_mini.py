# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'camera_mini.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(520, 1080)
        mainWindow.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.para_list = QtWidgets.QFrame(self.centralwidget)
        self.para_list.setGeometry(QtCore.QRect(10, 10, 291, 211))
        self.para_list.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border:2px solid black;")
        self.para_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.para_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.para_list.setObjectName("para_list")
        self.label_3 = QtWidgets.QLabel(self.para_list)
        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.xy_text = QtWidgets.QTextBrowser(self.para_list)
        self.xy_text.setGeometry(QtCore.QRect(20, 80, 181, 41))
        self.xy_text.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"font: 13pt \"宋体\";")
        self.xy_text.setObjectName("xy_text")
        self.lineEdit = QtWidgets.QLineEdit(self.para_list)
        self.lineEdit.setGeometry(QtCore.QRect(210, 100, 31, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 14pt \"Times New Roman\";\n"
"border:1px solid white;")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.para_list)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 81, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 14pt \"宋体\";\n"
"border:1px solid white;")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.para_list)
        self.label_6.setGeometry(QtCore.QRect(10, 140, 71, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"font: 14pt \"宋体\";\n"
"border:1px solid white;")
        self.label_6.setObjectName("label_6")
        self.warning_inf = QtWidgets.QTextBrowser(self.para_list)
        self.warning_inf.setGeometry(QtCore.QRect(90, 130, 181, 51))
        self.warning_inf.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border:1px solid white;\n"
"font: 13pt \"宋体\";\n"
"")
        self.warning_inf.setObjectName("warning_inf")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 260, 501, 721))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.pyplot = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.pyplot.setContentsMargins(0, 0, 0, 0)
        self.pyplot.setObjectName("pyplot")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 240, 71, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.para_list_2 = QtWidgets.QFrame(self.centralwidget)
        self.para_list_2.setGeometry(QtCore.QRect(310, 10, 201, 211))
        self.para_list_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"")
        self.para_list_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.para_list_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.para_list_2.setObjectName("para_list_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.para_list_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-30, 30, 231, 211))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.pyplot_rudder = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.pyplot_rudder.setContentsMargins(0, 0, 0, 0)
        self.pyplot_rudder.setObjectName("pyplot_rudder")
        self.label_7 = QtWidgets.QLabel(self.para_list_2)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 201, 31))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border:2px solid black;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 26))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "清淤机器人路线模拟及航向显示"))
        self.label_3.setText(_translate("mainWindow", "当前坐标及运行状态"))
        self.lineEdit.setText(_translate("mainWindow", "m"))
        self.label_5.setText(_translate("mainWindow", "(x,y)："))
        self.label_6.setText(_translate("mainWindow", "状态："))
        self.label_4.setText(_translate("mainWindow", "斜坡侧"))
        self.label_7.setText(_translate("mainWindow", "航向"))

