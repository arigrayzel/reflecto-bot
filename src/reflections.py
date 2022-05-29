#!/usr/bin/env python

import rospy
import numpy as np
import time
import tf

from geometry_msgs.msg import Point, Quaternion


class ReflectionTargeter(object):
    """Listens for a target and source vector and publishes a unit vector normal to the plane that reflects source onto target"""
    def __init__(self):
        self.source_topic = rospy.get_param("~light_source", "/light_source")
        self.target_topic = rospy.get_param("~target_source", "/target_source")
        self.pub_topic = rospy.get_param("~plane_normal", "/plane_normal")
        
        self.source_sub = rospy.Subscriber(self.source_topic, Point, self.source_callback, queue_size=1) 
        self.target_sub = rospy.Subscriber(self.target_topic, Point, self.target_callback, queue_size=1) 
        self.pub = rospy.Publisher(self.pub_topic, Point, queue_size=1)

        self.source = np.array([0.0,0.0,0.0])
        self.target = np.array([0.0,0.0,0.0])

    def source_callback(self, msg):
        #rospy.logwarn("New source")
        new_source = np.array([msg.x, msg.y, msg.z])
        self.source = new_source/np.linalg.norm(new_source) #ensure normalization
        self.calculate_normal()

    def target_callback(self, msg):
        #rospy.logwarn("New target")
        new_target = np.array([msg.x, msg.y, msg.z])
        self.target = new_target/np.linalg.norm(new_target) #ensure normalization
        self.calculate_normal()

    def calculate_normal(self):
        #rospy.logwarn("New plane normal!")
        diff = self.target-self.source
        norm = -diff/np.linalg.norm(diff)
        msg = Point(norm[0], norm[1], norm[2])
        self.pub.publish(msg)


if __name__=="__main__":
    rospy.init_node("normal_calc")
    rt = ReflectionTargeter()
    rospy.spin()
