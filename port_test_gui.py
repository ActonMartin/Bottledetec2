# from ui.ui_port_test import Ui_MainWindow
from ui_port_test import Ui_MainWindow
from PyQt5.QtCore import QSettings, QTimer, Qt, QDateTime
from PyQt5.QtGui import QIcon, QImage, QPixmap,QCloseEvent
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QComboBox,QMessageBox)
from functionCode.get_cwd import get_save_path,get_save_excel,get_cwd
import clr  # add C# support
# 加载dll
a_path = get_cwd()
dll_path = a_path + '/DLL_test'
clr.AddReference(dll_path)
from DLL_test import *

class KK(QMainWindow):
    def __init__(self):
        super(KK, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.cam1_ok.setEnabled(0)
        self.ui.cam2_ok.setEnabled(0)
        self.ui.cam3_ok.setEnabled(0)
        self.ui.cam4_ok.setEnabled(0)
        self.ui.cam5_ok.setEnabled(0)
        self.ui.cam6_ok.setEnabled(0)

        self.get_all_port()
        self.dll_instance = My_Dll()
        self.ui.connect_pushButton.clicked.connect(self.connect_port)
        self.ui.cam1_ok.clicked.connect(self.cam1_ok_)
        self.ui.cam2_ok.clicked.connect(self.cam2_ok_)
        self.ui.cam3_ok.clicked.connect(self.cam3_ok_)
        self.ui.cam4_ok.clicked.connect(self.cam4_ok_)
        self.ui.cam5_ok.clicked.connect(self.cam5_ok_)
        self.ui.cam6_ok.clicked.connect(self.cam6_ok_)
        self.ui.cam1_4.clicked.connect(self.cam1_4)



    def cam1_ok_(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('01')
            if a:
                QMessageBox.warning(self, 'cam1报警成功', 'cam1报警成功')
        except:
            pass

    def cam2_ok_(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('02')
            if a:
                QMessageBox.warning(self, 'cam2报警成功', 'cam2报警成功')
        except:
            pass

    def cam3_ok_(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('04')
            if a:
                QMessageBox.warning(self, 'cam3报警成功', 'cam3报警成功')
        except:
            pass

    def cam4_ok_(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('08')
            if a:
                QMessageBox.warning(self, 'cam4报警成功', 'cam4报警成功')
        except:
            pass

    def cam5_ok_(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('10')
            if a:
                QMessageBox.warning(self, 'cam5报警成功', 'cam5报警成功')
        except:
            pass

    def cam6_ok_(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('20')
            if a:
                QMessageBox.warning(self, 'cam6报警成功', 'cam6报警成功')
        except:
            pass

    def cam1_4(self):
        try:
            a = self.dll_instance.serial_port_Beep_ON('09')
            if a:
                QMessageBox.warning(self, 'cam1和4报警成功', 'cam1和4报警成功')
        except:
            pass


    def get_all_port(self):
        from serial.tools import list_ports
        port_list = list(list_ports.comports())
        num = len(port_list)
        ports = []
        if num <= 0:
            print("找不到任何串口设备")
        else:
            for i in range(num):
                # 将 ListPortInfo 对象转化为 list
                port = list(port_list[i])[0]
                ports.append(port)
        self.ui.comboBox_ports.addItems(ports)

    def set_all_campushbutton_on(self):
        self.ui.cam1_ok.setEnabled(1)
        self.ui.cam2_ok.setEnabled(2)
        self.ui.cam3_ok.setEnabled(1)
        self.ui.cam4_ok.setEnabled(1)
        self.ui.cam5_ok.setEnabled(1)
        self.ui.cam6_ok.setEnabled(1)


    def connect_port(self):
        port = self.ui.comboBox_ports.currentText()
        try:
            a = self.dll_instance.serial_port_Open(port)
            if a:
                QMessageBox.warning(self, '串口{}'.format(port), '串口{}打开成功'.format(port))
                self.set_all_campushbutton_on()
        except:
            QMessageBox.warning(self, '串口{}'.format(port), '串口{}打开失败'.format(port))


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    LOGWINDOW = KK()
    LOGWINDOW.show()
    sys.exit(APP.exec_())