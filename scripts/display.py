#!/usr/bin/env python3

import sys

import numpy as np

import cv2 as cv

import roslib
import rospy

from sensor_msgs.msg import CompressedImage

class image_display:

    def __init__(self):
        self.subscriber = rospy.Subscriber("/raspicam_node/image/compressed",
            CompressedImage, self.callback,  queue_size = 1)

    def callback(self, msg):

        np_arr = np.frombuffer(msg.data, np.uint8)
        image_np = cv.imdecode(np_arr, cv.IMREAD_COLOR)
        image_edges = cv.Canny(image_np, 100, 200)
        cv.imshow('cv_img', image_np)
        cv.imshow('edges', image_edges)
        cv.waitKey(1)

def main(args):
    ic = image_display()
    rospy.init_node('image_display', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down ROS Image display module")
    cv.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
