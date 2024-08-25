import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from std_srvs.srv import SetBool

import time
#goes straight before wall

class Autodrive(Node):

    def __init__(self):
        super().__init__('Autodrive_node')
        self.counter = 0
        self.srv = self.create_service(SetBool, 'autodrive_service', self.auto_cb)
        self.get_logger().info("Service Server Running...")
        self.drive = True
        self.pub = self.create_publisher(Twist, 'cmd_vel', 10)
        self.sub = self.create_subscription(LaserScan, 'scan', self.sub_cb, 10)
        self.get_logger().info('Autodrive Node Running...')
        self.get_logger().info("Autodrive ON")

    def auto_cb(self, request, response):
        self.get_logger().info('Request Received... ')
        
        if request.data:
            response.success = True
            self.drive = True
            response.message = 'Autodrive ON'
        elif not request.data:
            response.success = True
            self.drive = False
            response.message = 'Autodrive OFF'
        else:
            response.success = False
            response.message = 'Error'
        
        print(request)
        print(response)
        
        return response


    def sub_cb(self, msg):
        if self.drive : 
            if min(msg.ranges[0], msg.ranges[15], msg.ranges[345]) < 0.5:
                self.pub_cb(0.0, 0.2)
                time.sleep(5)
            else:
                self.pub_cb(0.2, 0.0)
        else : 
            self.pub_cb(0.0, 0.0)

    def pub_cb(self, x, y):
        msg = Twist() 
        msg.linear.x = x
        msg.angular.z = y

        self.pub.publish(msg)
        #self.get_logger().info('Published message: ' + str(msg.linear.x)+ str(msg.angular.z))


def main(args=None):
    rclpy.init(args=args)
    node = Autodrive()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard Interrupt')
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()