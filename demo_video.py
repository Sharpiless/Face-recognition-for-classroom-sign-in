import numpy as np
import argparse
import sys
import cv2
import os

from func.facenet import FaceDet

if __name__ == '__main__':

    cap = cv2.VideoCapture('./src.flv')
    det = FaceDet()
    video_width = int(cap.get(3))
    video_height = int(cap.get(4))
    fps = int(cap.get(5))
    # fps = 15
    print(fps)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v') #opencv3.0
    videoWriter = cv2.VideoWriter(
        'dst.mp4', fourcc, fps, (533, 300))

    while True:

        _, frame = cap.read()
        if frame is None:
            break
        # frame = det.detect_and_recognition(frame)
        frame = det.detect_and_recognition(frame)

        cv2.imshow('a', frame)
        videoWriter.write(frame)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    videoWriter.release()
    cv2.destroyAllWindows()
