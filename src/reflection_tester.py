#!/usr/bin/env python

import sys
import rospy
import numpy as np
import time
import utils
import tf

from geometry_msgs.msg import Point, Quaternion

if __name__=="__main__":
    rospy.init_node("source pub")
    rospy.init_node("target pub")
    source_pub = rospy.Publisher("/light_source", Point, queue_size=1)
    target_pub = rospy.Publisher("/target_source", Point, queue_size=1)
    source = Point(sys.argv[1], sys.argv[2], sys.argv[3])
    target = Point(sys.argv[4], sys.argv[5], sys.argv[5])
    source_pub.publish(source)
    target_pub.publish(target)
    rospy.spin()
