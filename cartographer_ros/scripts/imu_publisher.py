#!/usr/bin/python

import rospy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3, Quaternion
import tf
import math
def talker():
    pub = rospy.Publisher('imu', Imu, queue_size=10)
    rospy.init_node('imu_publisher', anonymous=True)
    rate = rospy.Rate(30)
    imu_msg = Imu()
    imu_msg.header.frame_id = "imu_link"

    while not rospy.is_shutdown():
        rate.sleep()
        imu_msg.header.stamp = rospy.get_rostime()
        lin_acc = Vector3()
        lin_acc.x = 0.1

        orientation = Quaternion()
        roll = math.pi/2
        pitch = 0
        yaw = 0
        #orientation = tf.transformations.quaternion_from_euler(roll, pitch, yaw)
        #imu_msg.orientation.x = orientation[0]
        #imu_msg.orientation.y = orientation[1]
        #imu_msg.orientation.z = orientation[2]
        #imu_msg.orientation.w = orientation[3]
        orientation.w = 1
        imu_msg.orientation= orientation
        imu_msg.linear_acceleration = lin_acc
        pub.publish(imu_msg)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        rospy.logerr("crash")
        pass
    
