#!/usr/bin/env python

import os
from dynamixel_sdk import *
ADDR_MX_TORQUE_ENABLE      = 24
ADDR_MX_GOAL_POSITION      = 30
ADDR_MX_PRESENT_POSITION   = 36
PROTOCOL_VERSION            = 1.0
DXL_ID                      = 1
DXL_ID2                     = 2
BAUDRATE                    = 57600
DEVICENAME                  = '/dev/ttyUSB0'
TORQUE_ENABLE               = 1
TORQUE_DISABLE              = 0
DXL_MINIMUM_POSITION_VALUE  = 0
DXL_MAXIMUM_POSITION_VALUE  = 4095
X_DXL_MOVING_STATUS_THRESHOLD = 6
Y_DXL_MOVING_STATUS_THRESHOLD = 6
x_dxl_goal_position = 2021
y_dxl_goal_position = 2863

portHandler = PortHandler(DEVICENAME)
packetHandler = PacketHandler(PROTOCOL_VERSION)
portHandler.openPort()
portHandler.setBaudRate(BAUDRATE)

def enable_torque(id):
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, id, ADDR_MX_TORQUE_ENABLE, TORQUE_ENABLE)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))
    else:
        print("Dynamixel has been successfully Torque has been enabled")

def write_goal(id, pos):
    dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, id, ADDR_MX_GOAL_POSITION, pos)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

def pos_read(id):
    dxl_present_position, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, id, ADDR_MX_PRESENT_POSITION)
    if dxl_comm_result != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
    elif dxl_error != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error))

    print("[ID:%03d] PresPos:%03d" % (id, dxl_present_position))
    return dxl_present_position

def hit_pos(pos, goal_pos, thresh):
    if abs(goal_pos - pos) < thresh:
        print("Hit threshhold")
        return True

def close_port():
    portHandler.closePort()

def main():
    enable_torque(DXL_ID)
    enable_torque(DXL_ID2)

    write_goal(DXL_ID, x_dxl_goal_position)
    write_goal(DXL_ID2, y_dxl_goal_position)

    while 1:
        x = hit_pos( pos_read(DXL_ID), x_dxl_goal_position, X_DXL_MOVING_STATUS_THRESHOLD)
        y = hit_pos( pos_read(DXL_ID2), y_dxl_goal_position, Y_DXL_MOVING_STATUS_THRESHOLD)

        if ( x and y):
            print("Turret is centered up")
            break
        else:
            if x != True:
                print("X Not at goal: " + str(x_dxl_goal_position) + "instead at: " + str(pos_read(DXL_ID) ))
            if y != True:
                print("Y Not at goal: " + str(y_dxl_goal_position) + "instead at: " + str(pos_read(DXL_ID2) ))

    close_port()

if __name__ == "__main__":
    main()

