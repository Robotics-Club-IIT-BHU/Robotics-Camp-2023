# Task 
## This is an optional amd bonus task adviced to be attempted at last
<h2 align="center">Dynamic Reconfigure</h2>
Dynamic reconfigure is very simple conceptually, there are parameters you would like to change, like PID gains but you dont want to stop the simulation and restart you wanna do it online, this also translates to real world hardware as well where you do not have to stop the robot and open its computer to change the PID gains and run it again.


We would be implementing a small dynamic reconfiguration for the twolink, you may choose to do it for any robot of your choice. you can go through tutorial first and then follow along [Dynamic Reconfigure Tutorial](http://wiki.ros.org/dynamic_reconfigure/Tutorials).

lets write a simple .cfg file
```bash
cd catkin_ws/src/twolink
mkdir config # we prefer to put configs in a seperate folder named config
cd config
touch Simp.cfg
nano Simp.cfg # or open it in any text editor of your choice
```

And put the below code inside it

![code](https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/carbon.png)

The code is self explanatory (else go through the tutorial given above) moving on. Lets add this to the CMakeLists.txt
```bash
# before that if you haven't 
chmod a+x Simp.cfg
# this allows use to run this config
cd ..
nano CMakeLists.txt
```
go to line number 90 where you will find the config section of CMakelist
```
## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#   cfg/DynReconf1.cfg
#   cfg/DynReconf2.cfg
# )
```
like so change it to
```
generate_dynamic_reconfigure_options(
    config/Simp.cfg
)
```
**Dont forget to include the dynamic reconfigure in CMakelists.txt and Package.xml**
for CMakelists.txt
```
find_package(catkin REQUIRED COMPONENTS
  joint_state_publisher
  robot_state_publisher
  roscpp
  rospy
  rviz
  urdf
  dynamic_reconfigure
)
```

for package.xml
```
<run_depend>dynamic_reconfigure</run_depend>
<build_depend>dynamic_reconfigure</build_depend>
```

Now we have to integrate this with the node. Here in twolink the packages are based on python so we are using a dynamic reconfigure of python node, but the logic is the same for cpp.

Open up `twolink/scripts/controller.py`
and add these lines on the top while importing

```python
from dynamic_reconfigure.server import Server
from twolink.config import SimpConfig

rate_ctl = 0.5
pause = False

def callback(config, level):
    global rate_ctl, pause
    rospy.loginfo("""Reconfigure Request: {rate}, {pause}, {size}""".format(**config))
    rate_ctl = config["rate"]
    pause = config["pause"]
    return config
```
and then add the Server definition after declaring the ros node like this

```python
def sender():
    jspub = rospy.Publisher('joint_states', JointState, queue_size=10)

    rospy.init_node('controller_node')
    srv = Server(SimpConfig, callback)
    R = rospy.get_param('~controller_pub_rate')
    rate = rospy.Rate(R)

    T = rospy.get_param('~period')

    cmd = JointState()

    while not rospy.is_shutdown():
        if pause:
            continue
        cmd.header.stamp = rospy.Time.now()
        t = rospy.get_time()

        cmd.name = ['baseHinge', 'interArm']
        cmd.position = desired_thetas(t, T)

        jspub.publish(cmd)

        rate.sleep()
```

This should be all the changes now rebuild and run the diplay.launch file
```bash
cd catkin_ws
catkin build #or catkin_make
roslaunch twolink display.launch
```
On another Terminal
```bash
rosrun rqt_reconfigure rqt_reconfigure
```
<img src="https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/rqt1%20(1).png"/><p align="center">Pause = False</p>

<img src="https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/rqt2.png"/><p align="center">Pause=True</p>

You will be greeted with a gui interface for changing the parameters Experiment to your liking. That all for now now can can proceed to Gazebo
