#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move():
    rospy.init_node('move_robot', anonymous=True)
    velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()
    rate = rospy.Rate(10) # 10hz

    linearSpeed = 0.0 	# m/s
    angularSpeed = 0.0	# rad/s
    seconds = 1.0

    vel_msg.linear.x = linearSpeed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = angularSpeed

    while not rospy.is_shutdown():

        t = rospy.Time.now().to_sec()
        tlimit = t + seconds

        while(t < tlimit):
            velocity_publisher.publish(vel_msg)
            rate.sleep()
            t = rospy.Time.now().to_sec()

        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException: pass
