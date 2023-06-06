# Task 3 (Getting comfortable with Gazebo)
#### Install TurtleBot packages


During this Task, you will work with a simulated robot called **TurtleBot**, to apply the concepts of ROS. The following image is a picture of the robot you will work with. It is a differential drive robot, that has a Kinect sensor for environmental mapping, wheel encoders for position estimation.




Open application called **Terminator**, you can install it by running following command in the terminal:  
```bash
sudo apt-get install terminator
```

It's highly recommended to use this application instead of stock Terminal. You can have tabs or split windows into few terminals. To install the required packages, execute the following command.

```bash
sudo apt-get install ros-noetic-turtlebot ros-noetic-turtlebot-apps ros-noetic-turtlebot-interactions ros-noetic-turtlebot-simulator ros-noetic-turtlebot-gazebo -y
```

Just copy and paste it in a terminal.


After the installation is done, check that the simulation works in Gazebo. Execute the following command in a shell terminal.


```bash
roslaunch turtlebot_gazebo turtlebot_world.launch
```


You should get something similar to the following.

![env](https://risc.readthedocs.io/_images/turtlebot-gazebo.png )

#### Move the robot


How can you move the Turtlebot?

The easiest way is by executing an existing ROS program to control the robot. A ROS program is executed by using some special files called **launch files**.
Since a previously-made ROS program already exists that allows you to move the robot using the keyboard, let's launch that ROS program to teleoperate the robot.

Execute in a separate terminal:

`roslaunch turtlebot_teleop keyboard_teleop.launch`

Read the instructions on the screen to know which keys to use to move the robot around, and start moving the robot!


Try it! When you're done, you can <kbd>CTRL</kbd>+<kbd>C</kbd> to stop the execution of the program.
you have to submit zip file of screen recording of you bot being controlled by teleopkey .

Hope you enjoyed playing with your bot you can change the world by changing the world parameter in launch file..



#### What is a launch file ?


We've seen that ROS uses launch files in order to execute programs. when you use a command like roslaunch it just lunches a launch file so you were unknowingly launching a launch file  But... how do they work? Let's have a look.

lets  have a look at a launch file. Open the launch folder inside the ``turtlebot_teleop`` package and check the ``keyboard_teleop.launch`` file.

``` bash

  roscd turtlebot_teleop
  cd launch
  gedit keyboard_teleop.launch

```


You will see:

``` xml
<launch>
    <!-- turtlebot_teleop_key already has its own built in velocity smoother -->
    <node pkg="turtlebot_teleop" type="turtlebot_teleop_key" name="turtlebot_teleop_keyboard"  output="screen">
      <param name="scale_linear" value="0.5" type="double"/>
      <param name="scale_angular" value="1.5" type="double"/>
      <remap from="turtlebot_teleop_keyboard/cmd_vel" to="cmd_vel_mux/input/teleop"/>
    </node>
</launch>
```

In the launch file, you have some extra tags for setting parameters and remaps. For now, don't worry about those tags and focus on the node tag.

All launch files are contained within a ``<launch>`` tag. Inside that tag, you can see a ``<node>`` tag, where we specify the following parameters:

- pkg="``package_name``": Name of the package that contains the code of the ROS program to execute
- type="``python_file_name.py``" : Name of the program file that we want to execute
- name="``node_name``" : Name of the ROS node that will launch our Python file
- output="``type_of_output``" : Through which channel you will print the output of the Python file
