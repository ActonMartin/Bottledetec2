# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Bottledetec2\ui/port_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1091, 765)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 9, 861, 331))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cam1_ok = QtWidgets.QPushButton(self.frame)
        self.cam1_ok.setObjectName("cam1_ok")
        self.horizontalLayout.addWidget(self.cam1_ok)
        self.cam2_ok = QtWidgets.QPushButton(self.frame)
        self.cam2_ok.setObjectName("cam2_ok")
        self.horizontalLayout.addWidget(self.cam2_ok)
        self.cam3_ok = QtWidgets.QPushButton(self.frame)
        self.cam3_ok.setObjectName("cam3_ok")
        self.horizontalLayout.addWidget(self.cam3_ok)
        self.cam4_ok = QtWidgets.QPushButton(self.frame)
        self.cam4_ok.setObjectName("cam4_ok")
        self.horizontalLayout.addWidget(self.cam4_ok)
        self.cam5_ok = QtWidgets.QPushButton(self.frame)
        self.cam5_ok.setObjectName("cam5_ok")
        self.horizontalLayout.addWidget(self.cam5_ok)
        self.cam6_ok = QtWidgets.QPushButton(self.frame)
        self.cam6_ok.setObjectName("cam6_ok")
        self.horizontalLayout.addWidget(self.cam6_ok)
        self.cam1_4 = QtWidgets.QPushButton(self.frame)
        self.cam1_4.setObjectName("cam1_4")
        self.horizontalLayout.addWidget(self.cam1_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.connect_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.connect_pushButton.setGeometry(QtCore.QRect(740, 360, 121, 61))
        self.connect_pushButton.setObjectName("connect_pushButton")
        self.comboBox_ports = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_ports.setGeometry(QtCore.QRect(530, 360, 181, 61))
        self.comboBox_ports.setObjectName("comboBox_ports")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cam1_ok.setText(_translate("MainWindow", "cam1"))
        self.cam2_ok.setText(_translate("MainWindow", "cam2"))
        self.cam3_ok.setText(_translate("MainWindow", "cam3"))
        self.cam4_ok.setText(_translate("MainWindow", "cam4"))
        self.cam5_ok.setText(_translate("MainWindow", "cam5"))
        self.cam6_ok.setText(_translate("MainWindow", "cam6"))
        self.cam1_4.setText(_translate("MainWindow", "cam1_4"))
        self.connect_pushButton.setText(_translate("MainWindow", "连接串口"))
