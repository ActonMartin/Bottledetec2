from yolo import YOLO
from PIL import Image
import numpy as np
from PyQt5.Qt import*
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("深度学习技术驱动的视觉检测软件")
        self.resize(1205, 770)

        self.textname = []
        self.textnumber = []
        self.items_list = []
        # self.openfile_name_image = ''

        self.setup_ui()#画出所有！！！！！！！！！！！

    def setup_ui(self):
        #添加子控件
        label_title = QLabel(self)
        label_title.move(300, 50)
        label_title.setText("欢迎使用视觉检测软件")
        label_title.setStyleSheet("QLabel{color:rgb(0, 0, 0, 255);font-size:50px;font-weight:bold;font-family:宋体;}")

        btn1 = QPushButton(self)
        btn1.setText("开始检测")
        btn2 = QPushButton(self)
        btn2.setText("加载模型")

        btn1.move(300, 150)
        btn2.move(100, 150)
        btn1.resize(180,40)
        btn2.resize(180,40)

        btn1.setStyleSheet("QPushButton{color:rgb(0, 0, 0, 255);font-size:25px;font-weight:bold;font-family:宋体;}")
        btn2.setStyleSheet("QPushButton{color:rgb(0, 0, 0, 255);font-size:25px;font-weight:bold;font-family:宋体;}")


        def select_image():
            print("开始检测")
            self.openfile_name_image, _ = QFileDialog.getOpenFileName(self, "选择照片文件", r"./img/")
            # print(str(self.openfile_name_image)[-3:])
            if self.openfile_name_image[-3:] == 'jpg':
                label_1.setPixmap(QPixmap(str(self.openfile_name_image)).scaled(600,500))

                img = Image.open(str(self.openfile_name_image))
                # img = Image.open('001.jpg')

                img = img.resize((800,600))
                img = img.convert("RGB")
                print(type(img))
                img = self.yolo.detect_image(img)
                print(type(img))
                img = np.array(self.yolo.detect_image(img))
                image = QImage(img[:], img.shape[1], img.shape[0], img.shape[1] * 3, QImage.Format_RGB888)  # pyqt5转换成自己能放的图片格式
                jpg_out = QPixmap(image).scaled(600,500)  # 设置图片大小
                label_2.setPixmap(jpg_out)
            else:
                select_image()
            # cv_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            # cv2.imshow("video", cv_img)
            # cv2.waitKey(0)
        btn1.pressed.connect(select_image)

        def cao2():
            print("模型加载完成")
            self.yolo = YOLO()
            btn2.setText('模型加载完成')
            btn2.setStyleSheet("QPushButton{color:rgb(255, 0, 0, 255);font-size:25px;font-weight:bold;font-family:宋体;}")

        btn2.pressed.connect(cao2)

        label_1 = QLabel(self)
        label_1_1 = QLabel(self)
        label_2 = QLabel(self)
        label_2_2 = QLabel(self)
        ##############################################
        label_1.setFixedSize(600, 500)
        label_2.setFixedSize(600, 500)
        ##############################################
        label_1.move(0, 200)
        label_1_1.move(250, 725)
        label_2.move(605, 200)
        label_2_2.move(605+250, 725)

        label_1_1.setText("检测图片")
        label_2_2.setText("异常结果")

        label_1.setStyleSheet("QLabel{background:white;}")
        label_2.setStyleSheet("QLabel{background:white;}")

        label_1_1.setStyleSheet("QLabel{color:rgb(0, 0, 0, 255);font-size:25px;font-weight:bold;font-family:宋体;}")
        label_2_2.setStyleSheet("QLabel{color:rgb(200,0,200, 255);font-size:25px;font-weight:bold;font-family:宋体;}")

        label_1_1.setAlignment(Qt.AlignCenter)  # 水平居中
        label_2_2.setAlignment(Qt.AlignCenter)  # 水平居中


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())