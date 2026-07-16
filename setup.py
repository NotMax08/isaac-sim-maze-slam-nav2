from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'wall_follower'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/nav2_rviz2.launch.py',   
            'launch/slam_rviz2.launch.py', 
            #'config/nav2_view.rviz',
        ]),
    ],

    #ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p use_sim_time:=true
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='notmax',
    maintainer_email='maxyuan081205@gmail.com',
    description='Maze navigator w/ path following and lidar localization',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    }, 
    # entry_points={
    #     'console_scripts': [
    #         'cmd_vel_publisher = wall_follower.cmd_vel_publisher:main',
    #         'lidar_echo = wall_follower.lidar_echo:main',
    #         'maze_navigator = wall_follower.maze_navigator:main',
    #     ],
    # },
)
