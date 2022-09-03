echo "Stopping Axes"
ros2 service call /agv0/axis0/input/shutdown std_srvs/srv/Trigger
ros2 service call /agv0/axis1/input/shutdown std_srvs/srv/Trigger
ros2 service call /agv0/axis2/input/shutdown std_srvs/srv/Trigger
ros2 service call /agv0/axis3/input/shutdown std_srvs/srv/Trigger
