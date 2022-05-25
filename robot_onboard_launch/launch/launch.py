from launch_ros.substitutions import FindPackageShare
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution, TextSubstitution

deviceName = 'agv0'
canbusInterfaceName = 'can0'
batteryMonitorSerialPortName = 'ttyS0'

odriveCalibrationType = '0'

frontLeftAxisNum = '0'
frontRightAxisNum = '1'
rearLeftAxisNum = '3'
rearRightAxisNum = '2'

wheelBaseWidth = '0.27178'
wheelBaseLength = '0.181356'
wheelRadius = '0.04064'
invertRight = 'True'

def generate_launch_description():
    return LaunchDescription([
    # SocketCAN
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('socketcan'),
                    'launch',
                    'socketcan_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'canbus_interface_name': canbusInterfaceName
            }.items()
        ),
    # ODrive Front Left
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('odrive'),
                    'launch',
                    'odrive_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'canbus_interface_name': canbusInterfaceName,
                'axis_number': frontLeftAxisNum,
                'calibration_type': odriveCalibrationType
            }.items()
        ),
    # ODrive Front Right
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('odrive'),
                    'launch',
                    'odrive_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'canbus_interface_name': canbusInterfaceName,
                'axis_number': frontRightAxisNum,
                'calibration_type': odriveCalibrationType
            }.items()
        ),
    # ODrive Rear Left
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('odrive'),
                    'launch',
                    'odrive_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'canbus_interface_name': canbusInterfaceName,
                'axis_number': rearLeftAxisNum,
                'calibration_type': odriveCalibrationType
            }.items()
        ),
    # ODrive Rear Right
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('odrive'),
                    'launch',
                    'odrive_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'canbus_interface_name': canbusInterfaceName,
                'axis_number': rearRightAxisNum,
                'calibration_type': odriveCalibrationType
            }.items()
        ),
    # Kinematics
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('mecanum_kinematics'),
                    'launch',
                    'kinematic_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'front_left_axis_number': frontLeftAxisNum,
                'front_right_axis_number': frontRightAxisNum,
                'rear_left_axis_number': rearLeftAxisNum,
                'rear_right_axis_number': rearRightAxisNum,
                'wheel_base_width': wheelBaseWidth,
                'wheel_base_length': wheelBaseLength,
                'wheel_radius': wheelRadius,
                'invert_right': invertRight
            }.items()
        ),
    # Battery Monitor
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                PathJoinSubstitution([
                    FindPackageShare('battery_monitor'),
                    'launch',
                    'battery_monitor_launch.py'
                ])
            ]),
            launch_arguments = {
                'device_name': deviceName,
                'serial_port_name': batteryMonitorSerialPortName
            }.items()
        )
    ])