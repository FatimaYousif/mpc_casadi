import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped

class Relay(Node):
    def __init__(self):
        super().__init__('odom_to_pose')
        self.pub = self.create_publisher(PoseStamped, '/j100_0857/pose', 10)
        self.create_subscription(Odometry, '/odom', self.cb, 10)

    def cb(self, msg):
        p = PoseStamped()
        p.header = msg.header
        p.pose = msg.pose.pose
        self.pub.publish(p)

rclpy.init()
rclpy.spin(Relay())