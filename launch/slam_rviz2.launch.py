from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    slam_toolbox_dir = get_package_share_directory('slam_toolbox')
    home = os.path.expanduser('~')

    slam_params = f'{home}/lidar_maze_ws/src/wall_follower/config/slam_params.yaml'

    return LaunchDescription([
        # Start SLAM Toolbox
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(slam_toolbox_dir, 'launch', 'online_async_launch.py')
            ),
            launch_arguments={
                'use_sim_time': 'true',
                'slam_params_file': slam_params,
            }.items(),
        ),
        #ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -p use_sim_time:=true

        # # Start RViz2
        # Node(
        #     package='rviz2',
        #     executable='rviz2',
        #     name='rviz2',
        #     output='screen',
        #     parameters=[{'use_sim_time': True}],
        
        # ),
    ])