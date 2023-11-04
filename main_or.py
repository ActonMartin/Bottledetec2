from ui.ui_MainPage import Ui_MainWindow
from PyQt5.QtCore import QSettings, QTimer, Qt, QDateTime,QThread,pyqtSignal,QObject,pyqtSlot
from PyQt5.QtGui import QIcon, QImage, QPixmap,QCloseEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow,
                             QMessageBox)
import sys
# from functionCode.camera import Camera,get_devices_list
from functionCode.Camera_new_method import *
from functionCode.get_cwd import get_save_path,get_save_excel
import cv2
import threading
import os
from NET.yolo import YOLO
from PIL import Image
import numpy as np
import datetime
import time
from ui.open_setting import Settings
import xlwt
"""
连续模式
"""


class Worker(QObject):
    time_shijian = pyqtSignal(str)
    @pyqtSlot()
    def work(self): # A slot takes no params
        while 1:
            time.sleep(1)
            datatime = datetime.datetime.now()
            text = datatime.strftime('%Y-%m-%d %H:%M:%S')
            self.time_shijian.emit(text)
            # datatime = QDateTime.currentDateTime()
            # text = datatime.toString('yyyy年MM月dd日 dddd hh:mm:ss')
            # self.time_shijian.emit(text)


class MainWindows(QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('安瓿瓶缺陷检测')
        self.setWindowIcon(QIcon('ICON/logo.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.time_thread()
        self.ui.setting_action.triggered.connect(self.opensettings)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_old)
        self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_1)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_2)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_3)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_4)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_5)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_camera_6)
        # self.ui.loadcamera_pushButton.clicked.connect(self.load_end_step)



        # self.ui.pushButton.clicked.connect(self.load_timer)
        self.ui.pushButton.clicked.connect(self.load_timer1)
        # self.ui.pushButton.clicked.connect(self.load_timer2)
        # self.ui.pushButton.clicked.connect(self.load_timer3)
        # self.ui.pushButton.clicked.connect(self.load_timer4)
        # self.ui.pushButton.clicked.connect(self.load_timer5)
        # self.ui.pushButton.clicked.connect(self.load_timer6)
        self.ui.pushButton.clicked.connect(self.load_timer_end_step)


        self.ui.save_data_pushButton.clicked.connect(self.save_data_2_excel)
        self.ui.save_data_pushButton.setEnabled(0)
        self.ui.pushButton.setEnabled(0)
        self.ui.stop_pushButton.setEnabled(0)
        self.ui.save_pic_mode_pushButton.setEnabled(0)
        self.deviceList = enum_devices(device=0, device_way=False)
        # self.load_camera()
        # self.load_timer()
        self.rate = 5
        """开启一个线程加载模型"""
        self.load_model_thread = threading.Thread(target=self.load_model,args=())
        self.load_model_thread.start()

        self.ui.cleardata_pushButton.clicked.connect(self.clear_data)
        self.ui.stop_pushButton.clicked.connect(self.stop_check)
        self.ui.save_pic_mode_pushButton.clicked.connect(self.save_pic_mode)

        self.restore_data()
        # self.black_point, self.scratch, self.nodefine0, self.nodefine1, self.nodefine2 = 0, 0, 0, 0, 0
        # self.total_production, self.defective_rate, self.yield_rate, self.bad, self.good = 0, 0, 1, 0, 0
        """计算时间用，已经注释"""
        # self.count = 0
        # self.time_count = 0
        # self.save_pic('00')


    def save_pic_mode(self,pressed):
        if pressed:
            self.save_mode = 1
            self.ui.save_pic_mode_pushButton.setStyleSheet("border:2px solid rgb(0, 238, 0)") # green
        else:
            self.save_mode = 0
            self.ui.save_pic_mode_pushButton.setStyleSheet("border:2px solid rgb(255, 0, 0)") # red

    def stop_check(self,pressed):
        # self.stop = 0
        if pressed:
            self.stop = 0
            self.ui.stop_pushButton.setStyleSheet("border:2px solid rgb(255, 0, 0)")  # red
        else:
            self.stop = 1
            self.ui.stop_pushButton.setStyleSheet("border:2px solid rgb(0, 238, 0)")  # green

    def save_data_2_excel(self):
        cur_time = datetime.datetime.now()
        cur_time = cur_time.strftime('%Y_%m_%d_%H_%M_%S')
        save_excel_path = get_save_excel()
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
        booksheet.write(0, 0, '划痕')
        booksheet.write(1, 0, '黑点')
        booksheet.write(2, 0, '缺陷')
        booksheet.write(3, 0, '缺陷')
        booksheet.write(4, 0, '缺陷')
        booksheet.write(5, 0, '不良率')
        booksheet.write(6, 0, '良率')
        booksheet.write(7, 0, '总量')
        booksheet.write(0, 1, self.scratch)
        booksheet.write(1,1,self.black_point)
        booksheet.write(2,1,self.nodefine0)
        booksheet.write(3,1,self.nodefine1)
        booksheet.write(4,1,self.nodefine2)
        booksheet.write(5,1,self.defective_rate)
        booksheet.write(6,1,self.yield_rate)
        booksheet.write(7,1,self.total_production)
        workbook.save(save_excel_path+'\\' + cur_time+'_result.xls')

    def time_thread(self):
        self.worker = Worker()  # no parent!
        self.thread_time = QThread()  # no parent!
        self.worker.time_shijian.connect(self.show_time)
        self.worker.moveToThread(self.thread_time)
        self.thread_time.started.connect(self.worker.work)
        # self.thread.finished.connect(app.exit)
        self.thread_time.start()

    def show_time(self,text):
        self.ui.label_time.setText(text)

    def restore_data(self):
        self.config = QSettings('bottledetect_config.ini', QSettings.IniFormat)

        if self.config.value('restore') is None:
            self.black_point, self.scratch, self.nodefine0, self.nodefine1, self.nodefine2 = 0, 0, 0, 0, 0
            self.total_production, self.defective_rate, self.yield_rate, self.bad, self.good = 0, 0, 1, 0, 0

        if self.config.value('restore') is not None:
            self.ui.save_data_pushButton.setEnabled(1)
            self.black_point = int(self.config.value('black_point'))
            self.scratch = int(self.config.value('scratch'))
            self.nodefine0 = int(self.config.value('nodefine0'))
            self.nodefine1 = int(self.config.value('nodefine1'))
            self.nodefine2 = int(self.config.value('nodefine2'))
            self.total_production = int(self.config.value('total_production'))
            # print('total_production',self.total_production,type(self.total_production))
            self.bad = int(self.config.value('bad'))
            self.good = int(self.config.value('good'))
            self.defective_rate = float(self.config.value('defective_rate'))
            self.yield_rate = float(self.config.value('yield_rate'))
            self.defective_rate_baifen = '%.2f%%' % (self.defective_rate * 100)
            self.yield_rate_baifen = '%.2f%%' % (self.yield_rate * 100)
            # print(self.black_point,self.scratch)
            # self.ui.label_blackpoint.setText(str(self.black_point))
            # self.ui.label_sctatch.setText(str(self.scratch))
            # self.ui.label_nodefine0.setText(str(self.nodefine0))
            # self.ui.label_nodefine1.setText(str(self.nodefine1))
            # self.ui.label_nodefine2.setText(str(self.nodefine2))
            # self.ui.label_total_production.setText(str((self.total_production)* self.rate))
            # self.ui.label_defective_rate.setText(str(
            #     self.defective_rate_baifen))
            # self.ui.label_yield_rate.setText(str(self.yield_rate_baifen))

            self.ui.blackpoint_progressBar.setMaximum(self.total_production+1)
            self.ui.blackpoint_progressBar.setValue(self.black_point)
            self.ui.sctatch_progressBar.setMaximum(self.total_production+1)
            self.ui.sctatch_progressBar.setValue(self.scratch)
            self.ui.nodefine0_progressBar.setMaximum(self.total_production+1)
            self.ui.nodefine0_progressBar.setValue(self.nodefine0)
            self.ui.nodefine1_progressBar.setMaximum(self.total_production+1)
            self.ui.nodefine1_progressBar.setValue(self.nodefine1)
            self.ui.nodefine2_progressBar.setMaximum(self.total_production+1)
            self.ui.nodefine2_progressBar.setValue(self.nodefine2)

            self.ui.defective_rate_progressBar.setMaximum(100*100)
            self.ui.defective_rate_progressBar.setValue(self.defective_rate*100*100)
            self.ui.defective_rate_progressBar.setFormat("%.02f %%" % (self.defective_rate*100))

            self.ui.yield_rate_progressBar.setMaximum(100*100)
            self.ui.yield_rate_progressBar.setValue(self.yield_rate*100*100)
            self.ui.yield_rate_progressBar.setFormat("%.02f %%" % (self.yield_rate*100))

            self.ui.total_production_progressBar.setMaximum(self.total_production+1)
            self.ui.total_production_progressBar.setValue(self.total_production)

    def clear_data(self):
        self.black_point, self.scratch, self.nodefine0, self.nodefine1, self.nodefine2 = 0, 0, 0, 0, 0
        self.total_production, self.defective_rate, self.yield_rate, self.bad, self.good = 0, 0, 1, 0, 0
        # self.ui.label_sctatch.setText('0')
        # self.ui.label_blackpoint.setText('0')
        # self.ui.label_nodefine0.setText('0')
        # self.ui.label_nodefine1.setText('0')
        # self.ui.label_nodefine2.setText('0')
        #
        # self.ui.label_total_production.setText('0')
        # self.ui.label_defective_rate.setText('0')
        # self.ui.label_yield_rate.setText('100%')
        self.ui.blackpoint_progressBar.setMaximum(self.total_production+1)
        self.ui.blackpoint_progressBar.setValue(0)
        self.ui.sctatch_progressBar.setMaximum(self.total_production+1)
        self.ui.sctatch_progressBar.setValue(0)
        self.ui.nodefine0_progressBar.setMaximum(self.total_production+1)
        self.ui.nodefine0_progressBar.setValue(0)
        self.ui.nodefine1_progressBar.setMaximum(self.total_production+1)
        self.ui.nodefine1_progressBar.setValue(0)
        self.ui.nodefine2_progressBar.setMaximum(self.total_production+1)
        self.ui.nodefine2_progressBar.setValue(0)
        self.ui.total_production_progressBar.setMaximum(self.total_production+1)
        self.ui.total_production_progressBar.setValue(0)

        self.ui.defective_rate_progressBar.setMaximum(100*100)
        self.ui.defective_rate_progressBar.setValue(0)
        self.ui.defective_rate_progressBar.setFormat("%.02f %%" % (0.00 * 100))

        self.ui.yield_rate_progressBar.setMaximum(100*100)
        self.ui.yield_rate_progressBar.setValue(100*100)
        self.ui.yield_rate_progressBar.setFormat("%.02f %%" % (1.00 * 100))

        self.config.setValue('restore', '1')
        self.config.setValue('black_point', str(self.black_point))
        self.config.setValue('scratch', str(self.scratch))
        self.config.setValue('nodefine0', str(self.nodefine0))
        self.config.setValue('nodefine1', str(self.nodefine1))
        self.config.setValue('nodefine2', str(self.nodefine2))
        self.config.setValue('total_production', str(self.total_production))
        self.config.setValue('defective_rate', str(self.defective_rate))
        self.config.setValue('yield_rate', str(self.yield_rate))
        self.config.setValue('bad',str(self.bad))
        self.config.setValue('good',str(self.good))

    def opensettings(self):
        self.settings_page = Settings()
        self.settings_page.show()

    def load_timer1(self):
        self.stop = 1
        self.timer_camera1 = QTimer()
        self.timer_camera1.timeout.connect(self.show_image_on_label1)
        # self.timer_camera.timeout.connect(self.show_image_on_label_old_methed)
        self.timer_camera1.start(200)
        # self.ui.save_data_pushButton.setEnabled(1)
        # self.ui.stop_pushButton.setEnabled(1)
        # self.ui.save_pic_mode_pushButton.setEnabled(1)
        # self.ui.pushButton.setEnabled(0)

    def load_timer2(self):
        self.stop = 1
        self.timer_camera2 = QTimer()
        self.timer_camera2.timeout.connect(self.show_image_on_label2)
        # self.timer_camera.timeout.connect(self.show_image_on_label_old_methed)
        self.timer_camera3.start(200)
        # self.ui.save_data_pushButton.setEnabled(1)
        # self.ui.stop_pushButton.setEnabled(1)
        # self.ui.save_pic_mode_pushButton.setEnabled(1)
        # self.ui.pushButton.setEnabled(0)

    def load_timer3(self):
        self.stop = 1
        self.timer_camera3 = QTimer()
        self.timer_camera3.timeout.connect(self.show_image_on_label3)
        # self.timer_camera.timeout.connect(self.show_image_on_label_old_methed)
        self.timer_camera3.start(200)
        # self.ui.save_data_pushButton.setEnabled(1)
        # self.ui.stop_pushButton.setEnabled(1)
        # self.ui.save_pic_mode_pushButton.setEnabled(1)
        # self.ui.pushButton.setEnabled(0)

    def load_timer4(self):
        self.stop = 1
        self.timer_camera4 = QTimer()
        self.timer_camera4.timeout.connect(self.show_image_on_label4)
        # self.timer_camera.timeout.connect(self.show_image_on_label_old_methed)
        self.timer_camera4.start(200)
        # self.ui.save_data_pushButton.setEnabled(1)
        # self.ui.stop_pushButton.setEnabled(1)
        # self.ui.save_pic_mode_pushButton.setEnabled(1)
        # self.ui.pushButton.setEnabled(0)
    def load_timer5(self):
        self.stop = 1
        self.timer_camera5 = QTimer()
        self.timer_camera5.timeout.connect(self.show_image_on_label5)
        # self.timer_camera.timeout.connect(self.show_image_on_label_old_methed)
        self.timer_camera5.start(200)
        # self.ui.save_data_pushButton.setEnabled(1)
        # self.ui.stop_pushButton.setEnabled(1)
        # self.ui.save_pic_mode_pushButton.setEnabled(1)
        # self.ui.pushButton.setEnabled(0)
    def load_timer6(self):
        self.stop = 1
        self.timer_camera6 = QTimer()
        self.timer_camera6.timeout.connect(self.show_image_on_label6)
        # self.timer_camera.timeout.connect(self.show_image_on_label_old_methed)
        self.timer_camera1.start(200)
        # self.ui.save_data_pushButton.setEnabled(1)
        # self.ui.stop_pushButton.setEnabled(1)
        # self.ui.save_pic_mode_pushButton.setEnabled(1)
        # self.ui.pushButton.setEnabled(0)

    def load_timer_end_step(self):
        self.ui.save_data_pushButton.setEnabled(1)
        self.ui.stop_pushButton.setEnabled(1)
        self.ui.save_pic_mode_pushButton.setEnabled(1)
        self.ui.pushButton.setEnabled(0)

    def count_defects(self, list_,a):
        self.total_production += 1
        if list_:
            list_ = list(set(list_))
            # print('list_',list_)
            self.ui.statusbar.showMessage(a+'检测到缺陷',2000)
            try:
                # self.which_id_find_defection = 1
                self.black_point += list_.count(0)
                # self.good += list_.count(1)
                self.scratch += list_.count(2)
                self.nodefine0 += list_.count(3)
                self.nodefine1 += list_.count(4)
                self.nodefine2 += list_.count(5)
            except:
                pass
            try:
                if 0 in list_ or 2 in list_ or 3 in list_ or 4 in list_ or 5 in list_:
                    self.bad += 1
            except:
                pass
        else:
            self.ui.statusbar.clearMessage()
        self.defective_rate = self.bad / (self.total_production * self.rate)
        self.yield_rate = 1 - self.defective_rate

    def showresult(self):
        # try:
        #     self.ui.label_blackpoint.setText(str(self.black_point))
        #     self.ui.label_sctatch.setText(str(self.scratch))
        #     self.ui.label_nodefine0.setText(str(self.nodefine0))
        #     self.ui.label_nodefine1.setText(str(self.nodefine1))
        #     self.ui.label_nodefine2.setText(str(self.nodefine2))
        #
        #     self.defective_rate_baifen = '%.2f%%' % (self.defective_rate * 100)
        #     self.yield_rate_baifen = '%.2f%%' % (self.yield_rate * 100)
        #     # print(self.defective_rate,self.yield_rate)
        #     # print(self.defective_rate_baifen,self.yield_rate_baifen)
        #     self.ui.label_defective_rate.setText(str(
        #         self.defective_rate_baifen))
        #     self.ui.label_yield_rate.setText(str(self.yield_rate_baifen))
        #     self.ui.label_total_production.setText(
        #         str(self.total_production * self.rate))
        # except:
        #     pass
        try:
            self.ui.blackpoint_progressBar.setMaximum(self.total_production)
            self.ui.blackpoint_progressBar.setValue(self.black_point)
            self.ui.sctatch_progressBar.setMaximum(self.total_production)
            self.ui.sctatch_progressBar.setValue(self.scratch)
            self.ui.nodefine0_progressBar.setMaximum(self.total_production)
            self.ui.nodefine0_progressBar.setValue(self.nodefine0)
            self.ui.nodefine1_progressBar.setMaximum(self.total_production)
            self.ui.nodefine1_progressBar.setValue(self.nodefine1)
            self.ui.nodefine2_progressBar.setMaximum(self.total_production)
            self.ui.nodefine2_progressBar.setValue(self.nodefine2)

            self.ui.defective_rate_progressBar.setMaximum(100*100)
            self.ui.defective_rate_progressBar.setValue(self.defective_rate*100*100)
            self.ui.defective_rate_progressBar.setFormat("%.02f %%" % (self.defective_rate * 100))

            self.ui.yield_rate_progressBar.setMaximum(100*100)
            self.ui.yield_rate_progressBar.setValue(self.yield_rate*100*100)
            self.ui.yield_rate_progressBar.setFormat("%.02f %%" % (self.yield_rate * 100))
            self.ui.total_production_progressBar.setMaximum(self.total_production + 1)
            self.ui.total_production_progressBar.setValue(self.total_production)
        except:
            pass

        try:
            self.config.setValue('restore', '1')
            self.config.setValue('black_point',str(self.black_point))
            self.config.setValue('scratch',str(self.scratch))
            self.config.setValue('nodefine0',str(self.nodefine0))
            self.config.setValue('nodefine1',str(self.nodefine1))
            self.config.setValue('nodefine2',str(self.nodefine2))
            self.config.setValue('total_production',str(self.total_production))
            self.config.setValue('bad',str(self.bad))
            self.config.setValue('good',str(self.good))
            self.config.setValue('defective_rate',str(self.defective_rate))
            self.config.setValue('yield_rate',str(self.yield_rate))
        except:
            pass

    def load_model(self):
        try:
            self.yolo = YOLO()
        except:
            print('模型加载失败')

    def load_camera_old(self):
        try:
            self.cam1, _1 = creat_camera(self.deviceList, 0, log=False)
            open_device(self.cam1)
            start_grab_and_get_data_size(self.cam1)
            self.cam1_flag = 1
        except:
            self.cam1_flag = 0
            QMessageBox.warning(self, '相机', '一号相机没有启动成功')
        try:
            self.cam2, _2 = creat_camera(self.deviceList, 1, log=False)
            open_device(self.cam2)
            start_grab_and_get_data_size(self.cam2)
            self.cam2_flag = 1
        except:
            self.cam2_flag = 0
            QMessageBox.warning(self, '相机', '二号相机没有启动成功')
        try:
            self.cam3, _3 = creat_camera(self.deviceList, 2, log=False)
            open_device(self.cam3)
            start_grab_and_get_data_size(self.cam3)
            self.cam3_flag = 1
        except:
            self.cam3_flag = 0
            QMessageBox.warning(self, '相机', '三号相机没有启动成功')
        try:
            self.cam4, _4 = creat_camera(self.deviceList, 3, log=False)
            open_device(self.cam4)
            start_grab_and_get_data_size(self.cam4)
            self.cam4_flag = 1
        except:
            self.cam4_flag = 0
            QMessageBox.warning(self, '相机', '四号相机没有启动成功')
        try:
            self.cam5, _5 = creat_camera(self.deviceList, 4, log=False)
            open_device(self.cam5)
            start_grab_and_get_data_size(self.cam5)
            self.cam5_flag = 1
        except:
            self.cam5_flag = 0
            QMessageBox.warning(self, '相机', '五号相机没有启动成功')
        try:
            self.cam6, _6 = creat_camera(self.deviceList, 5, log=False)
            open_device(self.cam6)
            start_grab_and_get_data_size(self.cam6)
            self.cam6_flag = 1
        except:
            self.cam6_flag = 0
            QMessageBox.warning(self, '相机', '六号相机没有启动成功')

        self.ui.pushButton.setEnabled(1)
        self.ui.loadcamera_pushButton.setEnabled(0)

    def load_camera_1(self):
        try:
            self.cam1, _1 = creat_camera(self.deviceList, 0, log=False)
            open_device(self.cam1)
            start_grab_and_get_data_size(self.cam1)
            self.cam1_flag = 1
        except:
            self.cam1_flag = 0
            QMessageBox.warning(self, '相机', '一号相机没有启动成功')

    def load_camera_2(self):
        try:
            self.cam2, _2 = creat_camera(self.deviceList, 1, log=False)
            open_device(self.cam2)
            start_grab_and_get_data_size(self.cam2)
            self.cam2_flag = 1
        except:
            self.cam2_flag = 0
            QMessageBox.warning(self, '相机', '二号相机没有启动成功')

    def load_camera_3(self):
        try:
            self.cam3, _3 = creat_camera(self.deviceList, 2, log=False)
            open_device(self.cam3)
            start_grab_and_get_data_size(self.cam3)
            self.cam3_flag = 1
        except:
            self.cam3_flag = 0
            QMessageBox.warning(self, '相机', '三号相机没有启动成功')

    def load_camera_4(self):
        try:
            self.cam4, _4 = creat_camera(self.deviceList, 3, log=False)
            open_device(self.cam4)
            start_grab_and_get_data_size(self.cam4)
            self.cam4_flag = 1
        except:
            self.cam4_flag = 0
            QMessageBox.warning(self, '相机', '四号相机没有启动成功')

    def load_camera_5(self):
        try:
            self.cam5, _5 = creat_camera(self.deviceList, 4, log=False)
            open_device(self.cam5)
            start_grab_and_get_data_size(self.cam5)
            self.cam5_flag = 1
        except:
            self.cam5_flag = 0
            QMessageBox.warning(self, '相机', '五号相机没有启动成功')

    def load_camera_6(self):
        try:
            self.cam6, _6 = creat_camera(self.deviceList, 5, log=False)
            open_device(self.cam6)
            start_grab_and_get_data_size(self.cam6)
            self.cam6_flag = 1
        except:
            self.cam6_flag = 0
            QMessageBox.warning(self, '相机', '六号相机没有启动成功')
        self.ui.pushButton.setEnabled(1)
        self.ui.loadcamera_pushButton.setEnabled(0)

    def load_end_step(self):
        self.ui.pushButton.setEnabled(1)
        self.ui.loadcamera_pushButton.setEnabled(0)

    def start_grab(self,cam_id):
        pass
    def takeshot_thread(self):
        """废弃代码"""
        self.thread_move = threading.Thread(target=self.emit_signal, args=())
        self.thread_move.start()

    def show_image_on_label1(self):
        if self.cam1_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show1 = threading.Thread(target=self.make_easy, args=(self.ui.label1_camera, self.cam1, 'CAMERA_1'))
                    # self.thread_show1.start()
                    # self.thread_show1.join()
                    self.make_easy(self.ui.label1_camera, self.cam1, 'CAMERA_1')
                else:
                    self.ui.label1_camera.clear()
            except:
                print('cam1 error')

    def show_image_on_label2(self):
        if self.cam2_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show2 = threading.Thread(target=self.make_easy, args=(self.ui.label2_camera, self.cam2,'CAMERA_2'))
                    # self.thread_show2.start()
                    # self.thread_show2.join()
                    self.make_easy(self.ui.label2_camera, self.cam2,'CAMERA_2')
                else:
                    self.ui.label2_camera.clear()
            except:
                print('cam2 error')

    def show_image_on_label3(self):
        if self.cam3_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show3 = threading.Thread(target=self.make_easy, args=(self.ui.label3_camera, self.cam3,'CAMERA_3'))
                    # self.thread_show3.start()
                    # self.thread_show3.join()
                    self.make_easy(self.ui.label3_camera, self.cam3,'CAMERA_3')
                else:
                    self.ui.label3_camera.clear()
            except:
                print('cam3 error')

    def show_image_on_label4(self):
        if self.cam4_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show4 = threading.Thread(target=self.make_easy, args=(self.ui.label4_camera, self.cam4,'CAMERA_4'))
                    # self.thread_show4.start()
                    # self.thread_show4.join()
                    self.make_easy(self.ui.label4_camera, self.cam4,'CAMERA_4')
                else:
                    self.ui.label4_camera.clear()
            except:
                print('cam4 error')

    def show_image_on_label5(self):
        if self.cam5_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show5 = threading.Thread(target=self.make_easy, args=(self.ui.label5_camera, self.cam5,'CAMERA_5'))
                    # self.thread_show5.start()
                    # self.thread_show5.join()
                    self.make_easy(self.ui.label5_camera, self.cam5,'CAMERA_5')
                else:
                    self.ui.label5_camera.clear()
            except:
                print('cam5 error')

    def show_image_on_label6(self):
        if self.cam6_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show6 = threading.Thread(target=self.make_easy, args=(self.ui.label6_camera, self.cam6,'CAMERA_6'))
                    # self.thread_show6.start()
                    # self.thread_show6.join()
                    self.make_easy(self.ui.label6_camera, self.cam6,'CAMERA_6')
                else:
                    self.ui.label6_camera.clear()
            except:
                print('cam6 error')

    def show_image_on_label(self):
        if self.cam1_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show1 = threading.Thread(target=self.make_easy, args=(self.ui.label1_camera, self.cam1, 'CAMERA_1'))
                    # self.thread_show1.start()
                    # self.thread_show1.join()
                    self.make_easy(self.ui.label1_camera, self.cam1, 'CAMERA_1')
                else:
                    self.ui.label1_camera.clear()
            except:
                print('cam1 error')

        if self.cam2_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show2 = threading.Thread(target=self.make_easy, args=(self.ui.label2_camera, self.cam2,'CAMERA_2'))
                    # self.thread_show2.start()
                    # self.thread_show2.join()
                    self.make_easy(self.ui.label2_camera, self.cam2,'CAMERA_2')
                else:
                    self.ui.label2_camera.clear()
            except:
                print('cam2 error')

        if self.cam3_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show3 = threading.Thread(target=self.make_easy, args=(self.ui.label3_camera, self.cam3,'CAMERA_3'))
                    # self.thread_show3.start()
                    # self.thread_show3.join()
                    self.make_easy(self.ui.label3_camera, self.cam3,'CAMERA_3')
                else:
                    self.ui.label3_camera.clear()
            except:
                print('cam3 error')

        if self.cam4_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show4 = threading.Thread(target=self.make_easy, args=(self.ui.label4_camera, self.cam4,'CAMERA_4'))
                    # self.thread_show4.start()
                    # self.thread_show4.join()
                    self.make_easy(self.ui.label4_camera, self.cam4,'CAMERA_4')
                else:
                    self.ui.label4_camera.clear()
            except:
                print('cam4 error')

        if self.cam5_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show5 = threading.Thread(target=self.make_easy, args=(self.ui.label5_camera, self.cam5,'CAMERA_5'))
                    # self.thread_show5.start()
                    # self.thread_show5.join()
                    self.make_easy(self.ui.label5_camera, self.cam5,'CAMERA_5')
                else:
                    self.ui.label5_camera.clear()
            except:
                print('cam5 error')

        if self.cam6_flag:
            # todo dll给触发
            try:
                if self.stop:
                    # self.thread_show6 = threading.Thread(target=self.make_easy, args=(self.ui.label6_camera, self.cam6,'CAMERA_6'))
                    # self.thread_show6.start()
                    # self.thread_show6.join()
                    self.make_easy(self.ui.label6_camera, self.cam6,'CAMERA_6')
                else:
                    self.ui.label6_camera.clear()
            except:
                print('cam6 error')

    def save_pic(self,image,a):
        time_cur = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
        path = get_save_path()
        path = path + '\\' + a + '\\'
        if not os.path.exists(path):
            os.mkdir(path)
        image_name = path + time_cur + '.jpg'
        cv2.imwrite(image_name,image)

    def make_easy(self, label_id, cam_id,a):
        # label_id.repaint()
        image_from_camera = access_get_image(cam_id, "getoneframetimeout")
        if image_from_camera is not None:
            image_into_net = cv2.resize(image_from_camera, (int(1200), int(960)))
            image_into_net = cv2.cvtColor(image_into_net, cv2.COLOR_BGR2RGB)
            # to do save pic
            try:
                if self.save_mode:
                    self.save_pic(image_into_net, a)
            except:
                pass
            image_into_net = Image.fromarray(image_into_net)

            image_into_net, defect_list = self.yolo.detect_image((image_into_net))
            self.count_defects(defect_list, a)
            self.showresult()
            self.change_color_on_label(defect_list, label_id)
            image_show_on_label = np.array(image_into_net)
            image_show_on_label = self.change_image_size_on_label(
                image_show_on_label)
            image_show_on_label = cv2.cvtColor(image_show_on_label, cv2.COLOR_BGR2RGB)
            image_show_on_label = QImage(image_show_on_label.data,
                                         image_show_on_label.shape[1],
                                         image_show_on_label.shape[0],
                                         QImage.Format_RGB888)
            label_id.setPixmap(QPixmap.fromImage(image_show_on_label))

    def change_color_on_label(self, onelist, label):
        if onelist:
            label.setStyleSheet('background-color: rgb(255, 0, 0)')
        else:
            label.setStyleSheet('background-color: rgb(0, 255, 0)')

    def change_image_size_on_label(self, image):
        #2 是全屏,0是默认打开，不是全屏
        if int(self.windowState()) == 2:
            image = cv2.resize(image, (int(512), int(340)))
        if int(self.windowState()) == 0:
            image = cv2.resize(image, (int(340), int(225)))
        return image

    def closeEvent(self, a0: QCloseEvent) -> None:
        try:
            infoBox = QMessageBox()  ##Message Box that doesn't run
            infoBox.setText("正在关闭相机资源")
            infoBox.setWindowTitle("关闭窗口")
            infoBox.setStandardButtons(QMessageBox.Ok)
            infoBox.button(QMessageBox.Ok).animateClick(3 * 1000) # 3秒自动关闭
            infoBox.exec_()
        except:
            pass
        try:
            close_and_destroy_device(self.cam1)
            close_and_destroy_device(self.cam2)
            close_and_destroy_device(self.cam3)
            close_and_destroy_device(self.cam4)
            close_and_destroy_device(self.cam5)
            close_and_destroy_device(self.cam6)
        except:
            pass

    def emit_signal(self):
        if self.cam1_flag:
            try:
                self.cam1.takeshot()
            except:
                pass
        if self.cam2_flag:
            try:
                self.cam2.takeshot()
            except:
                pass

    def show_image_on_label_old_methed(self):
        """
        Deprecation code
        :return:
        """
        # if self.cam1_flag:
        #     try:
        #         self.ui.label.repaint()
        #         self.image1 = self.cam1.show_thread()
        #         show1 = cv2.resize(self.image1, (int(1200), int(960)))  # 把读到的帧的大小重新设置为 640x480
        #         show1 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)
        #         showImage1 = QImage(show1.data, show1.shape[1], show1.shape[0], QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        #         self.ui.label.setPixmap(QPixmap.fromImage(showImage1))  # 往显示视频的Label里 显示QImage
        #
        #         self.image2_net = Image.fromarray(self.image2)
        #         print(type(self.image2_net))
        #         # self.image2_net = self.yolo.detect_image(self.image2_net)
        #         # self.image2_net = np.array(self.image2_net)
        #         # show1 = cv2.resize(self.image2_net, (int(1200), int(960)))  # 把读到的帧的大小重新设置为 640x480
        #         # show1 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)
        #         # showImage1 = QImage(show1.data, show1.shape[1], show1.shape[0], QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
        #         # self.ui.label.setPixmap(QPixmap.fromImage(showImage1))  # 往显示视频的Label里 显示QImage
        #     except:
        #         print('12')
        if self.cam2_flag:
            if self.stop:
                # todo 获取dll给的触发信号，满足就执行下面
                try:
                    self.ui.label2_camera.repaint()
                    self.image2 = self.cam2.show_thread()
                    show2 = cv2.resize(self.image2, (int(1200), int(960)))  # 把读到的帧的大小重新设置为 640x480
                    show2 = cv2.cvtColor(show2, cv2.COLOR_BGR2RGB)
                    self.image2_net = Image.fromarray(show2)
                    self.image2_net, defect_list = self.yolo.detect_image(self.image2_net)
                    self.count_defects(defect_list)
                    # if self.which_id_find_defection == 1:
                    #     self.ui.statusbar.showMessage('2号相机检测到异常',5000)
                    # else:
                    #     self.ui.statusbar.clearMessage()
                    self.showresult()
                    self.change_color_on_label(defect_list, self.ui.label2_camera)
                    self.image2_net = np.array(self.image2_net)
                    show1 = self.change_image_size_on_label(self.image2_net)
                    show1 = cv2.cvtColor(show1, cv2.COLOR_BGR2RGB)
                    showImage1 = QImage(show1.data, show1.shape[1], show1.shape[0],QImage.Format_RGB888)
                    self.ui.label2_camera.setPixmap(QPixmap.fromImage(showImage1))  # 往显示视频的Label里 显示QImage
                except:
                    print('34')
            else:
                self.ui.label2_camera.clear()


if __name__ == "__main__":
    APP = QApplication(sys.argv)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    LOGWINDOW = MainWindows()
    LOGWINDOW.show()
    sys.exit(APP.exec_())