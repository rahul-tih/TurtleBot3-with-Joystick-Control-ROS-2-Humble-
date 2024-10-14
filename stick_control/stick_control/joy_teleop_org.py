#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
import numpy as np




def joy_cb (data):
    global V_cmd, omg_cmd
    V_cmd=data.axes[4]*0.165
    omg_cmd=data.axes[3]*1



def joy_driver():
    global V_cmd, omg_cmd    
    pub_vel = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    V_cmd=0
    omg_cmd=0
    rospy.Subscriber('/joy', Joy, joy_cb)
    rate = rospy.Rate(looprate)
    Vel_cmd=Twist()
    while not rospy.is_shutdown():
        
        Vel_cmd.linear.x=V_cmd
        Vel_cmd.angular.z=omg_cmd
                  
        pub_vel.publish(Vel_cmd) 
        rate.sleep()


if __name__ == '__main__':
    rospy.init_node('joy_teleop', anonymous=True)
    looprate=20
    try:
        joy_driver()
    except rospy.ROSInterruptException:
        pass
