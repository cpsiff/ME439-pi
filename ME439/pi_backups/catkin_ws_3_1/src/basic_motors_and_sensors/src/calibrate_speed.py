#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 14:03:32 2022

@author: pi

Node to determine the proper conversion from motor speed signals (-480 to 480)
to actual robot speed
"""

import rospy
import time
from pololu_drv8835_rpi import motors
import matplotlib.pyplot as plt
from std_msgs.msg import Int32

SPEEDS = [480, 360, 240, 120, 0, -120, -240, -360, -480]

rospy.init_node('motor_commands_node', anonymous=False)

left_encoder = 0

def set_left_encoder(msg_in):
    global left_encoder
    left_encoder = msg_in.data

def main():        
    global left_encoder
    sub = rospy.Subscriber('/encoderLeft', Int32, set_left_encoder)
    
    counts_per_sec = []
    for spd in SPEEDS:
        motors.setSpeeds(spd, spd)
        time.sleep(0.5)
        encoder_start = left_encoder
        time.sleep(5)
        encoder_end = left_encoder
        # print("start", encoder_start)
        # print("end", encoder_end)
        
        change = encoder_end - encoder_start
        counts_per_sec.append(change/5)
    
    motors.setSpeeds(0, 0)
    
    print(SPEEDS)
    print(counts_per_sec)
    
    plt.plot(SPEEDS, counts_per_sec)
    plt.show()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        motors.setSpeeds(0, 0)
        pass