# import rclpy
# from rclpy.node import Node
# from sensor_msgs.msg import LaserScan
# import numpy as np
# from geometry_msgs.msg import Twist #publishing Twist messages to isaac-sim!


# class CmdVelPublisher(Node): #inherets Nodes functions
#     def __init__(self):
#         super().__init__('cmd_vel_publisher') #calls Nodes constructor with param 'cmd_vel_publisher'
#         self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)
#         timer_period = 0.1  # seconds
#         self.timer = self.create_timer(timer_period, self.timer_callback)

#     def timer_callback(self):
#         msg = Twist()
#         msg.linear.x = 0.3 #m/s
#         msg.angular.z = 0.0 #rad/s
#         self.publisher_.publish(msg)
#         self.get_logger().info('Publishing: "%i"' % msg.linear.x)
    
# def main(args=None):
#     rclpy.init(args=args)

#     cmd_vel_publisher = CmdVelPublisher()
#     rclpy.spin(cmd_vel_publisher)

#     cmd_vel_publisher.destroy_node()
#     rclpy.shutdown() 

# if __name__ == '__main__':
#     main()