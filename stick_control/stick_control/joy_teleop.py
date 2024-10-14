#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from sensor_msgs.msg import Joy

from geometry_msgs.msg import Twist

import numpy as np

class MinimalPublisher(Node):

	def __init__(self):
		super().__init__('minimal_publisher')
		self.V_cmd = 0.0
		self.omg_cmd = 0.0
		self.Vel_cmd=Twist()
		self.subscription = self.create_subscription(
			Joy,
			'/joy',
			self.joy_cb,
			10)
		self.subscription  # prevent unused variable warning

		self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
		timer_period = 0.5  # seconds
		self.timer = self.create_timer(timer_period, self.timer_callback)
		self.i = 0

	def timer_callback(self):
		print (self.V_cmd, self.omg_cmd)
		self.Vel_cmd.linear.x=self.V_cmd
		self.Vel_cmd.angular.z=self.omg_cmd
		self.publisher_.publish(self.Vel_cmd)
		#self.get_logger().info('Publishing: "%s"' % msg.data)
		
		self.i += 1

	def joy_cb(self, msg):
		self.V_cmd=msg.axes[4]*0.165
		self.omg_cmd=msg.axes[3]*1
		#print(self.V_cmd, self.omg_cmd)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
