#!/usr/bin/env python

import sys
import rospy
import numpy as np
import time
import tf

from geometry_msgs.msg import Point, Quaternion

if __name__=="__main__":
    rospy.init_node("test_publisher")
    source_pub = rospy.Publisher("/light_source", Point, queue_size=1)
    target_pub = rospy.Publisher("/target_source", Point, queue_size=1)
    source = Point(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
    target= Point(float(sys.argv[4]), float(sys.argv[5]), float(sys.argv[6]))
    print(source)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        source_pub.publish(source)
        target_pub.publish(target)
        rate.sleep()
    rospy.spin()
