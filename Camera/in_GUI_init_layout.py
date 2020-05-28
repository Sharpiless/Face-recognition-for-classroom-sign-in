# coding:utf-8

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import qtawesome
import cv2


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号

    def write(self, text):
        self.textWritten.emit(str(text))


class Initor_for_btn(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

    def init_bottom_box(self):
        self.bottom_box = QtWidgets.QLabel(self)
        self.bottom_box.setAlignment(Qt.AlignCenter)
        self.bottom_box.setStyleSheet("QLabel{background:black;}"
                                      "QLabel{color:rgb(100,100,100);"
                                      "font-size:15px;"
                                      "font-weight:bold;font-family:宋体;}"
                                      "border-radius: 25px;border: 1px solid black;")
        self.bottom_box.setText("控制台输出")
        self.right_layout.addWidget(self.bottom_box, 9, 0, 1, 9)

    def init_right(self):

        # 原始视频
        self.raw_video = QtWidgets.QLabel(self)
        self.raw_video.setAlignment(Qt.AlignCenter)
        self.raw_video.setText("请选择视频输入")
        self.raw_video.setFixedSize(
            self.video_size[0], self.video_size[1])  # width height
        # self.raw_video.move(290, 20)
        self.raw_video.setStyleSheet("QLabel{background:white;}"
                                     "QLabel{color:rgb(100,100,100);"
                                     "font-size:15px;"
                                     "font-weight:bold;font-family:宋体;}"
                                     "border-radius: 25px;border: 1px solid black;")
        # 检测视频
        self.face_video = QtWidgets.QLabel(self)
        self.face_video.setAlignment(Qt.AlignCenter)
        self.face_video.setText("等待视频检测")
        self.face_video.setFixedSize(
            self.video_size[0], self.video_size[1])  # width height
        self.face_video.setStyleSheet("QLabel{background:white;}"
                                      "QLabel{color:rgb(100,100,100);"
                                      "font-size:15px;"
                                      "font-weight:bold;font-family:宋体;}"
                                      "border-radius: 25px;border: 1px solid black;")

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.right_bar_layout.addWidget(self.raw_video, 0, 0)
        self.right_bar_layout.addWidget(self.face_video, 1, 0)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

    def init_left(self):

        self.left_close = QtWidgets.QPushButton(
            qtawesome.icon('fa.remove', color='white'), '')  # 关闭按钮
        self.left_reset = QtWidgets.QPushButton(
            qtawesome.icon('fa.undo', color='white'), '')  # 刷新
        self.left_mini = QtWidgets.QPushButton(
            qtawesome.icon('fa.minus', color='white'), '')  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("文件")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("摄像头")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("检测")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4 = QtWidgets.QPushButton("帮助")
        self.left_label_4.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(
            qtawesome.icon('fa.film', color='white'), "本地文件")
        self.left_button_1.setObjectName('left_button')
        
        self.left_button_2 = QtWidgets.QPushButton(
            qtawesome.icon('fa.video-camera', color='white'), "打开摄像头")
        self.left_button_2.setObjectName('left_button')
        
        self.left_button_rec = QtWidgets.QPushButton(
            qtawesome.icon('fa.play', color='white'), "开始人脸识别")
        self.left_button_rec.setObjectName('left_button')
        
        self.left_button_6 = QtWidgets.QPushButton(
            qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_6.setObjectName('left_button')
        
        self.left_button_7 = QtWidgets.QPushButton(
            qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_7.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_reset, 0, 1, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 4, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_rec, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_4, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 11, 0, 1, 3)

        self.left_widget.setStyleSheet('''
                QPushButton{border:none;color:white;}
                QPushButton#left_label{
                    border:none;
                    border-bottom:1px solid white;
                    font-size:18px;
                    font-weight:700;
                    font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                }
                QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            ''')

        self.left_close.setFixedSize(32, 32)  # 设置关闭按钮的大小
        self.left_reset.setFixedSize(32, 32)  # 设置按钮大小
        self.left_mini.setFixedSize(32, 32)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:2px;}QPushButton:hover{background:red;}''')
        self.left_reset.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:2px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:2px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet(
            '''QWidget#left_widget{
                    background:black;
                    border-top:1px solid white;
                    border-bottom:1px solid white;
                    border-left:1px solid white;
                    border-top-left-radius:10px;
                    border-bottom-left-radius:10px;
                }'''
        )

    def init_ui(self):
        # self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(
            self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(
            self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件


class Initor_for_event(Initor_for_btn):

    def __init__(self):
        super().__init__()
        self.timer_camera = QTimer()  # 定义定时器

    def init_btn_event(self):

        self.left_mini.clicked.connect(self.showMinimized)

        self.left_button_7.clicked.connect(self.load_url)
        self.left_button_6.clicked.connect(self.message_box6)

        self.left_button_1.clicked.connect(
            self.load_local_video_file)  # 点击选择文件
        self.left_button_2.clicked.connect(self.load_camera_video)  # 加载摄像头

    def load_url(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(
            'https://blog.csdn.net/weixin_44936889'))

    def message_box6(self):
        QMessageBox.about(self, "反馈意见", "1691608003@qq.com")
