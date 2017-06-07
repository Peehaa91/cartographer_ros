#!/usr/bin/python

import rospy
from sensor_msgs.msg import PointCloud2
import sensor_msgs.point_cloud2
from std_msgs.msg import Header

scan_ready = False
counter = 0
cloud_msg = PointCloud2()
accumulated_points = []
pub = rospy.Publisher

def scan_callback(data):
    global counter, cloud_msg, accumulated_points, scan_ready, pub,sub
    if scan_ready:
        header = Header()
        header.frame_id = data.header.frame_id
        header.stamp = rospy.get_rostime()
        msg = sensor_msgs.point_cloud2.create_cloud_xyz32(header, accumulated_points)
        print "pub"
        pub.publish(msg)
        accumulated_points = []
        counter = 0
        scan_ready = False
    for point in sensor_msgs.point_cloud2.read_points(data, skip_nans=True):
        accumulated_points.append(point)
    #print len(accumulated_points)
    counter += 1
    if counter == 160:
        scan_ready = True
        #sub.unregister()
        # pub.publish(msg)

        # sensor_msgs.point_cloud2.create_cloud_xyz32()

        # if counter == 0:
        #    cloud_msg = PointCloud2()
        #    cloud_msg.header.frame_id = data.header.frame_id
        #    cloud_msg.
        # for


def talker():
    global frame_id, accumulated_points, scan_ready
    rospy.spin()
    #    rate.sleep()


if __name__ == '__main__':
    try:
        rospy.init_node('scan_accumulator')
        sub = rospy.Subscriber('/vertical_laser_3d', PointCloud2, scan_callback)
        pub = rospy.Publisher('/accumulated_scan', PointCloud2, queue_size=10)
        talker()
    except rospy.ROSInterruptException:
        rospy.logerr("crash")
        pass
