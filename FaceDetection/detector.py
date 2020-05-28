import numpy as np
import argparse
import sys
import cv2
import os
from time import time
import TestFace as face_recognition
from TestFace import face_encodings


class FaceDet(object):
    '''
    人脸检测+识别
    需要识别的脸放到那个faces文件夹里面
    '''

    def __init__(self):

        self.input_size = 300
        self.process_this_frame = True
        self.base_path = './faces'
        self.init_raw_face()

    def init_raw_face(self):

        self.frame = None

        self.known_face_encodings = []
        self.known_face_names = []

        faces = os.listdir(self.base_path)

        for pt in faces:

            name = pt.split('.')[0]
            print('loading {}……'.format(name))
            self.known_face_names.append(name)

            image = face_recognition.load_image_file(
                os.path.join(self.base_path, pt))
            encoding = face_encodings(image)[0]

            self.known_face_encodings.append(encoding)

        self.process_this_frame = True

    def detect_and_recognition(self, im):

        if self.process_this_frame:

            self.frame = self.resize_image(im)
            rgb = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

            face_names = []

            face_loc = face_recognition.face_locations(rgb)
            face_enc = face_recognition.face_encodings(rgb, face_loc)

            for enc in face_enc:
                matches = face_recognition.compare_faces(
                    self.known_face_encodings, enc)
                name = "Unknown"
                face_distances = face_recognition.face_distance(
                    self.known_face_encodings, enc)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
                face_names.append(name)

            for (top, right, bottom, left), name in zip(face_loc, face_names):

                cv2.rectangle(self.frame, (left, top),
                              (right, bottom), (0, 0, 255), 2)
                cv2.rectangle(self.frame, (left, bottom - 10),
                              (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(self.frame, name, (left + 6, bottom - 6),
                            font, 1.0, (255, 255, 255), 1)

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

    # cap = cv2.VideoCapture('../hahhhhhh.mp4')
    cap = cv2.VideoCapture('../video/6.mp4')
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
