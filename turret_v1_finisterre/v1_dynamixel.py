#!/usr/bin/env python
import cv2

from picamera2 import MappedArray, Picamera2, Preview
from picamera2.encoders import H264Encoder

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
            print("Z: " + str(Zpos))

    #        if Xpos >= 380:
    #            pan_motor.run(1, False) #clockwise
    #            sleep(0.005)
    #        elif Xpos <= 260:           #with respect to the center of the frame
    #            pan_motor.run(1, True) #counter clockwise
    #            sleep(0.005)
    #        elif Ypos > 300:
    #            tilt_motor.run(1, False) #down
    #            sleep(0.005)
    #        elif Ypos < 180:
    #            tilt_motor.run(1, True) #up
    #            sleep(0.005)
    #        else:
    #            locked(Xpos,260,380)
    #        break
except KeyboardInterrupt:
    print('interrupted!')

picam2.stop_recording()

