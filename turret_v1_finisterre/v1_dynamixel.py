#!/usr/bin/env python
# https://github.com/raspberrypi/picamera2/blob/main/examples/opencv_face_detect_2.py
# https://github.com/UGA-BSAIL/dynamixel-controller/blob/moreJSON/docs.md

from dynio import *
import cv2
from picamera2 import MappedArray, Picamera2, Preview
from picamera2.encoders import H264Encoder

dxl_io = dxl.DynamixelIO('/dev/ttyUSB0', baud_rate=57600)
mx_28_y = dxl_io.new_mx28(1, 1)  # MX-64 protocol 1 with ID 2
mx_28_x = dxl_io.new_mx28(2, 1)  # MX-64 protocol 1 with ID 2

mx_28_y.torque_enable()
mx_28_x.torque_enable()

mx_28_y.set_position(2021)
mx_28_x.set_position(2863)

face_detector = cv2.CascadeClassifier("/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml")


def draw_faces(request):
    with MappedArray(request, "main") as m:
        for f in faces:
            (x, y, w, h) = [c * n // d for c, n, d in zip(f, (w0, h0) * 2, (w1, h1) * 2)]
            cv2.rectangle(m.array, (x, y), (x + w, y + h), (0, 255, 0, 0))

picam2 = Picamera2()
#picam2.start_preview(Preview.QTGL)
config = picam2.create_preview_configuration(main={"size": (640, 480)},
                                      lores={"size": (320, 240), "format": "YUV420"})
picam2.configure(config)

(w0, h0) = picam2.stream_configuration("main")["size"]
(w1, h1) = picam2.stream_configuration("lores")["size"]
s1 = picam2.stream_configuration("lores")["stride"]
faces = []
picam2.post_callback = draw_faces

#encoder = H264Encoder(10000000)
#picam2.start_recording(encoder, "test.h264")
picam2.start()

try:
    while True:
        buffer = picam2.capture_buffer("lores")
        grey = buffer[:s1 * h1].reshape((h1, s1))
        faces = face_detector.detectMultiScale(grey, 1.1, 3)

        for index,(x,y,w,h) in enumerate(faces):
            frame = cv2.rectangle(buffer, (x,y), (x+w,y+h), (255,255,0), 2)

            Xpos = x+(w/2)#calculates the X coordinate of the center of the face.
            Ypos = y+(h/2)#calculates the Y coordinate of the center of the face.
            Zpos = index+1

            print("I see you! At coords:")
            print("X: " + str(Xpos))
            print("Y: " + str(Ypos))

            positiony = mx_28_y.get_position()
            positionx = mx_28_x.get_position()
            angley = mx_28_y.get_angle()
            anglex = mx_28_x.get_angle()

            print("Y pos: " + str(positiony))
            print("X pos: " + str(positionx))
            print("Angle y: " + str(angley))
            print("Angle x: " + str(anglex))

            # Center is x: 127 / y: 127
            # Max is 255 / 255
            # Min is 0 / 0 

            if Xpos >= 190:
                 mx_28_x.set_angle(anglex-4)
                 print("Clockwise")
            elif Xpos <= 130:           #with respect to the center of the frame
                 print("Counter clockwise")
                 mx_28_x.set_angle(anglex+4)
            elif Ypos > 150:
                 mx_28_y.set_angle(angley+6)
                 print("Down")
            elif Ypos < 90:
                 mx_28_y.set_angle(angley-6)
                 print("Up")
            else:
                 print("Locked")
            break
except KeyboardInterrupt:
    print('interrupted!')

picam2.stop_recording()

