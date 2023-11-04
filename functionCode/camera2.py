from functionCode.CameraParams_header import *
from functionCode.MvCameraControl_class import *
from functionCode.PixelType_header import *
from functionCode.CameraParams_const import *
import sys
from functionCode.pic_data import Color_numpy, Is_color_data,Is_mono_data, Mono_numpy
import threading
import time
import os


class Camera():
    def __init__(self):
        self.deviceList = MV_CC_DEVICE_INFO_LIST()
        self.tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE
        ret = MvCamera.MV_CC_EnumDevices(self.tlayerType, self.deviceList)
        if ret != 0:
            print("enum devices fail! ret[0x%x]" % ret)
            sys.exit()
        if self.deviceList.nDeviceNum == 0:
            print("find no device!")
            sys.exit()
        print("Find %d devices!" % self.deviceList.nDeviceNum)
        self.b_save_jpg = False
        self.b_save_bmp = False
        self.buf_save_image = None
        # self.st_frame_info = None

    # 创建相机实例并创建句柄,(设置日志路径)
    def creat_camera(self,nConnectionNum):
        """
        :param deviceList:        设备列表
        :param nConnectionNum:    需要连接的设备序号
        :param log:               是否创建日志
        :param log_path:          日志保存路径
        :return:                  相机实例和设备列表
        """
        # 创建相机实例
        cam = MvCamera()
        # 选择设备并创建句柄
        stDeviceList = cast(self.deviceList.pDeviceInfo[int(nConnectionNum)], POINTER(MV_CC_DEVICE_INFO)).contents
        ret = cam.MV_CC_CreateHandleWithoutLog(stDeviceList)
        print(1111)
        if ret != 0:
            print("create handle fail! ret[0x%x]" % ret)
            sys.exit()
        return cam

    def getnumbersofcamera(self):
        """得到相机的数目"""
        return self.deviceList.nDeviceNum

    def To_hex_str(self,num):
        chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        hexStr = ""
        if num < 0:
            num = num + 2**32
        while num >= 16:
            digit = num % 16
            hexStr = chaDic.get(digit, str(digit)) + hexStr
            num //= 16
        hexStr = chaDic.get(num, str(num)) + hexStr
        return hexStr

    def activatecamera(self,cam):
        ret = cam.MV_CC_OpenDevice(MV_ACCESS_Exclusive, 0)
        if ret != 0:
            print('show error', 'open device fail! ret = ' + self.To_hex_str(ret))
            return ret
        stBool = c_bool(False)
        ret = cam.MV_CC_GetBoolValue("AcquisitionFrameRateEnable", byref(stBool))
        if ret != 0:
            print("get acquisition frame rate enable fail! ret[0x%x]" % ret)
        stParam = MVCC_INTVALUE()
        memset(byref(stParam), 0, sizeof(MVCC_INTVALUE))

        ret = cam.MV_CC_GetIntValue("PayloadSize", stParam)
        if ret != 0:
            print("get payload size fail! ret[0x%x]" % ret)
        self.n_payload_size = stParam.nCurValue
        self.buf_cache = (c_ubyte * self.n_payload_size)()
        ret = cam.MV_CC_StartGrabbing()
        # return ret

    def show_thread(self,cam):
        stFrameInfo = MV_FRAME_OUT_INFO_EX()
        img_buff = None
        while True:
            ret = cam.MV_CC_GetOneFrameTimeout(byref(self.buf_cache), self.n_payload_size, stFrameInfo, 1000)
            if ret == 0:
                # 获取到图像的时间开始节点获取到图像的时间开始节点
                self.st_frame_info = stFrameInfo
                # print("get one frame: Width[%d], Height[%d], nFrameNum[%d]" % (
                # self.st_frame_info.nWidth, self.st_frame_info.nHeight, self.st_frame_info.nFrameNum))
                self.n_save_image_size = self.st_frame_info.nWidth * self.st_frame_info.nHeight * 3 + 2048

                if img_buff is None:
                    img_buff = (c_ubyte * self.n_save_image_size)()

                if True == self.b_save_jpg:
                    self.Save_jpg()  # ch:保存Jpg图片 | en:Save Jpg
                if self.buf_save_image is None:
                    self.buf_save_image = (c_ubyte * self.n_save_image_size)()

                stParam = MV_SAVE_IMAGE_PARAM_EX()
                stParam.enImageType = MV_Image_Bmp;  # ch:需要保存的图像类型 | en:Image format to save
                stParam.enPixelType = self.st_frame_info.enPixelType  # ch:相机对应的像素格式 | en:Camera pixel type
                stParam.nWidth = self.st_frame_info.nWidth  # ch:相机对应的宽 | en:Width
                stParam.nHeight = self.st_frame_info.nHeight  # ch:相机对应的高 | en:Height
                stParam.nDataLen = self.st_frame_info.nFrameLen
                stParam.pData = cast(self.buf_cache, POINTER(c_ubyte))
                stParam.pImageBuffer = cast(byref(self.buf_save_image), POINTER(c_ubyte))
                stParam.nBufferSize = self.n_save_image_size  # ch:存储节点的大小 | en:Buffer node size
                stParam.nJpgQuality = 80;  # ch:jpg编码，仅在保存Jpg图像时有效。保存BMP时SDK内忽略该参数
                if True == self.b_save_bmp:
                    self.Save_Bmp()  # ch:保存Bmp图片 | en:Save Bmp
            else:
                continue

            # 转换像素结构体赋值
            stConvertParam = MV_CC_PIXEL_CONVERT_PARAM()
            memset(byref(stConvertParam), 0, sizeof(stConvertParam))
            stConvertParam.nWidth = self.st_frame_info.nWidth
            stConvertParam.nHeight = self.st_frame_info.nHeight
            stConvertParam.pSrcData = self.buf_cache
            stConvertParam.nSrcDataLen = self.st_frame_info.nFrameLen
            stConvertParam.enSrcPixelType = self.st_frame_info.enPixelType

            # Mono8直接显示
            if PixelType_Gvsp_Mono8 == self.st_frame_info.enPixelType:
                numArray = Mono_numpy(self.buf_cache, self.st_frame_info.nWidth,
                                                      self.st_frame_info.nHeight)

            # RGB直接显示
            elif PixelType_Gvsp_RGB8_Packed == self.st_frame_info.enPixelType:
                numArray = Color_numpy(self.buf_cache, self.st_frame_info.nWidth,
                                                       self.st_frame_info.nHeight)

            # 如果是黑白且非Mono8则转为Mono8
            elif True == Is_mono_data(self.st_frame_info.enPixelType):
                nConvertSize = self.st_frame_info.nWidth * self.st_frame_info.nHeight
                stConvertParam.enDstPixelType = PixelType_Gvsp_Mono8
                stConvertParam.pDstBuffer = (c_ubyte * nConvertSize)()
                stConvertParam.nDstBufferSize = nConvertSize
                ret = cam.MV_CC_ConvertPixelType(stConvertParam)
                if ret != 0:
                    print('show error', 'convert pixel fail! ret = ' + self.To_hex_str(ret))
                    continue
                cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, nConvertSize)
                numArray = Mono_numpy(self, img_buff, self.st_frame_info.nWidth,
                                                      self.st_frame_info.nHeight)

            # 如果是彩色且非RGB则转为RGB后显示
            elif True == Is_color_data(self.st_frame_info.enPixelType):
                nConvertSize = self.st_frame_info.nWidth * self.st_frame_info.nHeight * 3
                stConvertParam.enDstPixelType = PixelType_Gvsp_RGB8_Packed
                stConvertParam.pDstBuffer = (c_ubyte * nConvertSize)()
                stConvertParam.nDstBufferSize = nConvertSize
                ret = cam.MV_CC_ConvertPixelType(stConvertParam)
                if ret != 0:
                    print('show error', 'convert pixel fail! ret = ' + self.To_hex_str(ret))
                    continue
                cdll.msvcrt.memcpy(byref(img_buff), stConvertParam.pDstBuffer, nConvertSize)
                numArray = Color_numpy(img_buff, self.st_frame_info.nWidth,
                                                       self.st_frame_info.nHeight)
            return numArray

    def Work_thread(self,cam):
        stFrameInfo = MV_FRAME_OUT_INFO_EX()
        ret = cam.MV_CC_GetOneFrameTimeout(byref(self.buf_cache), self.n_payload_size, stFrameInfo, 1000)
        if ret == 0:
            for i in range(1):
                self.st_frame_info = stFrameInfo
                self.Save_jpg()  # ch:保存Jpg图片 | en:Save Jpg

    def takeshot(self):
        try:
            self.h_thread_handle = threading.Thread(target=Camera.Work_thread, args=(self,))
            self.h_thread_handle.start()
        except:
            print('show error', 'error: unable to start thread')

    def stopgrabimage(self,cam):
        ret = cam.MV_CC_StopGrabbing()
        if ret != 0:
            print("stop grabbing fail! ret[0x%x]" % ret)
            del self.buf_cache
            sys.exit()

    def closedevice(self,cam):
        ret = cam.MV_CC_CloseDevice()
        if ret != 0:
            print("close deivce fail! ret[0x%x]" % ret)
            del self.buf_cache
            sys.exit()

    def destoryhandle(self,cam):
        ret = cam.MV_CC_DestroyHandle()
        if ret != 0:
            print("destroy handle fail! ret[0x%x]" % ret)
            del self.buf_cache
            sys.exit()

    def Save_jpg(self,cam):
        # if(None == self.buf_cache):
        #     return
        # self.buf_save_image = None
        # file_path = str(self.st_frame_info.nFrameNum) + ".jpg"

        # time_now = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f')
        time_now = time.time()
        folder = './pic/'
        file_path = folder + str(time_now) + ".jpg"
        if not os.path.exists(folder):
            os.makedirs(folder)
        self.n_save_image_size = self.st_frame_info.nWidth * self.st_frame_info.nHeight * 3 + 2048
        # if self.buf_save_image is None:
        #     self.buf_save_image = (c_ubyte * self.n_save_image_size)()
        self.buf_save_image = (c_ubyte * self.n_save_image_size)()

        stParam = MV_SAVE_IMAGE_PARAM_EX()
        stParam.enImageType = MV_Image_Jpeg;                                        # ch:需要保存的图像类型 | en:Image format to save
        stParam.enPixelType = self.st_frame_info.enPixelType                               # ch:相机对应的像素格式 | en:Camera pixel type
        stParam.nWidth      = self.st_frame_info.nWidth                                    # ch:相机对应的宽 | en:Width
        stParam.nHeight     = self.st_frame_info.nHeight                                   # ch:相机对应的高 | en:Height
        stParam.nDataLen    = self.st_frame_info.nFrameLen
        stParam.pData       = cast(self.buf_cache, POINTER(c_ubyte))
        stParam.pImageBuffer= cast(byref(self.buf_save_image), POINTER(c_ubyte))
        stParam.nBufferSize = self.n_save_image_size                                 # ch:存储节点的大小 | en:Buffer node size
        stParam.nJpgQuality = 90;                                                    # ch:jpg编码，仅在保存Jpg图像时有效。保存BMP时SDK内忽略该参数
        return_code = cam.MV_CC_SaveImageEx2(stParam)

        if return_code != 0:
            print('show error','save jpg fail! ret = '+self.To_hex_str(return_code))
            self.b_save_jpg = False
            return
        file_open = open(file_path.encode('ascii'), 'wb+')
        img_buff = (c_ubyte * stParam.nImageLen)()
        try:
            cdll.msvcrt.memcpy(byref(img_buff), stParam.pImageBuffer, stParam.nImageLen)
            file_open.write(img_buff)
            self.b_save_jpg = False
            print('show info','save jpg success!')
        except:
            self.b_save_jpg = False
            raise Exception("get one frame failed:%s" % e.message)
        if(None != img_buff):
            del img_buff

    def Save_Bmp(self,cam):
        if(0 == self.buf_cache):
            return
        self.buf_save_image = None
        file_path = str(self.st_frame_info.nFrameNum) + ".bmp"
        self.buf_save_image = self.st_frame_info.nWidth * self.st_frame_info.nHeight * 3 + 2048
        if self.buf_save_image is None:
            self.buf_save_image = (c_ubyte * self.n_save_image_size)()

        stParam = MV_SAVE_IMAGE_PARAM_EX()
        stParam.enImageType = MV_Image_Bmp;                                        # ch:需要保存的图像类型 | en:Image format to save
        stParam.enPixelType = self.st_frame_info.enPixelType                               # ch:相机对应的像素格式 | en:Camera pixel type
        stParam.nWidth      = self.st_frame_info.nWidth                                    # ch:相机对应的宽 | en:Width
        stParam.nHeight     = self.st_frame_info.nHeight                                   # ch:相机对应的高 | en:Height
        stParam.nDataLen    = self.st_frame_info.nFrameLen
        stParam.pData       = cast(self.buf_cache, POINTER(c_ubyte))
        stParam.pImageBuffer =  cast(byref(self.buf_save_image), POINTER(c_ubyte))
        stParam.nBufferSize = self.n_save_image_size                                 # ch:存储节点的大小 | en:Buffer node size
        return_code = cam.MV_CC_SaveImageEx2(stParam)
        if return_code != 0:
            print('show error','save bmp fail! ret = '+self.To_hex_str(return_code))
            self.b_save_bmp = False
            return
        file_open = open(file_path.encode('ascii'), 'wb+')
        img_buff = (c_ubyte * stParam.nImageLen)()
        try:
            cdll.msvcrt.memcpy(byref(img_buff), stParam.pImageBuffer, stParam.nImageLen)
            file_open.write(img_buff)
            self.b_save_bmp = False
            print('show info','save bmp success!')
        except:
            self.b_save_bmp = False
            raise Exception("get one frame failed:%s" % e.message)
        if(None != img_buff):
            del img_buff

    def Get_parameter(self,cam):
        stFloatParam_FrameRate = MVCC_FLOATVALUE()
        memset(byref(stFloatParam_FrameRate), 0, sizeof(MVCC_FLOATVALUE))
        stFloatParam_exposureTime = MVCC_FLOATVALUE()
        memset(byref(stFloatParam_exposureTime), 0, sizeof(MVCC_FLOATVALUE))
        stFloatParam_gain = MVCC_FLOATVALUE()
        memset(byref(stFloatParam_gain), 0, sizeof(MVCC_FLOATVALUE))
        ret = cam.MV_CC_GetFloatValue("AcquisitionFrameRate", stFloatParam_FrameRate)
        if ret != 0:
            print('get acquistion frame rate fail! ret = ' + self.To_hex_str(ret))
        self.frame_rate = stFloatParam_FrameRate.fCurValue
        ret = cam.MV_CC_GetFloatValue("ExposureTime", stFloatParam_exposureTime)
        if ret != 0:
            print('get exposure time fail! ret = ' + self.To_hex_str(ret))
        self.exposure_time = stFloatParam_exposureTime.fCurValue
        ret = cam.MV_CC_GetFloatValue("Gain", stFloatParam_gain)
        if ret != 0:
            print('get gain fail! ret = ' + self.To_hex_str(ret))
        self.gain = stFloatParam_gain.fCurValue
        print('成功得到相机相关参数')



if __name__ == "__main__":
    Cam = Camera()

    camera1 = Cam.creat_camera(0)
    camera2 = Cam.creat_camera(1)
    camera3 = Cam.creat_camera(2)
    camera4 = Cam.creat_camera(3)
    camera5 = Cam.creat_camera(4)
    camera6 = Cam.creat_camera(5)

    Cam.activatecamera(camera1)
    Cam.activatecamera(camera2)
