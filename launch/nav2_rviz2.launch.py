from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')
    home = os.path.expanduser('~')

    return LaunchDescription([
        # Start Nav2
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_bringup_dir, 'launch', 'bringup_launch.py')
            ),
            launch_arguments={
                'use_sim_time': 'true',
                'map': f'{home}/maps/my_maze.yaml',
                'params_file': f'{home}/lidar_maze_ws/src/wall_follower/config/nav2_params.yaml',
                'use_docking': 'false',
                'use_route': 'false',              
            }.items(),
            
        ),

        # Start RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            #arguments=['-d', f'{home}/lidar_maze_ws/src/wall_follower/config/nav2_view.rviz'],
            parameters=[{'use_sim_time': True}],
        ),
    ])