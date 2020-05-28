# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import qtawesome

from time import sleep, ctime
import numpy as np
import sys
import cv2

from Camera.in_GUI_init_layout import Initor_for_event
from func.facenet import FaceDet

im = None
result = None


class MainUi(Initor_for_event):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setWindowTitle("人脸识别系统")
        self.timer_detector = QTimer()  # 定义定时器
        self.resize(1200, 910)
        self.video_size = (500, 360)
        self.detectFlag = 0  # 初始不显示检测结果
        self.setFixedSize(self.width(), self.height())
        self.init_layout()
        self.init_clik()

    def init_clik(self):

        self.detect_thread = DETECT_Thread()
        self.detect_thread.start()
        self.left_button_rec.clicked.connect(self.init_rec_btn)
        self.left_close.clicked.connect(self.close_all)

    def close_all(self):

        self.detect_thread.running = False
        self.detect_thread.task = None
        self.close()


    def init_rec_btn(self):
        self.detectFlag = 1 - self.detectFlag
        if self.detectFlag:
            self.detect_thread.task = 'rec'
            self.left_button_rec.setText("暂停人脸识别")
            self.left_button_rec.setIcon(
                qtawesome.icon('fa.pause', color='white'))
            self.load_detected_video()
        else:
            self.left_button_rec.setText("开始人脸识别")
            self.left_button_rec.setIcon(
                qtawesome.icon('fa.play', color='white'))
            self.detect_thread.task = None

    def init_layout(self):

        self.init_left()
        self.init_right()
        self.init_bottom_box()
        self.init_btn_event()
        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.main_layout.setSpacing(0)
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    def load_camera_video(self, index=0):

        self.cap = cv2.VideoCapture(index)  # 调用摄像头（一般电脑自带摄像头index为0）
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        if not self.cap.isOpened():
            raise EOFError("未检测到可用摄像头")
        self.timer_camera.start(fps)
        self.timer_camera.timeout.connect(self.openFrame)

    def load_local_video_file(self):

        videoName, _ = QFileDialog.getOpenFileName(
            self, "Open", "", "*.mp4;;*.avi;;All Files(*)")
        if videoName != "":  # 为用户取消
            self.cap = cv2.VideoCapture(videoName)
            fps = int(self.cap.get(cv2.CAP_PROP_FPS))
            self.timer_camera.start(fps)
            self.timer_camera.timeout.connect(self.openFrame)

    def load_detected_video(self):

        self.timer_detector.start(0)
        self.timer_detector.timeout.connect(self.open_Detected_Frame)

    def open_Detected_Frame(self):
        global result
        if self.detectFlag:
            if not result is None:
                detected_frame = cv2.cvtColor(
                    result, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = detected_frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(detected_frame.data,  width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.face_video.width(), self.face_video.height())
                self.face_video.setPixmap(QPixmap.fromImage(q_image))
        else:
            self.timer_detector.stop()   # 停止计时器

    def openFrame(self):
        global im
        if self.cap.isOpened():
            ret, im = self.cap.read()
            if ret:
                frame = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
                height, width, bytesPerComponent = frame.shape
                bytesPerLine = bytesPerComponent * width
                q_image = QImage(frame.data,  width, height, bytesPerLine,
                                 QImage.Format_RGB888).scaled(self.raw_video.width(), self.raw_video.height())
                self.raw_video.setPixmap(QPixmap.fromImage(q_image))
            else:
                im = None
                self.cap.release()
                self.timer_camera.stop()   # 停止计时器


class DETECT_Thread(QThread):

    def __init__(self):
        super().__init__()
        self.task = None
        self.detector = FaceDet()
        self.running = True

    def run(self):
        global im, result
        while True:
            if not self.running:
                return
            if not im is None:
                if self.task == 'rec':
                    result = self.detector.detect_and_recognition(im)
                elif self.task == 'det':
                    result = self.detector.detect_only(im)
                else:
                    result = None
                    sleep(0.2)
        return
