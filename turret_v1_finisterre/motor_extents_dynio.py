#!/usr/bin/env python3
# https://github.com/UGA-BSAIL/dynamixel-controller/blob/moreJSON/docs.md

from dynio import *

dxl_io = dxl.DynamixelIO('/dev/ttyUSB0', baud_rate=57600)
mx_28_y = dxl_io.new_mx28(1, 1)  # MX-64 protocol 1 with ID 2
mx_28_x = dxl_io.new_mx28(2, 1)  # MX-64 protocol 1 with ID 2

#mx_28_y.write_control_table("LED", 1)
#mx_28_x.write_control_table("LED", 1)

mx_28_y.torque_disable()
mx_28_x.torque_disable()
#mx_28_y.torque_enable()
#mx_28_x.torque_enable()

while 1:
    positiony = mx_28_y.get_position()
    positionx = mx_28_x.get_position()

    print("Y pos: " + str(positiony))
    print("X pos: " + str(positionx))

    angley = mx_28_y.get_angle()
    currenty = mx_28_y.get_current()

    anglex = mx_28_x.get_angle()
    currentx = mx_28_x.get_current()

    print("Angle y: " + str(angley))
    print("Payload y % " + str(currenty))

    print("Angle x: " + str(anglex))
    print("Payload x % " + str(currentx))

    print("----------------------------------------------------------------")
