import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class TurtlePoseSubscriber(Node):
    def __init__(self):
        super().__init__('turtle_pose_subscriber')
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.pose_callback,
            10
        )

    def pose_callback(self, msg):
        self.get_logger().info(f'Turtle Position -> x: {msg.x}, y: {msg.y}, theta: {msg.theta}')

def main(args=None):
    rclpy.init(args=args)
    node = TurtlePoseSubscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
