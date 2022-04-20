#!/usr/bin/python3

### The Subscriber Node: Node2

# Import required libraries
import rospy
from std_msgs.msg import String

# The Subscriber Callback() Function
def callback(msg):
	rospy.loginfo(rospy.get_caller_id() + " %s", msg.data)  # Do the required processing & log ROS message to rosout
	'''
	Basically concatenate the callerid of the message & the message itself
	'''

# The node2() Function
def node2():
	rospy.init_node('Node2', anonymous = True)  # Create & Initialise the ROS Node
	'''
	Node Name: Node1
	anonymous = True: Create a unique id for this Node
	'''

	sub = rospy.Subscriber('/team_abhiyaan', String, callback)  # Create a Subscriber Object
	'''
	Topic: /team_abhiyaan
	Datatype: String
	Callback Function: callback(msg)  # It is invoked asa subscriber receivec a new message 
	'''

	rospy.spin()  # Start listening

# The main function
if __name__ == '__main__':
	try:
		node2()  # Call node2() function
	
	# For invocaiton of exception for operations that interrupted
	except rospy.ROSinterruptexception:
		rospy.loginfo("Node terminated.")  # Log Termination message to rosout

# References:
# https://www.udemy.com/course/ros-essentials/learn/lecture/22078052#overview
# http://wiki.ros.org/ROS/Tutorials
# https://raw.githubusercontent.com/StevenShiChina/books/master/Programming.Robots.with.ROS.A.Practical.Introduction.to.the.Robot.Operating.System.pdf


