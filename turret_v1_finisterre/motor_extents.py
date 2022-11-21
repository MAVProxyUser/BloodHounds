#!/usr/bin/env python
# Based on https://github.com/ROBOTIS-GIT/DynamixelSDK/blob/master/python/tests/protocol1_0/read_write.py
#
# Supporting 3d printed structures
# https://www.thingiverse.com/thing:98266 +  https://www.thingiverse.com/thing:3821230 (melded together by Cherbini)
# https://grabcad.com/library/fr05-s101k-1
# https://grabcad.com/library/dynamixel_28t_servohorn-1 (used temporarily for support in liu of HN07-I101 Set)
# https://github.com/adilzhaniwe/planar-manipulator-CAD/blob/master/base_new.sldprt
# 
from dynamixel_sdk import *                     # Uses Dynamixel SDK library

# Control table address for MX-28AT
# https://github.com/ROBOTIS-GIT/emanual/blob/master/docs/en/dxl/mx/mx-28.md
#

ADDR_MX_TORQUE_ENABLE      = 24                 # Control table address is different in Dynamixel model
ADDR_MX_GOAL_POSITION      = 30
ADDR_MX_PRESENT_POSITION   = 36

# Protocol version
PROTOCOL_VERSION            = 1.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL_ID                      = 1                 # Dynamixel ID : 1
DXL_ID2                     = 2                 # Dynamixel ID : 2
BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"

TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = 0                 # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 4095              # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                # Dynamixel moving status threshold

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    quit()

# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    quit()

# Disable Dynamixel Torque
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL_ID, ADDR_MX_TORQUE_ENABLE, TORQUE_DISABLE)
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

    print("[ID:%03d] PresPos:%03d [ID:%03d] PresPos:%03d" % (DXL_ID, dxl_present_position, DXL_ID2, dxl_present_position2))

# Close port
portHandler.closePort()

