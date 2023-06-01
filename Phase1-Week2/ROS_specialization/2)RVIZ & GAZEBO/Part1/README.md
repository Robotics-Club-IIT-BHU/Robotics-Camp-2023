<h2 align="center">RViz</h2>

**Visualisation** is the key which make robotics fun, Generally we want to see what the robot is seeing, how its joints, links are behaving while interacting with environment etc.... so for these purposes ROS has a package RViz(known as ROS Visualiser) to allow us to see and visualise all these things.

It allows us to....
 - See the image from the camera mounted on robot.
 - Visulaise and debug URDFs.
 - Odometry and Mapping of the environment.
 - set Markers
 - visulaise transformations 
 - and so on.......

Before moving further, see these Videos for Rviz Introduction and feel



[Rviz Introduction by The Construct](https://www.youtube.com/watch?v=yLwr5Zhr_t8&t=137s)<br/>
[More indepth usage](https://www.youtube.com/watch?v=6pep5xB4pEU)




Before moving further with RViz, let's first learn about **tf or transforms(transformations)**.

<h2 align="center">tf</h2>

In pybullet camp, you found an example of transformation i.e., **euler2quaternion** or **quaternion2euler**, but robotics is not just limited to it. To learn more about transformations in real world with robotics see [This video from Maryland University](https://www.youtube.com/watch?v=olmAyg_mrdI&list=PLZgpos4wVnCYhf5jsl2HcsCl_Pql6Kigk&index=2&t=837s)(Although this video is on quadrotors but nearly same math applies in all robotics field.)

In ROS, there is a seprate package which handles transformations, but one might be thinking...

<p align="center">
<img width = 500 height=300 src = "https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/ask.jpeg">
</p>

I will leave the answer on [Kostas Danillidis-Proff at University of Pennsylvania](https://www.coursera.org/lecture/robotics-perception/rotations-and-translations-eTSMz)

In the video you can find how different transformations need to be consider just for a single camera. But real robotics applications not just limits to a camera but include sensors like [IMU](https://en.wikipedia.org/wiki/Inertial_measurement_unit), [GPS](https://en.wikipedia.org/wiki/Global_Positioning_System), [LaserScan](https://en.wikipedia.org/wiki/Laser_scanning), [Encoders](https://www.encoder.com/article-what-is-an-encoder), and many more like this can be included, Hence to make all sensor synchronized ROS reduces the overhead of managing transformations differently but made a compact way of handling these through tf package. Additionally, it can be extended for joints, links transformations as well and allows you to view your entire robot urdf and all its parent and child frames using TF_ViewFrames. 

To learn more thoroughly about it Refer [ROS-Wiki/tf](http://wiki.ros.org/tf).

Also you can look about RViz from [ROS-Wiki/RViz](http://wiki.ros.org/rviz)(Although i think it will be hard for some of you to understand it directly from wiki for now..).

Basically it helps you by providing a transformation (both rotation and translational) between two frame of references. 

## Simple examples


- Lets Say you have a overhead camera and you know the position of target and the robot from the cameras point of view But you have to move the robot which has a different coordinate system, Its obvious if we consider to just flip the axises of the camera coordinate from XYZ to ZYX axises we can directly control the robot

<p align ="center">
<img src = "https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/overhead.jpg"><br/>
</p>

basically we did a matrix multiplication or a Rotation of the coordinates to get the Point of references. If you dont understand what a rotation matrix is just imagine it as a extention of your complex number multiplication that rotated a phaser to a desired angle, and to get a better Visualization of what this does then just have a look at the image below.
<p align ="center">
<img src = "https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/rot1.png"><br/>
</p>



- **Complex Scenario** : Now lets consider a complex case where the point of references are not stationary Like in the robot given below lets say we wanted to climb stairs, And we have the coordinates of the stairs from the Center of Mass of the robot, If we have the task to keep only the front most leg on the stairs, We would need the coordinate of the stairs from the frame of reference of the toe, But this time the rotation and translation matrix is not constant like the previous examples as the position of the toe is changing relative to the Center of mass as the joint angles are changing So keeping this in mind we have first compute the forward Kinematics of the toes and then compute the translation and rotation matrix which is very hard considering your system may have multiple joints and multiple end effectors , In all this case the TF package comes in handy
<p align ="center">
<img src = "https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/stoch.png"><br/>
</p>

## HANDS ON

Only seeing something don't make you master in it. so let's try some things by yourselves...

Run below Packages Step by Step to get the flavour of Rviz and tf.

P.S. -> We are not going indepth of the underlying code(As our aim is to give you a headstart on how these are useful and not telling about every knitty-gritty details), if one is willing he/she can go through it for better understanding

 - [Learning Urdf Step by Step](http://wiki.ros.org/urdf/Tutorials) - Although these concepts were taught in pybullet camp but here you will actually going to visulaise it in RViz-ROS. **Just Follow the steps as mentioned there and try to Run locally-> Learning URDF Step by Step Tutorial for first three section till now(Upto- Adding Physical and Collision Properties to a URDF Model).**
   
 - TF from ROS wiki [[1]](http://wiki.ros.org/tf/Tutorials/Introduction%20to%20tf) , [[2]](http://wiki.ros.org/tf/Tutorials/Writing%20a%20tf%20broadcaster%20%28C%2B%2B%29), [[3]](http://wiki.ros.org/tf/Tutorials/Adding%20a%20frame%20%28C%2B%2B%29), [[4]](http://wiki.ros.org/tf/Tutorials/tf%20and%20Time%20%28C%2B%2B%29),, [[5]](http://wiki.ros.org/tf/Tutorials/Time%20travel%20with%20tf%20%28C%2B%2B%29) Go through all these tutorials to get a good understanding of tf
       

## Now you can proceed to attempt <a href="https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/2)RVIZ%20&%20GAZEBO/Task1/README.md"> Task for this part</a>







Now we will discuss a common concern with programming i.e., degugging and how ROS have some awesome tools to address it.

<h2 align="center">RQT</h2>

RQt runs in the same way as a node.


```bash
# start roscore 
~$ roscore
```
```bash
# in another terminal run
-$ rqt
```
A similar window of this type will open
<img src = "../../assests/rqt.png">

RQT have different components varying from viewing node Graphs, logging errors/warnings, plotting variables, viewing images from camera on bot and other things. **We will go through three of them rqt_graph, rqt_plot, rqt_logging one by one**.

### 1. rqt_graph

Rqt graph is a GUI plugin from the Rqt tool suite. With rqt graph you can visualize the ROS graph of your application. On one window you can see all your running nodes, as well as the communication between them. The nodes and topics will be displayed inside their namespace.

**Why using rqt graph**?

When you develop with ROS you usually organize your work into packages and nodes. As your application grows (more sensors, more actuators, more ways to control your robot, …), so does your code base. So, you end up with many nodes and topics, and it might become harder to debug. Using rqt graph will help you mostly for those two things:

 - You’ll get a global overview of your system. This is really useful so you can take better decisions for the future new parts of your application.
 - When you have a bug somewhere due to communication between nodes, you will be able to easily spot the problem. Maybe a node is not correctly connected to another, or there are 2 nodes publishing on a given topic instead of just one, which is why you get some weird values on the subscriber side.
  
<p align = "center">
<img width = 500 height = 200 src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTcjlPVOXaSmC4IDTvmhoGsicCVTpHrrnVbvA&usqp=CAU"><br/>
<b>An example of rqt_graph</b></br>
(Here Red one is the topic connecting publisher and subscriber)
</p>

Follow [this tutorial from Wiki](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics) as it explained very neatly about rqt_graph.

### 2. rqt_plot

Yes te word describes it right, we can use this to plot the data from the meassage on a particular topic. 
For example below plot describes the x and y coordination of a bot varies with time.

<p align="center">
<img width = 600 height = 400 src = "https://www.programmersought.com/images/386/21b565afa70361bca5cca940ba31e8ca.png">
</p>

**Why it is used**?
 - It can be used to see the values of a variable and compare it with theoretical ones.
 - Can be used to compare the values coming from sensor and your estimation of that value.
 - And more importantly it allows you to argue about the behaviour of your robots in real time and can allow us to identify any errors(if present).

We can provide you with a demonstration of rqt_plot using turtlesim package available in ROS, but [this article](https://roboticsbackend.com/rqt-plot-easily-debug-ros-topics/) has presented in an intutive way and reduces our headache :sweat_smile:

### 3. rqt_logger

Firstly follow this [ROS-wiki Article](http://wiki.ros.org/ROS/Tutorials/UsingRqtconsoleRoslaunch), then we will move forward.

what it does -
 - It allows to view message in descriptive way
 - can allow us to view each node is properly functioning or not?
 - hence you don't need to run  ```rostopic echo <topic-name>``` to view meassafe puclished to each topic seprately and allows smooth debugging.

## Its Getting Boring ???

    
Well i know it is but you are now done with boring theory and can jump on using these things with your own robot!!!! 
</p>
From now we expect you to discuss with a senior on what robot you would be using to complete the further content as we would like you to have  a good learning experience at the end. We would be only showing example of code snippets and you can directly apply them on your robot, as ros doesnt make any assumptions of your robot and helps to generalize the code.


For Now we are using a simple 2R robot to demonstrate the futher half
![pic](https://camo.githubusercontent.com/98138ae949d015904a90a91fb03cd415d1195d624a146033169048b218850cbe/687474703a2f2f692e696d6775722e636f6d2f4f6a625a77414b2e676966)

This is from the package [twolink](https://github.com/tanay-bits/twolink) which you can implement with the following commands, similarly you can install any ros packages from github for using them in your project.

```bash
cd catkin_ws/src
git clone https://github.com/tanay-bits/twolink
```

                                           
Now you can proceed to TASK 2



