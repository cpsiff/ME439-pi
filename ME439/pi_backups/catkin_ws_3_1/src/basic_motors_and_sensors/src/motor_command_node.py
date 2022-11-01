#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:03:32 2022

@author: pi
"""

import rospy
from std_msgs.msg import Float32 # message type

rospy.init_node('motor_command_node', anonymous=False)


def talker_for_wheel_commands():
    pub_wheel_command_left = rospy.Publisher('wheel_command_left', Float32, queue_size=1)
    
    wheel_command_left_msg = Float32()
    
    while not rospy.is_shutdown():
    
        # read from user
        wheel_command_left = int(input("Enter wheel command left (-480 to 480) \n"))
        
        # pack the message object with the current data
        wheel_command_left_msg.data = wheel_command_left
        
        # publish the message
        pub_wheel_command_left.publish(wheel_command_left_msg)


if __name__ == '__main__':
    try:
        talker_for_wheel_commands()
    except rospy.ROSInterruptException:
        pass