from ui.ui_settings import Ui_SettingWindow
from PyQt5.QtWidgets import QMainWindow,QApplication,QMessageBox
from PyQt5.QtGui import QImage,QPixmap
import sys
# import serial
# import serial.tools.list_ports
from functionCode.camera import Camera,get_devices_list
import cv2


class Settings(QMainWindow):
    def __init__(self):
        super(Settings, self).__init__()
        self.ui = Ui_SettingWindow()
        self.ui.setupUi(self)

        self.ui.checkcamera_pushButton.clicked.connect(self.checkCamera)
        self.ui.preview_pushButton.clicked.connect(self.previewCamera)
        self.ui.closePreview_pushButton.clicked.connect(self.closePreviewCamera)
        self.current_port = None


    def checkCamera(self):
        try:
            devices_list = get_devices_list()
            self.cam = Camera(devices_list)
            numbers = self.cam.getnumbersofcamera()
            items = [i for i in range(numbers)]
            items = [str(i) for i in items]
            self.ui.camera_comboBox.addItems(items)
            self.ui.checkcamera_pushButton.setEnabled(False)
        except:
            QMessageBox.about(self,'相机','没有检测到相机，请检查相机是否插入')



    def previewCamera(self):
        # print('windowState', int(self.windowState()))
        try:
            currentCameraIndex = int(self.ui.camera_comboBox.currentText())
            self.cam.activatecamera(currentCameraIndex)
            self.cam_flag = 1
        except:
            self.cam_flag = 0
            QMessageBox.about(self,'相机启动失败','相机启动失败')
        try:
            if self.cam_flag:
                if int(self.windowState()) == 0:
                    width, height = 512,384
                elif int(self.windowState()) == 2:
                    width, height = 640,480
                self.image = self.cam.show_thread()
                show = cv2.resize(self.image, (int(width), int(height)))  # 把读到的帧的大小重新设置为 640x480
                show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
                showImage = QImage(show.data, show.shape[1], show.shape[0], QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
                self.ui.preview_label.setPixmap(QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage
        except:
            QMessageBox.about(self,'相机预览失败','相机预览失败')


    def closePreviewCamera(self):
        try:
            self.cam.closedevice()
            self.ui.preview_label.clear()
        except:
            QMessageBox.about(self,"关闭相机预览","关闭相机预览失败")


if __name__ == "__main__":
    App = QApplication(sys.argv)
    settingWindow = Settings()
    settingWindow.show()
    sys.exit(App.exec_())