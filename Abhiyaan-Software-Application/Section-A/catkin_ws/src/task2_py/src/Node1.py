#!/usr/bin/python3

### The Publisher Node: Node1

# Import required libraries
import rospy
from std_msgs.msg import String

# The node1() Function
def node1():
	rospy.init_node('Node1', anonymous = True)  # Create & Initialise the ROS Node
	'''
	Node Name: Node1
	anonymous = True: Create a unique id for this Node
	'''

	pub = rospy.Publisher('/team_abhiyaan', String, queue_size = 10)  # Create a Publisher Object
	'''
	Topic: '/team_abhiyaan'
	Datatype: String
	Buffer Size = 10
	'''

	rate = rospy.Rate(1)  # Specify rate of publication: 1Hz 

	# While the ROS Programm is alive/running
	while not rospy.is_shutdown():
		str = 'Team Abhiyaan rocks:'  # Specify message to publish
		rospy.loginfo(str)   # Log ROS message to rosout
		pub.publish(str)  # Publish the ROS message
		rate.sleep()  # Sleep for 1s

# The main function
if __name__ == '__main__':
	try:
		node1()  # Call node1() function
	
	# For invocation of exception for operations that interrupted
	except rospy.ROSinterruptexception:
		rospy.loginfo("Node terminated.")  # Log Termination message to rosout

# References:
# https://www.udemy.com/course/ros-essentials/learn/lecture/22078052#overview
# http://wiki.ros.org/ROS/Tutorials
# https://raw.githubusercontent.com/StevenShiChina/books/master/Programming.Robots.with.ROS.A.Practical.Introduction.to.the.Robot.Operating.System.pdf

	
