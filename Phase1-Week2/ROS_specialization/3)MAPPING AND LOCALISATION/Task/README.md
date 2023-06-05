# Mapping task

People using ROS-noetic do:

`sudo apt-get install ros-noetic-turtlebot3-*`

People using ROS-kinetic do:

`sudo apt-get install ros-kinetic-turtlebot3-*`

Those using ROS-melodic do:

`sudo apt-get install ros-melodic-turtlebot3-*`

After the installation:

```bash
cd ~
nano .bashrc
```

At the end of your .bashrc file add this line:

```bash
export TURTLEBOT3_MODEL=waffle
```


We have mentioned waffle here. You can use waffle_pi or burger also.

In this task we will cover simultaneous localisation and mapping



Let's start with SLAM:

### SLAM

**SLAM** (Simultaneous Localization and Mapping) is a technique to draw a map by estimating current location in an arbitrary space. 

Now do things step-by-step in different terminals:
```bash
roscore

roslaunch turtlebot3_gazebo turtlebot3_world.launch

roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping

roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch

```
>first launchfile launches a gazebo world and spawn a turtle bot inside it
>second launchfile launches gmapping package it is a famous opensource 2d mapping package This package have node that subscribes on laser data and tf with which it creates a map you can visualise the map on RViz
>.Third launchfile launches teleop package which takes input from keyboard and according publishes on /cmd/vel to control the turtle bot with help of keyboard
```bash
Control Your TurtleBot3!
  ---------------------------
  Moving around:
          w
     a    s    d
          x

  w/x : increase/decrease linear velocity
  a/d : increase/decrease angular velocity
  space key, s : force stop

  CTRL-C to quit

```

> Practice moving around in the environment on your own as you will require it for the assignment.


Now move your bot in entire world and start mapping the world.
It may take a larger time to map the whole world and your PC may also heat up a bit, but don't worry a lot about it.
Sometimes your map will get distorted in between and when you see the terminal, it will show something like this:

 `Scan Matching Failed, using odometry. Likelihood = 0`

This mostly happens when there is some issue with **tf** package. Maneuver your bot multiple times to the entire world until you get a perfect map.
It requires a lot of practice to build a good map, so you may find it difficult to get a good map in first try. 
You can visualize you map in rviz be just launching rviz and selecting topic to /map
![map](https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/14629942916859263.png)
Once your map is built, i.e. you have mapped the entire world, then for saving this map, execute this:

`rosrun map_server map_saver -f ~/map`
> Remember to save your map aftercompleting mapping, else your entire work will be of no use.

# [Submission link ](https://forms.gle/YEZacNvAEBcZq3pAA)
## last date to submit :- 14 june 2023
For now, we are done SLAM basics
