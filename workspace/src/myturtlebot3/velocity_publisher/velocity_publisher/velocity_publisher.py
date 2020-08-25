from geometry_msgs.msg import Twist
import rclpy
import os
from rclpy.qos import QoSProfile

turtlebot3_velocity = Twist()
turtlebot3_velocity.linear.y = 0.0
turtlebot3_velocity.linear.z = 0.0
turtlebot3_velocity.angular.x = 0.0
turtlebot3_velocity.angular.y = 0.0

BURGER_MAX_LIN_VEL = 0.22
BURGER_MAX_ANG_VEL = 2.84

WAFFLE_MAX_LIN_VEL = 0.26
WAFFLE_MAX_ANG_VEL = 1.82


TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']
if TURTLEBOT3_MODEL == 'burger':
    MAX_LIN_VEL = BURGER_MAX_LIN_VEL
    MAX_ANG_VEL = BURGER_MAX_ANG_VEL

elif TURTLEBOT3_MODEL == 'waffle':
    MAX_LIN_VEL = WAFFLE_MAX_LIN_VEL
    MAX_ANG_VEL = WAFFLE_MAX_ANG_VEL

else:
    print('Something is Wrong, check code and enviromental variables such as $TURTLEBOT3_MODEL')





def get_velocities(MAX_LIN_VEL,MAX_ANG_VEL):
    linear_velocity = (input('Insira a velocidade linear -{} ~ {} \n>'.format(MAX_LIN_VEL,MAX_LIN_VEL)))
    angular_velocity = (input('Insira a velocidade angular (-{} ~ {} \n>)'.format(MAX_ANG_VEL, MAX_ANG_VEL)))
    return (float(linear_velocity), float(angular_velocity))

def check_velocities(linear_velocity, angular_velocity):
    if abs(linear_velocity) > MAX_LIN_VEL:
        print('Erro, a velocidade linear inserida não é suportada pelo robô')
        linear_velocity, angular_velocity = get_velocities(MAX_LIN_VEL, MAX_ANG_VEL)
    else:
        linear_velocity = linear_velocity
    
    if abs(angular_velocity) > MAX_ANG_VEL:
        print('Erro, a velocidade linear inserida não é suportada pelo robô')
        linear_velocity, angular_velocity = get_velocities(MAX_LIN_VEL, MAX_ANG_VEL)
    else:
        angular_velocity = angular_velocity
    return (float(linear_velocity), float(angular_velocity))

        
    

def main():
    rclpy.init()
    qos = QoSProfile(depth=10)

    node = rclpy.create_node('velocity_publisher')
    pub = node.create_publisher(Twist,'/cmd_vel',qos)
    while(1):
        linear_velocity, angular_velocity = get_velocities(MAX_LIN_VEL, MAX_ANG_VEL)
        turtlebot3_velocity.linear.x, turtlebot3_velocity.angular.z = check_velocities(linear_velocity,angular_velocity)
        pub.publish(turtlebot3_velocity)

    
    
    

if __name__ == '__main__':
    main()