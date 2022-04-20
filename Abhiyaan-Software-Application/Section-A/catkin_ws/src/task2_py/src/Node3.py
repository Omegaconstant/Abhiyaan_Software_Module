#!/usr/bin/python3

### A Subscriber-Publisher Node: Node3

# Import required libraries
import rospy
from std_msgs.msg import String

# The String modification function
def str_operation(str):
	str_list = str.split()  # Split the string based on spaces & store in python list

	# Individually reverse each substrings
	for i in range(len(str_list)):
		str_list[i] = str_list[i][::-1]
	
	return ' '.join(str_list)  # Join all substrings by spaces and return it

# The Subscriber Callback() Function
def callback(msg):
	caller_id = String()  # Initialise variable caller_id as String()
	caller_id.data = rospy.get_caller_id()  # Store the caller id data in it

	rev_str = String()  # Initialise variable rev_str as String()
	rev_str.data = str_operation(msg.data)  # Obtain the required processed message

	rospy.loginfo(caller_id.data + " %s", rev_str.data)  # Log ROS message to rosout
	pub.publish(rev_str.data)  # Publish the ROS message

# The node3() Function
def node3():
	global pub,sub  # Define global variable pub,sub

	rospy.init_node('Node3', anonymous = True)  # Create & Initialise the ROS Node
	'''
	Node Name: Node3
	anonymous = True: Create a unique id for this Node
	'''

	pub = rospy.Publisher('/naayihba_maet', String, queue_size = 10)  # Create a Publisher Object
	'''
	Topic: '/naayihba_maet'
	Datatype: String
	Buffer Size = 10
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
		node3()  # Call node3() function
	
	# For invocaiton of exception for operations that interrupted
	except rospy.ROSinterruptexception:
		rospy.loginfo("Node terminated.")  # Log Termination message to rosout

# References:
# https://www.udemy.com/course/ros-essentials/learn/lecture/22078052#overview
# http://wiki.ros.org/ROS/Tutorials
# https://raw.githubusercontent.com/StevenShiChina/books/master/Programming.Robots.with.ROS.A.Practical.Introduction.to.the.Robot.Operating.System.pdf


