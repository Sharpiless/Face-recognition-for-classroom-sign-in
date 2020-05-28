import numpy as np
import sys
import cv2
import os
import FaceDetection.TestFace as face_recognition
from FaceDetection.TestFace import face_encodings

from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from time import localtime
fontC = ImageFont.truetype('platech.ttf', 16, 0)


class FaceDet(object):
    '''
    人脸检测+识别
    需要识别的脸放到那个faces文件夹里面
    '''

    def __init__(self):

        self.input_size = 300  # 输入大小
        self.process_this_frame = True  # 隔帧检测的bool变量
        self.base_path = './faces'  # 人脸文件夹
        self.init_raw_face()  # 初始化操作（加载文件夹中人脸）
        self.current_name = 'WTF'

    def init_raw_face(self):

        self.frame = None

        self.known_face_encodings = []  # 人脸编码
        self.known_face_names = []  # 人脸姓名

        faces = os.listdir(self.base_path)

        for name in faces:
            tmp = os.path.join(self.base_path, name)
            for pt in os.listdir(tmp):
                print('loading {}……'.format(name))
                self.known_face_names.append(name)

                image = face_recognition.load_image_file(
                    os.path.join(tmp, pt))  # 人脸检测
                encoding = face_encodings(image)[0]  # 人脸编码

                self.known_face_encodings.append(encoding)

        self.process_this_frame = True

    def get_time(self, name):

        out = '\n{}年 {}月 {}日\n时间：{}\n识别身份：{}\n签到成功！'
        t = localtime()
        out = out.format(
            t.tm_year, t.tm_mon, t.tm_mday,
            str(t.tm_hour)+':'+str(t.tm_min),
            name
        )

        return out

    def drawTest(self, image, addText, x1, y1):

        img = Image.fromarray(image)
        draw = ImageDraw.Draw(img)
        draw.text((x1, y1),
                  addText.encode("utf-8").decode("utf-8"),
                  (255, 255, 255), font=fontC)
        imagex = np.array(img)

        return imagex

    def detect_and_recognition(self, im):

        if self.process_this_frame:

            self.frame = self.resize_image(im)
            rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            face_names = []

            face_loc = face_recognition.face_locations(rgb)[:1]
            face_enc = face_recognition.face_encodings(rgb, face_loc)[
                :1]  # 人脸编码

            for enc in face_enc:
                matches = face_recognition.compare_faces(
                    self.known_face_encodings, enc)  # 计算人脸匹配度
                name = "Unknown"
                face_distances = face_recognition.face_distance(
                    self.known_face_encodings, enc)  # 计算特征向量距离
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_loc, face_names):

                if name == 'Unknown':
                    color = (0, 0, 255)
                else:
                    color = (0, 255, 0)

                cv2.rectangle(self.frame, (left, top),
                              (right, bottom), color, 2)
                cv2.rectangle(self.frame, (left, bottom - 10),
                              (right, bottom), color, cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                text = name.replace('_', ' ')

                if not name == 'Unknown' and name == self.current_name:
                    self.frame = self.drawTest(
                        self.frame, self.get_time(text), 0, 4)

                else:
                    cv2.putText(self.frame, text, (left + 6, bottom - 6),
                                font, 0.7, (255, 255, 255), 2)

                self.current_name = name

        self.process_this_frame = not self.process_this_frame

        return self.frame

    def resize_image(self, image):

        image_shape = image.shape

        size_min = np.min(image_shape[:2])
        size_max = np.max(image_shape[:2])

        min_size = self.input_size

        scale = float(min_size) / float(size_min)

        image = cv2.resize(image, dsize=(0, 0), fx=scale, fy=scale)

        return image


if __name__ == '__main__':

    cap = cv2.VideoCapture('../kun.mp4')
    det = FaceDet()
    video_width = int(cap.get(3))
    video_height = int(cap.get(4))
    fps = int(cap.get(5))
    # fps = 15
    print(fps)
    # fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #opencv3.0
    # videoWriter = cv2.VideoWriter(
    #     'detected.mp4', fourcc, fps, (542, 300))

    while True:

        _, frame = cap.read()
        if frame is None:
            break
        frame = det.detect_and_recognition(frame)
        cv2.imshow('a', frame)
        # videoWriter.write(im)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    # videoWriter.release()
    cv2.destroyAllWindows()
