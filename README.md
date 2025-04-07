#Terminal1:

ssh ubuntu@192.168.0.229 # Your SSH IP

export TURTLEBOT3_MODEL=burger

ros2 launch turtlebot3_bringup robot.launch.py

#Terminal2:

ssh ubuntu@92.168.0.229 # Your SSH IP

export TURTLEBOT3_MODEL=burger

sudo chmod +rw /dev/input/js0

sudo chmod +rw /dev/input/event0

sudo chmod +rw /dev/input/event0

ros2 eun joy joy_node

#Terminal3:

ssh ubuntu@92.168.0.229

export TURTLEBOT3_MODEL=burger

ros2 run stick_control stick_control


#To find the SSH IP 

ifconfig

inet (***.***.*.***) Your IP Address
 
