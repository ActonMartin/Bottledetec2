# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Projects\Bottledetec2\ui/MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1190, 796)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label_time = QtWidgets.QLabel(self.centralwidget)
        self.label_time.setMinimumSize(QtCore.QSize(0, 50))
        self.label_time.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_time.setFont(font)
        self.label_time.setText("")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout_3.addWidget(self.label_time)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label1_camera = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label1_camera.setFont(font)
        self.label1_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label1_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label1_camera.setObjectName("label1_camera")
        self.horizontalLayout_8.addWidget(self.label1_camera)
        self.horizontalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")

        self.label2_camera = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label2_camera.setFont(font)
        self.label2_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label2_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label2_camera.setObjectName("label2_camera")
        self.horizontalLayout_9.addWidget(self.label2_camera)
        self.horizontalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label3_camera = QtWidgets.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label3_camera.setFont(font)
        self.label3_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label3_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label3_camera.setObjectName("label3_camera")
        self.horizontalLayout_10.addWidget(self.label3_camera)
        self.horizontalLayout_4.addWidget(self.groupBox_3)
        self.groupBox_0 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_0.setStyleSheet("QGroupBox#groupBox_0 { border: 1px solid black;}")
        self.groupBox_0.setObjectName("groupBox_0")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.groupBox_0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_sctatch_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_sctatch_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_sctatch_.setFont(font)
        self.label_sctatch_.setObjectName("label_sctatch_")
        self.horizontalLayout.addWidget(self.label_sctatch_)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sctatch_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.sctatch_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sctatch_progressBar.setFont(font)
        self.sctatch_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.sctatch_progressBar.setProperty("value", 0)
        self.sctatch_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.sctatch_progressBar.setInvertedAppearance(False)
        self.sctatch_progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.sctatch_progressBar.setObjectName("sctatch_progressBar")
        self.horizontalLayout.addWidget(self.sctatch_progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 4)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_blackpoint_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_blackpoint_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_blackpoint_.setFont(font)
        self.label_blackpoint_.setObjectName("label_blackpoint_")
        self.horizontalLayout_2.addWidget(self.label_blackpoint_)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.blackpoint_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.blackpoint_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.blackpoint_progressBar.setFont(font)
        self.blackpoint_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.blackpoint_progressBar.setProperty("value", 0)
        self.blackpoint_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.blackpoint_progressBar.setObjectName("blackpoint_progressBar")
        self.horizontalLayout_2.addWidget(self.blackpoint_progressBar)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 4)
        self.horizontalLayout_2.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_nodefine0_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_nodefine0_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_nodefine0_.setFont(font)
        self.label_nodefine0_.setObjectName("label_nodefine0_")
        self.horizontalLayout_3.addWidget(self.label_nodefine0_)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.nodefine0_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.nodefine0_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nodefine0_progressBar.setFont(font)
        self.nodefine0_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.nodefine0_progressBar.setProperty("value", 0)
        self.nodefine0_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.nodefine0_progressBar.setObjectName("nodefine0_progressBar")
        self.horizontalLayout_3.addWidget(self.nodefine0_progressBar)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 4)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_nodefine1_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_nodefine1_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_nodefine1_.setFont(font)
        self.label_nodefine1_.setObjectName("label_nodefine1_")
        self.horizontalLayout_6.addWidget(self.label_nodefine1_)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.nodefine1_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.nodefine1_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nodefine1_progressBar.setFont(font)
        self.nodefine1_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.nodefine1_progressBar.setProperty("value", 0)
        self.nodefine1_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.nodefine1_progressBar.setObjectName("nodefine1_progressBar")
        self.horizontalLayout_6.addWidget(self.nodefine1_progressBar)
        spacerItem7 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 1)
        self.horizontalLayout_6.setStretch(2, 4)
        self.horizontalLayout_6.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_nodefine2_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_nodefine2_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_nodefine2_.setFont(font)
        self.label_nodefine2_.setObjectName("label_nodefine2_")
        self.horizontalLayout_7.addWidget(self.label_nodefine2_)
        spacerItem8 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.nodefine2_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.nodefine2_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.nodefine2_progressBar.setFont(font)
        self.nodefine2_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.nodefine2_progressBar.setProperty("value", 0)
        self.nodefine2_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.nodefine2_progressBar.setObjectName("nodefine2_progressBar")
        self.horizontalLayout_7.addWidget(self.nodefine2_progressBar)
        spacerItem9 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)
        self.horizontalLayout_7.setStretch(2, 4)
        self.horizontalLayout_7.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_defective_rate_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_defective_rate_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_defective_rate_.setFont(font)
        self.label_defective_rate_.setObjectName("label_defective_rate_")
        self.horizontalLayout_16.addWidget(self.label_defective_rate_)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem10)
        self.defective_rate_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.defective_rate_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.defective_rate_progressBar.setFont(font)
        self.defective_rate_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.defective_rate_progressBar.setProperty("value", 0)
        self.defective_rate_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.defective_rate_progressBar.setObjectName("defective_rate_progressBar")
        self.horizontalLayout_16.addWidget(self.defective_rate_progressBar)
        spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem11)
        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 4)
        self.horizontalLayout_16.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_yield_rate_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_yield_rate_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_yield_rate_.setFont(font)
        self.label_yield_rate_.setObjectName("label_yield_rate_")
        self.horizontalLayout_17.addWidget(self.label_yield_rate_)
        spacerItem12 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem12)
        self.yield_rate_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.yield_rate_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yield_rate_progressBar.setFont(font)
        self.yield_rate_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.yield_rate_progressBar.setProperty("value", 0)
        self.yield_rate_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.yield_rate_progressBar.setObjectName("yield_rate_progressBar")
        self.horizontalLayout_17.addWidget(self.yield_rate_progressBar)
        spacerItem13 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem13)
        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 1)
        self.horizontalLayout_17.setStretch(2, 4)
        self.horizontalLayout_17.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_total_production_ = QtWidgets.QLabel(self.groupBox_0)
        self.label_total_production_.setMaximumSize(QtCore.QSize(44, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_total_production_.setFont(font)
        self.label_total_production_.setObjectName("label_total_production_")
        self.horizontalLayout_18.addWidget(self.label_total_production_)
        spacerItem14 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem14)
        self.total_production_progressBar = QtWidgets.QProgressBar(self.groupBox_0)
        self.total_production_progressBar.setMinimumSize(QtCore.QSize(114, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.total_production_progressBar.setFont(font)
        self.total_production_progressBar.setStyleSheet("QProgressBar {color: red;}")
        self.total_production_progressBar.setProperty("value", 0)
        self.total_production_progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.total_production_progressBar.setObjectName("total_production_progressBar")
        self.horizontalLayout_18.addWidget(self.total_production_progressBar)
        spacerItem15 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem15)
        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 1)
        self.horizontalLayout_18.setStretch(2, 4)
        self.horizontalLayout_18.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem16)
        self.save_data_pushButton = QtWidgets.QPushButton(self.groupBox_0)
        self.save_data_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.save_data_pushButton.setMaximumSize(QtCore.QSize(60, 25))
        self.save_data_pushButton.setObjectName("save_data_pushButton")
        self.horizontalLayout_19.addWidget(self.save_data_pushButton)
        self.cleardata_pushButton = QtWidgets.QPushButton(self.groupBox_0)
        self.cleardata_pushButton.setMinimumSize(QtCore.QSize(0, 25))
        self.cleardata_pushButton.setMaximumSize(QtCore.QSize(60, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.cleardata_pushButton.setFont(font)
        self.cleardata_pushButton.setObjectName("cleardata_pushButton")
        self.horizontalLayout_19.addWidget(self.cleardata_pushButton)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem17)
        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(2, 2)
        self.horizontalLayout_19.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20.addLayout(self.verticalLayout)
        self.horizontalLayout_4.addWidget(self.groupBox_0)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 2)
        self.horizontalLayout_4.setStretch(2, 2)
        self.horizontalLayout_4.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label4_camera = QtWidgets.QLabel(self.groupBox_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label4_camera.setFont(font)
        self.label4_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label4_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label4_camera.setObjectName("label4_camera")
        self.horizontalLayout_11.addWidget(self.label4_camera)
        self.horizontalLayout_14.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label5_camera = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label5_camera.setFont(font)
        self.label5_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label5_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label5_camera.setObjectName("label5_camera")
        self.horizontalLayout_12.addWidget(self.label5_camera)
        self.horizontalLayout_14.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label6_camera = QtWidgets.QLabel(self.groupBox_6)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label6_camera.setFont(font)
        self.label6_camera.setFrameShape(QtWidgets.QFrame.Box)
        self.label6_camera.setAlignment(QtCore.Qt.AlignCenter)
        self.label6_camera.setObjectName("label6_camera")
        self.horizontalLayout_13.addWidget(self.label6_camera)
        self.horizontalLayout_14.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setStyleSheet("QGroupBox#groupBox_7 { border: 1px solid black;}")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem18)
        self.loadcamera_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.loadcamera_pushButton.setMinimumSize(QtCore.QSize(88, 40))
        self.loadcamera_pushButton.setObjectName("loadcamera_pushButton")
        self.verticalLayout_2.addWidget(self.loadcamera_pushButton)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem19)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton.setMinimumSize(QtCore.QSize(88, 40))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem20)
        self.stop_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.stop_pushButton.setMinimumSize(QtCore.QSize(88, 40))
        self.stop_pushButton.setCheckable(True)
        self.stop_pushButton.setObjectName("stop_pushButton")
        self.verticalLayout_2.addWidget(self.stop_pushButton)
        spacerItem21 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem21)
        self.save_pic_mode_pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.save_pic_mode_pushButton.setMinimumSize(QtCore.QSize(88, 40))
        self.save_pic_mode_pushButton.setCheckable(True)
        self.save_pic_mode_pushButton.setObjectName("save_pic_mode_pushButton")
        self.verticalLayout_2.addWidget(self.save_pic_mode_pushButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.horizontalLayout_14.addWidget(self.groupBox_7)
        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 2)
        self.horizontalLayout_14.setStretch(2, 2)
        self.horizontalLayout_14.setStretch(3, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem22)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_21.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_21.addWidget(self.pushButton_3)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem23)
        self.baud_label = QtWidgets.QLabel(self.frame)
        self.baud_label.setMinimumSize(QtCore.QSize(80, 40))
        self.baud_label.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.baud_label.setFont(font)
        self.baud_label.setAlignment(QtCore.Qt.AlignCenter)
        self.baud_label.setObjectName("baud_label")
        self.horizontalLayout_21.addWidget(self.baud_label)
        self.baudrate_comboBox = QtWidgets.QComboBox(self.frame)
        self.baudrate_comboBox.setMinimumSize(QtCore.QSize(0, 40))
        self.baudrate_comboBox.setObjectName("baudrate_comboBox")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.baudrate_comboBox.addItem("")
        self.horizontalLayout_21.addWidget(self.baudrate_comboBox)
        self.comboBox_ports = QtWidgets.QComboBox(self.frame)
        self.comboBox_ports.setMinimumSize(QtCore.QSize(0, 40))
        self.comboBox_ports.setObjectName("comboBox_ports")
        self.horizontalLayout_21.addWidget(self.comboBox_ports)
        self.connect_port_pushButton = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connect_port_pushButton.sizePolicy().hasHeightForWidth())
        self.connect_port_pushButton.setSizePolicy(sizePolicy)
        self.connect_port_pushButton.setMinimumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.connect_port_pushButton.setFont(font)
        self.connect_port_pushButton.setObjectName("connect_port_pushButton")
        self.horizontalLayout_21.addWidget(self.connect_port_pushButton)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem24)
        self.horizontalLayout_21.setStretch(0, 6)
        self.horizontalLayout_22.addLayout(self.horizontalLayout_21)
        self.verticalLayout_3.addWidget(self.frame)
        self.verticalLayout_3.setStretch(2, 6)
        self.verticalLayout_3.setStretch(3, 6)
        self.horizontalLayout_15.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1190, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.statusbar.setFont(font)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setting_action = QtWidgets.QAction(MainWindow)
        self.setting_action.setObjectName("setting_action")
        self.menu.addAction(self.setting_action)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "欢迎使用视觉检测软件"))
        self.groupBox.setTitle(_translate("MainWindow", "一号相机"))
        self.label1_camera.setText(_translate("MainWindow", "一号相机画面"))
        self.groupBox_2.setTitle(_translate("MainWindow", "二号相机"))
        self.label2_camera.setText(_translate("MainWindow", "二号相机画面"))
        self.groupBox_3.setTitle(_translate("MainWindow", "三号相机"))
        self.label3_camera.setText(_translate("MainWindow", "三号相机画面"))
        self.groupBox_0.setTitle(_translate("MainWindow", "统计"))
        self.label_sctatch_.setText(_translate("MainWindow", "划  痕"))
        self.sctatch_progressBar.setFormat(_translate("MainWindow", "%v"))
        self.label_blackpoint_.setText(_translate("MainWindow", "黑  点"))
        self.blackpoint_progressBar.setFormat(_translate("MainWindow", "%v"))
        self.label_nodefine0_.setText(_translate("MainWindow", "缺  陷"))
        self.nodefine0_progressBar.setFormat(_translate("MainWindow", "%v"))
        self.label_nodefine1_.setText(_translate("MainWindow", "缺  陷"))
        self.nodefine1_progressBar.setFormat(_translate("MainWindow", "%v"))
        self.label_nodefine2_.setText(_translate("MainWindow", "缺  陷"))
        self.nodefine2_progressBar.setFormat(_translate("MainWindow", "%v"))
        self.label_defective_rate_.setText(_translate("MainWindow", "不良率"))
        self.defective_rate_progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_yield_rate_.setText(_translate("MainWindow", "良  率"))
        self.yield_rate_progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.label_total_production_.setText(_translate("MainWindow", "总  量"))
        self.total_production_progressBar.setFormat(_translate("MainWindow", "%v"))
        self.save_data_pushButton.setText(_translate("MainWindow", "保存数据"))
        self.cleardata_pushButton.setText(_translate("MainWindow", "清零统计"))
        self.groupBox_4.setTitle(_translate("MainWindow", "四号相机"))
        self.label4_camera.setText(_translate("MainWindow", "四号相机画面"))
        self.groupBox_5.setTitle(_translate("MainWindow", "五号相机"))
        self.label5_camera.setText(_translate("MainWindow", "五号相机画面"))
        self.groupBox_6.setTitle(_translate("MainWindow", "六号相机"))
        self.label6_camera.setText(_translate("MainWindow", "六号相机画面"))
        self.groupBox_7.setTitle(_translate("MainWindow", "功能按键"))
        self.loadcamera_pushButton.setText(_translate("MainWindow", "加载相机"))
        self.pushButton.setText(_translate("MainWindow", "启动检测"))
        self.stop_pushButton.setText(_translate("MainWindow", "停止检测"))
        self.save_pic_mode_pushButton.setText(_translate("MainWindow", "存照模式"))
        self.pushButton_2.setText(_translate("MainWindow", "加载相机"))
        self.pushButton_3.setText(_translate("MainWindow", "开始检测"))
        self.baud_label.setText(_translate("MainWindow", "波特率"))
        self.baudrate_comboBox.setItemText(0, _translate("MainWindow", "9600"))
        self.baudrate_comboBox.setItemText(1, _translate("MainWindow", "19200"))
        self.baudrate_comboBox.setItemText(2, _translate("MainWindow", "38400"))
        self.baudrate_comboBox.setItemText(3, _translate("MainWindow", "57600"))
        self.baudrate_comboBox.setItemText(4, _translate("MainWindow", "115200"))
        self.baudrate_comboBox.setItemText(5, _translate("MainWindow", "50"))
        self.baudrate_comboBox.setItemText(6, _translate("MainWindow", "75"))
        self.baudrate_comboBox.setItemText(7, _translate("MainWindow", "110"))
        self.baudrate_comboBox.setItemText(8, _translate("MainWindow", "134"))
        self.baudrate_comboBox.setItemText(9, _translate("MainWindow", "150"))
        self.baudrate_comboBox.setItemText(10, _translate("MainWindow", "200"))
        self.baudrate_comboBox.setItemText(11, _translate("MainWindow", "300"))
        self.baudrate_comboBox.setItemText(12, _translate("MainWindow", "600"))
        self.baudrate_comboBox.setItemText(13, _translate("MainWindow", "1200"))
        self.baudrate_comboBox.setItemText(14, _translate("MainWindow", "1800"))
        self.baudrate_comboBox.setItemText(15, _translate("MainWindow", "2400"))
        self.baudrate_comboBox.setItemText(16, _translate("MainWindow", "4800"))
        self.connect_port_pushButton.setText(_translate("MainWindow", "连接串口"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.setting_action.setText(_translate("MainWindow", "设置"))