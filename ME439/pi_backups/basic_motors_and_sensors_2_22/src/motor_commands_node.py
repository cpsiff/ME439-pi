#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:03:32 2022

@author: pi
"""

import rospy
from std_msgs.msg import Float32MultiArray # message type

rospy.init_node('motor_commands_node', anonymous=False)


def talker_for_wheel_commands():
    pub_wheel_commands = rospy.Publisher('wheel_commands', Float32MultiArray, queue_size=1)
    
    msg = Float32MultiArray()
    
    while not rospy.is_shutdown():
    
        # read from user
        cmdL, cmdR = [float(x) for x in input("enter cmdL, cmdR in m/s: ").split(",")]
    
        cmdL = cmdL*(1/rospy.get_param('/motor_speed_constant'))
        cmdR = cmdR*(1/rospy.get_param('/motor_speed_constant'))
            
        if(cmdL > rospy.get_param('/max_motor_command')):
            print("Too fast, try again (max is 2.352)")
            
        else:
            # pack the message object with the current data
            msg.data = [int(cmdL), int(cmdR)]
            
            # publish the message
            pub_wheel_commands.publish(msg)


if __name__ == '__main__':
    try:
        talker_for_wheel_commands()
    except rospy.ROSInterruptException:
        pass