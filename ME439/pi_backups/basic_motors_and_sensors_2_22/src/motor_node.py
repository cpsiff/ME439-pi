#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 13:50:22 2022

@author: pi
"""

import rospy
from std_msgs.msg import Float32 # message type
from pololu_drv8835_rpi import motors, MAX_SPEED # MAX_SPEED is just 480

# actually create the ROS node
# anonymous=False means only one motor node at a time
rospy.init_node('motor_node', anonymous=False)


def listener():
    # subscribe to the wheel_command_left topic
    # 1st argument: topic, 2nd arg: message type, 3rd: callback
    sub = rospy.Subscriber('/wheel_command_left', Float32, set_wheel_command_left)
    
    rospy.spin() # keep the node from exiting


def set_wheel_command_left(msg_in):
    wheel_command_left = int(msg_in.data) # Float32 has a field called data
    motors.motor1.setSpeed(wheel_command_left)
    rospy.loginfo(f"got command{msg_in.data}")


# boot things up, with exception handling
# don't run if being imported (that's what the name = main check does)
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        motors.motor1.setSpeed(0)
        motors.motor2.setSpeed(0)
        
    # just in case it somehow gets past the try block above
    motors.motor1.setSpeed(0)
    motors.motor2.setSpeed(0)