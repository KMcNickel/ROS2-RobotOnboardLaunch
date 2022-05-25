#/bin/bash

ros2 lifecycle set /agv0/can0/receiver configure
ros2 lifecycle set /agv0/can0/sender configure
ros2 lifecycle set /agv0/axis0/odrive configure
ros2 lifecycle set /agv0/axis1/odrive configure
ros2 lifecycle set /agv0/axis2/odrive configure
ros2 lifecycle set /agv0/axis3/odrive configure
ros2 lifecycle set /agv0/inverse_kinematics configure
ros2 lifecycle set /agv0/forward_kinematics configure

ros2 lifecycle set /agv0/can0/receiver activate
ros2 lifecycle set /agv0/can0/sender activate
ros2 lifecycle set /agv0/axis0/odrive activate
ros2 lifecycle set /agv0/axis1/odrive activate
ros2 lifecycle set /agv0/axis2/odrive activate
ros2 lifecycle set /agv0/axis3/odrive activate
ros2 lifecycle set /agv0/inverse_kinematics activate
ros2 lifecycle set /agv0/forward_kinematics activate

ros2 service call /agv0/axis0/input/start std_srvs/srv/Trigger
ros2 service call /agv0/axis1/input/start std_srvs/srv/Trigger
ros2 service call /agv0/axis2/input/start std_srvs/srv/Trigger
ros2 service call /agv0/axis3/input/start std_srvs/srv/Trigger