echo "Clearing Errors"
ros2 service call /agv0/axis0/input/clearErrors std_srvs/srv/Trigger
ros2 service call /agv0/axis1/input/clearErrors std_srvs/srv/Trigger
ros2 service call /agv0/axis2/input/clearErrors std_srvs/srv/Trigger
ros2 service call /agv0/axis3/input/clearErrors std_srvs/srv/Trigger

echo "Starting Axes"
ros2 service call /agv0/axis0/input/start std_srvs/srv/Trigger
ros2 service call /agv0/axis1/input/start std_srvs/srv/Trigger
ros2 service call /agv0/axis2/input/start std_srvs/srv/Trigger
ros2 service call /agv0/axis3/input/start std_srvs/srv/Trigger