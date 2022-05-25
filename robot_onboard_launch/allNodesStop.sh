#/bin/bash

ros2 lifecycle set /agv0/can0/receiver shutdown
ros2 lifecycle set /agv0/can0/sender shutdown
ros2 lifecycle set /agv0/axis0/odrive shutdown
ros2 lifecycle set /agv0/axis1/odrive shutdown
ros2 lifecycle set /agv0/axis2/odrive shutdown
ros2 lifecycle set /agv0/axis3/odrive shutdown
ros2 lifecycle set /agv0/inverse_kinematics shutdown
ros2 lifecycle set /agv0/forward_kinematics shutdown