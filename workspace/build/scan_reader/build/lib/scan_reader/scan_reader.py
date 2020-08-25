import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        qos = rclpy.qos.QoSProfile(depth=10,reliability=2,durability=2,history = 1)
        self.subscription = self.create_subscription(LaserScan,
            '/scan',
            self.listener_callback,
            qos)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print(len(msg.ranges))
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()