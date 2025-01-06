#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node('minimal_node')
    node.get_logger().info("Minimal node is running!")
    rclpy.spin(node)

if __name__ == '__main__':
    main()