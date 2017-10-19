#!/usr/bin/python

import rospy
from sensor_msgs.msg import Imu
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import glob
import re
import itertools
import numpy
from mpl_toolkits.mplot3d import Axes3D

from geometry_msgs.msg import Vector3, Quaternion
import tf
import math
import numpy
counter = 0
point_x = []
point_y = []
point_z = []
last_time = 0
t = []
t.append(0)
def plot():
    fig = plt.figure()

 #   plt.plot(point_x, point_y, point_z)
    plt.plot(t, point_x, 'ro')
    plt.plot(t, point_y, 'ro')
    plt.plot(t, point_z, 'ro')
    plt.show()
def callback(msg):
    global point_x, point_y, point_z, counter, t, last_time
    if counter != 0:
        t.append(t[len(t)-1] + (msg.header.stamp - last_time).to_sec())
    last_time = msg.header.stamp
    point_x.append(msg.linear_acceleration.x)
    point_y.append(msg.linear_acceleration.y)
    point_z.append(msg.linear_acceleration.z)
    if counter == 100:
        plot()
    counter = counter + 1

def receiver():
    rospy.init_node('imu_check', anonymous=True)
    sub = rospy.Subscriber('imu', Imu, callback,None, 1000)
    
    rospy.spin()

if __name__ == '__main__':
    try:
        receiver()
    except rospy.ROSInterruptException:
        rospy.logerr("crash")
        pass
