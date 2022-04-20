#!/usr/bin/python3

import rospy
import time
import math
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
from turtlesim.msg import Pose

def pose_callback_turtle1(pose_message1):
    global x1, y1, yaw1  
    x1 = pose_message1.x
    y1 = pose_message1.y
    yaw1 = pose_message1.theta

def pose_callback_turtle2(pose_message2):
    global x2, y2, yaw2
    x2 = pose_message2.x
    y2 = pose_message2.y
    yaw2 = pose_message2.theta

def motion(velocity_pubisher_turtle1, velocity_pubisher_turtle2):
    vel_msg_turtle1 = Twist()
    vel_msg_turtle2 = Twist()

    accel_turtle1 = Point()
    accel_turtle2 = Point()

    loop_rate = rospy.Rate(1)
    
    while((x1<10.5) and(y1<10.5) and(x2<10.5) and(y2<10.5)):
        F = G*m1*m2/((x1-x2)**2 + (y1-y2)**2)
        relative_angle = math.atan2(y2-y1,x2-x1)

        accel_turtle1.x = 0 if x1==x2 else math.copysign(1,x2-x1) *(F/m1) *math.cos(relative_angle)
        accel_turtle1.y = 0 if y1==y2 else math.copysign(1,y2-y1) *(F/m1) *math.sin(relative_angle)

        accel_turtle2.x = 0 if x1==x2 else math.copysign(1,x1-x2) *(F/m2) *math.cos(relative_angle)
        accel_turtle1.x = 0 if y1==y2 else math.copysign(1,y1-y2) *(F/m2) *math.sin(relative_angle)

        if((x1==x2) and(y1==y2)):
            vel_msg_turtle1.linear.x = 0
            vel_msg_turtle1.linear.y = 0

            vel_msg_turtle2.linear.x = 0
            vel_msg_turtle2.linear.y = 0

            break

        else:
            vel_msg_turtle1.linear.x += accel_turtle1.x *(0.01)
            vel_msg_turtle1.linear.y += accel_turtle1.y *(0.01)
            vel_msg_turtle1.angular.z = 0.01

            vel_msg_turtle2.linear.x += accel_turtle2.x *(0.01)
            vel_msg_turtle2.linear.y += accel_turtle2.y *(0.01)
            vel_msg_turtle2.angular.z = 0.01

        loop_rate.sleep()

    vel_msg_turtle1.linear.x = 0
    vel_msg_turtle1.linear.y = 0
    vel_msg_turtle1.angular.z = 0

    vel_msg_turtle2.linear.x = 0
    vel_msg_turtle2.linear.y = 0
    vel_msg_turtle2.angular.z = 0

    velocity_pubisher_turtle1.publish(vel_msg_turtle1)
    velocity_pubisher_turtle2.publish(vel_msg_turtle2)
    
def node_newton():
    rospy.init_node('Node_turtle', anonymous = True)

    cmd_vel_topic_turtle1 = '/turtle1/cmd_vel'
    velocity_publisher_turtle1 = rospy.Publisher(cmd_vel_topic_turtle1, Twist, queue_size = 10)

    cmd_vel_topic_turtle2 = '/turtle2/cmd_vel'
    velocity_publisher_turtle2 = rospy.Publisher(cmd_vel_topic_turtle2, Twist, queue_size = 10)

    position_topic_turtle1 = '/turtle1/pose' 
    pose_subscriber_turtle1 = rospy.Subscriber(position_topic_turtle1, Pose, pose_callback_turtle1)

    position_topic_turtle2 = '/turtle2/pose' 
    pose_subscriber_turtle2 = rospy.Subscriber(position_topic_turtle2, Pose, pose_callback_turtle2)

    time.sleep(2)

    global G, m1, m2
    G = 1
    m1 = 1
    m2 = 2

    motion(velocity_publisher_turtle1,velocity_publisher_turtle2)
    rospy.spin()

if __name__ == '__main__':
    try:
        node_newton()
    except rospy.ROSInterruptException:
        rospy.loginfo("Node terminated.")

# References:
# https://www.udemy.com/course/ros-essentials/learn/lecture/22078052#overview
# http://wiki.ros.org/ROS/Tutorials
# https://raw.githubusercontent.com/StevenShiChina/books/master/Programming.Robots.with.ROS.A.Practical.Introduction.to.the.Robot.Operating.System.pdf





