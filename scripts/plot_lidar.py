#!/usr/bin/env python3

import rospy
import cv2
import numpy as np
import math

from sensor_msgs.msg import LaserScan

def callback(data):
    frame = np.zeros((500, 500,3), np.uint8)
    angle = data.angle_min
    for r in data.ranges:
        if r==0:
            r = data.range_max
        x = math.trunc((r * 50.0)*math.cos(angle))
        y = math.trunc((r * 50.0)*math.sin(angle))

        cv2.line(frame,(250, 250),(x+250,-y+250),(255,0,0),2)
        angle = angle + data.angle_increment 
    cv2.circle(frame, (250, 250), 2, (255, 255, 0))
    cv2.imshow('frame',frame)
    cv2.waitKey(1)
    
def listener():
    rospy.init_node('plot_lidar', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException: pass
