import rclpy
import time
from rclpy.node import Node
from geometry_msgs.msg import Twist
from rclpy.qos import QoSProfile
from sensor_msgs.msg import LaserScan


class SensorSubscriber(Node):

    def __init__(self):
        super().__init__('Sensor_Subscriber')
        qos = rclpy.qos.QoSProfile(depth=10,reliability=2,durability=2,history = 1)
        self.subscription = self.create_subscription(LaserScan,
            '/scan',
            self.sensor_ranges_callback,
            qos)
        self.subscription  # prevent unused variable warning

    def sensor_ranges_callback(self, sensor):
        print(min(sensor.ranges[10:90]))

        if (min(sensor.ranges[0:10])<0.5) or (min(sensor.ranges[350:360])<0.4):
            print('stoping')
            twist.angular.z = 1.0
            twist.linear.x = 0.0
            velocity_publisher.publisher.publish(twist)
            time.sleep(0.3)
        elif (min(sensor.ranges[45:90])<0.5):
            print('publishing')
            twist.angular.z = -1.0
            velocity_publisher.publisher.publish(twist)
            time.sleep(0.1)

        elif (min(sensor.ranges[270:350])<0.5):
            print('publishing')
            twist.angular.z = 1.0
            velocity_publisher.publisher.publish(twist)
            time.sleep(0.1)
        

            
        twist.angular.z = 0.0
        twist.linear.x = 0.22
        velocity_publisher.publisher.publish(twist)



class VelocityPublisher(Node):
    def __init__(self):
        super().__init__('Velocity_Publisher')
        qos = QoSProfile(depth=10)
        self.publisher = self.create_publisher(Twist,'/cmd_vel',qos)
        self.publisher
       


def main(args=None):
    rclpy.init(args=args)

    sensor_subscriber = SensorSubscriber()
    global velocity_publisher
    velocity_publisher = VelocityPublisher()
    global twist
    twist = Twist()
    twist.linear.x = 0.22
    velocity_publisher.publisher.publish(twist)
    rclpy.spin(sensor_subscriber)


    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    sensor_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()