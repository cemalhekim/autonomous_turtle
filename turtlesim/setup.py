from setuptools import setup

package_name = 'turtlesim'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/ros2/share', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your.email@example.com',
    description='A simple robot simulation in ROS 2',
    license='License',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pose_subscribe = turtlesim.pose_subscribe:main',
        ],
    },
)
