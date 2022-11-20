import cv2
import numpy as np
import os
import serial
import time
from time import sleep
from rpi_python_drv8825.stepper import StepperMotor
import RPi.GPIO as GPIO

# Setup Trigger Relay on GPIO16
triggerPin = 16
GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)

def trigger():
       GPIO.output(triggerPin, GPIO.HIGH)
       sleep(.06)
       GPIO.output(triggerPin, GPIO.LOW)

# Status Setup
font = cv2.FONT_HERSHEY_SIMPLEX
curr_time = time.time()

# Locked Setup
def locked(num,a,b):
     if a < num and num < b:
        trigger()
 
# Pan Motor
enable_pin1 = 12
step_pin1 = 23
dir_pin1 = 24
mode_pins1 = (14, 15, 18)
step_type1 = '1/32'
fullstep_delay1 = .005

# Tilt Motor
enable_pin2 = 12
step_pin2 = 27
dir_pin2 = 22
mode_pins2 = (14, 15, 18)
step_type2 = '1/32'
fullstep_delay2 = .005

face_cascade = cv2.CascadeClassifier('/home/johnc/.local/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_eye.xml')
#smile_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_smile.xml')

# Initialize and start realtime video capture
id = 0
cap = cv2.VideoCapture(0)

# Set properties. Each returns === True on success (i.e. correct resolution)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


# create objects

pan_motor = StepperMotor(enable_pin1, step_pin1, dir_pin1, mode_pins1, step_type1, fullstep_delay1)
tilt_motor = StepperMotor(enable_pin2, step_pin2, dir_pin2, mode_pins2, step_type2, fullstep_delay2)

pan_motor.enable(True) #enable stepper driver
tilt_motor.enable(True) #enable stepper driver

last_time = time.time()
num_frames = 0

while True:
#    ret, img = cap.read()
    ret, orig = cap.read()
    img = cv2.flip(orig,0)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors = 5,
       )
    for index,(x,y,w,h) in enumerate(faces):
        cv2.putText(img, "Not Locked", (x+5,y-5), font, 1, (255,255,255), 2)
        frame = cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0), 2)

        Xpos = x+(w/2)#calculates the X coordinate of the center of the face.
        Ypos = y+(h/2)#calculates the Y coordinate of the center of the face.
        Zpos = index+1

        if Xpos >= 380:
            pan_motor.run(1, False) #clockwise
            sleep(0.005)
        elif Xpos <= 260:           #with respect to the center of the frame
            pan_motor.run(1, True) #counter clockwise
            sleep(0.005)
        elif Ypos > 300:
            tilt_motor.run(1, False) #down
            sleep(0.005)
        elif Ypos < 180:
            tilt_motor.run(1, True) #up
            sleep(0.005)
        else:
            locked(Xpos,260,380)

        break
   

    elapsed_time = curr_time - last_time
    if (elapsed_time > 1.0):
       last_time = curr_time
       num_frames = 0

    #cv2.imshow('camera',img)

#    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
#    if k == 27:
#        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
pan_motor.enable(False)
tilt_motor.enable(False)
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()

