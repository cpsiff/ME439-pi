#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
title: Sensors to Motor Command Node - ME439 Intro to robotics, wisc.edu
Author: Peter Adamczyk 
Updated 2021-02-17

sensors_to_motor_command_node.py
ROS Node to accept commands of "wheel_command_left" and "wheel_command_right" and make the motors run on a robot using the Pololu DRV8835 Raspberry Pi Hat 
"""

import rospy
# "traceback" is a library that lets you track down errors. 
import traceback
# Import the message types we will need
from std_msgs.msg import Int32, Float32MultiArray, Float32

# Set up callable Publishers and messages
# pub_wheel_command_left = rospy.Publisher('/wheel_command_left',Float32,queue_size=1)
# pub_wheel_command_right = rospy.Publisher('/wheel_command_right',Float32,queue_size=1)
pub_wheel_commands = rospy.Publisher('wheel_commands', Float32MultiArray, queue_size=1)


def sensors_to_wheel_speed():
    rospy.init_node('sensors_to_motor_commands_node',anonymous=False)
    
    sub_A0_proc = rospy.Subscriber('/sensors_A0_proc',Float32,A0_proc_to_motor_command)
    
    # prevent the node from exiting
    rospy.spin()
    
    
def A0_proc_to_motor_command(msg_in):
    
    # unpack the message
    A0_proc = msg_in.data
    rospy.loginfo(f"A0_proc {A0_proc}")
    
    #determine the left wheel speed
##### CODE HERE 
    # Here a random example:  Scale wheel command according to the sensor input, with some limits. 
#    wheel_command_left = 4.0*A0_proc
#    if wheel_command_left > 480.:
#        wheel_command_left = 480.
#    if wheel_command_left < 60.:
#        wheel_command_left = 0.
        
#    if(A0_proc > 0.2):
#        wheel_command_left = 200
#    else:
#        wheel_command_left = 0
        
    difference = A0_proc - 0.2
    wheel_command_left = difference*200
    if(wheel_command_left < 0):
        wheel_command_left *= 16
    
##### 
        
    # pack and publish
#    wheel_command_left_msg = Float32()
#    wheel_command_left_msg.data = wheel_command_left
#    pub_wheel_command_left.publish(wheel_command_left_msg)
#    rospy.loginfo("left {0}".format(wheel_command_left_msg.data)) 
    
##### CODE HERE    
    # Dummy code for the right: 
    wheel_command_right = wheel_command_left
#####
    
    # pack and publish
#    wheel_command_right_msg = Float32()
#    wheel_command_right_msg.data = wheel_command_right
#    pub_wheel_command_right.publish(wheel_command_right_msg)
#    rospy.loginfo("right {}".format(wheel_command_right_msg.data))  
    
    msg = Float32MultiArray()
    msg.data = [int(wheel_command_left), int(wheel_command_right)]
    pub_wheel_commands.publish(msg)
    rospy.loginfo(f"left: {wheel_command_left}, right: {wheel_command_right}")
    
# Section to start the execution, with Exception handling.         
if __name__ == "__main__": 
    try: 
        sensors_to_wheel_speed()
    except : 
        traceback.print_exc()   # Print any error to the screen. 
        pass