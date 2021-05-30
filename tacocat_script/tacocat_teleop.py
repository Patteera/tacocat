#!/usr/bin/env python
import rospy
import sys

#This expresses velocity in free space broken into its linear and angular parts.
from geometry_msgs.msg import Twist 

# Provide instruction on how to use keys to control robot.
usage = """
'W' = Move Forward
'S' = Move Backward
'A' = Revolve Left
'Q' = Turn Left
'D' = Revolve Right
'E' = Turn Right
'x' = Stop
"""

print usage

# Char detector code from https://gist.github.com/jasonrdsouza/1901709
def getchar():
    #Returns a single character from standard input
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def KEY_to_twist():
    twist = Twist()

    ch = getchar()
    if ch.strip() == '': 
        print('bye!')
        return []
    elif ch == 'k':
        sys.exit() #Press k to kill all progress and exit.
    else:
        if ch == 'w':
            twist.linear.x = 0.5
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
        elif ch == 's':
            twist.linear.x = -0.5
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
        elif ch == 'a':
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0.5
        elif ch == 'q':
            twist.linear.x = 0.5
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0.5
        elif ch == 'd':
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = -0.5
        elif ch == 'e':
            twist.linear.x = 0.5
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = -0.5
        elif ch == 'x':
            twist.linear.x = 0
            twist.linear.y = 0
            twist.linear.z = 0
            twist.angular.x = 0
            twist.angular.y = 0
            twist.angular.z = 0
        return twist


#Declares that the node is publishing the topic'cmd_vel', message type 'Twist', queued message limited to 1.
pub = rospy.Publisher('cmd_vel', Twist, queue_size = 1)

if __name__ == '__main__':
    try:
        rospy.init_node('tacocat_teleop', anonymous=True) #Gives the name to this node.

        rate = rospy.Rate(10) # Looping rate of 10hz

        while not rospy.is_shutdown():
            msg = KEY_to_twist()
            if msg is not []: pub.publish(msg)
            rate.sleep()
    except rospy.ROSInterruptException:
        pass