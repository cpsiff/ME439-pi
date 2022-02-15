#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Updated 2021-02-18

@author: Peter Adamczyk
"""

#Read Bag File

# set up File parameters: 
bagfilename = 'imu_static.bag'  # FUTURE: Consider adding Argument Parsing ("argparse" module) see https://flaviocopes.com/python-command-line-arguments/
topicnames = ['/imu_mpu6050_raw']  # this must be a list - hence the brackets. 


# the "rosbag" module is the key to unpacking bag files. 
import rosbag

# Set up lists to receive the unpacked ROS data types
topics = []
msgs = []
ts = []

# and more lists to hold a version converted into ordinary Python. 
times = []
As = []    # Accelerations, X Y Z
Ws = []    # Angular Velocities (Omegas), X Y Z

# Unpack the bag file into the lists. 
bag = rosbag.Bag(bagfilename)
for topic, msg, t in bag.read_messages(topics=topicnames):
    # First store all the available info in lists
    topics.append(topic)  # this will have a list of all the topic types of the unpacked messages
    msgs.append(msg)  # this will have the messages themselves.  
    ts.append(t)  # the "to_time" method of the "rospy.Time" class makes this into a Seconds number
    
    # Then make it into regular Python lists of numbers (unpack the structure)
    times.append(t.to_time())
    As.append([msg.linear_acceleration.x,msg.linear_acceleration.y,msg.linear_acceleration.z])
    Ws.append([msg.angular_velocity.x,msg.angular_velocity.y,msg.angular_velocity.z])

bag.close()


# rearrange
import numpy as np
times = np.array(times) - times[0]  # remove the big offset in "ts" by subtracting the first element
As = np.array(As)
Ws = np.array(Ws)

# # Inspect some properties if you like. 
#print(type(ts))
#print(ts.shape)
#print(type(Ws))
#print(Ws.shape)

# Plot the data using matplotlib
from matplotlib import pyplot as plt
plt.figure()
plt.plot(times,Ws)
plt.show()

# Report mean values. Add any other processing you want to do, here.  
print(np.mean(Ws,axis=0))
