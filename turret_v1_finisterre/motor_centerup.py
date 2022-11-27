#!/usr/bin/env python

import os

from dynamixel_sdk import *                    # Uses Dynamixel SDK library

# Control table address
ADDR_MX_TORQUE_ENABLE      = 24               # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION      = 30
ADDR_MX_PRESENT_POSITION   = 36

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = 1                 # Dynamixel ID : 1
DXL_ID2                     = 2                 # Dynamixel ID : 1
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = 0           # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 4095            # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
X_DXL_MOVING_STATUS_THRESHOLD = 6                # Dynamixel moving status threshold
Y_DXL_MOVING_STATUS_THRESHOLD = 6                # Dynamixel moving status threshold

# Center:[ID:001] X PresPos:2021 [ID:002] Y PresPos:2863
x_dxl_goal_position = 2021         # X Center Goal position
y_dxl_goal_position = 2863         # Y Center Goal position

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    quit()

# Enable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel has been successfully connected")

# X Write goal position
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID, ADDR_MX_GOAL_POSITION, x_dxl_goal_position)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

# Y Write goal position
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL_ID2, ADDR_MX_GOAL_POSITION, y_dxl_goal_position)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))

while 1:
    # Read present position
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    dxl_present_position2, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL_ID2, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("[ID:%03d] X GoalPos:%03d  PresPos:%03d" % (DXL_ID, x_dxl_goal_position, dxl_present_position))
    print("[ID:%03d] Y GoalPos:%03d  PresPos:%03d" % (DXL_ID2, y_dxl_goal_position, dxl_present_position2))

    xflag, yflag = 0, 0
    if abs(x_dxl_goal_position - dxl_present_position) < X_DXL_MOVING_STATUS_THRESHOLD:
        print("X Hit threshhold")
        xflag = 1
    if abs(y_dxl_goal_position - dxl_present_position2) < Y_DXL_MOVING_STATUS_THRESHOLD:
        print("Y Hit threshhold")
        yflag = 1
    if xflag == 1 & yflag == 1:
        print("Turret is centered up")
        break

# Close port
portHandler.closePort()
