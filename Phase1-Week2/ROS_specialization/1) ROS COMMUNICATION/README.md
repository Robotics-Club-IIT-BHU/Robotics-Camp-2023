# ROS specilization
Lets Start out with Linux commands go through the compilation we have made here [LinuxCommands.md](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/linuxcommands.md)

Thats should be all for your Linux Tutorial Now back to topic : )

## ROS Communication
An superior alternative for this tutorial is the follow the official tutorial by [ROS wiki](http://wiki.ros.org/ROS/Tutorials) here Beginner Tutorial till **tutorial 15**. What we present here is just for you to understand Lets Start with the basic ROS package. So do go through it and complete the examples.

# Create package
Follow this [Tutorial](http://wiki.ros.org/ROS/Tutorials/CreatingPackage).
```
user@master: ~/catkin_ws $ create_catkin_pkg demo roscpp rospy tf2

user@master: ~/catkin_ws $ create_catkin_pkg <packageName> <dependencies>
  
--or--
user@master: ~/catkin_ws $ caktin_create_pkg  ## Use this command instead if you get error doing the above
  ```
should create a folder

     ├── catkin_ws
         └── src/
             ├── demo/               ## package
             |    ├── include/demo/  ## Contains header files
             |    ├── src/           ## Contains source files or cpp files
             |    ├── launch/        ## Contains Launch files
             |    ├── package.xml    ## Definition of package
             |    └── CMakeLists.txt ## Definition for building
             |   ...
             └── CMakeLists.txt
After Building these one can also access using ros commands
```
$ roscd demo
$ rosed demo main.launch ## or any file existing in the package
```

### Topics and Services


Basically there are central nodes called **master** that collects all the new messages and distributes them within nodes. Basically **Messages** are feed or reading from sensors or useful information from some device/program called **Nodes**.
**Services** compared to messages just doesnt collect or send to one node but a trasaction of information takes place. Basically it is so that a node asks the other node to do something (could be to solve a mathematical problem, or Move the motors or turn on siren) And after that is completed the other node sends a confirmation or results. This Forward and backward motion of Information is termed as **Request** (one who asks for something) and **Response** (after processing the request).

For understanding them better we recommend you to follow the Tutorial by ROS:

- Nodes [Tutorial](http://wiki.ros.org/ROS/Tutorials/UnderstandingNodes)
- Topics [Tutotial](http://wiki.ros.org/ROS/Tutorials/UnderstandingTopics)
- Services [Tutorial](http://wiki.ros.org/ROS/Tutorials/UnderstandingServicesParams)
These Topics and Services have there own Data type called ```msg``` and ```srv``` to handle the communication effectively and robustly these are similar to your definition of ```struct```
```
// structdef.h
struct {
  int id;
  string name;
  float vals[];
};
```
Similarly

```
## messagedef.msg
int64 id
string name
float64 val[]
```

Same goes for ```srv``` files These messages are sent and recieved inside individual nodes using a mechanism called as **Publisher** which sends message to the **master**, And **Subscriber** which subscribes the message from master in a **Asynchornous** fashion using callbacks For understanding them check out the tutorials (we generally prefer c++ but you can choose to do the tutorials in python).

- Msg and Srv [Tutorial](http://wiki.ros.org/ROS/Tutorials/CreatingMsgAndSrv)
- Publisher and Subscriber [Tutorial](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28c%2B%2B%29) and [Run](http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber)
- Service Server and Client [Tutorial](http://wiki.ros.org/ROS/Tutorials/WritingServiceClient%28c%2B%2B%29) and [Run](http://wiki.ros.org/ROS/Tutorials/ExaminingServiceClient)

# Launch
Basically all your nodes are spawned by executing them but what if there are many nodes to launch we use a set of rules to launch them and using ```roslaunch```

You can directly checkout its implementation here. [Tutorial](http://wiki.ros.org/ROS/Tutorials/UsingRqtconsoleRoslaunch#Using_roslaunch)

<br><br>
# BONUS TASKS

For these tasks, you will be using turtlesim here.
## TASK 1
Using Subscriber and Publisher you need to make the turtle move in a straight line path as shown below.

[simplescreenrecorder-2023-06-03_11.48.00.webm](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/120899038/45203124-ce01-4a36-a509-244943fb0653)

## TASK 2
Using Subscriber and Publisher you need to make the turtle rotate some angle as shown below.

[simplescreenrecorder-2023-06-03_11.47.10.webm](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/120899038/312ba373-f41e-4c99-893d-0236a6eee154)

## TASK 3

This task will be used for evaluation 
* Launch turtle sim package
* create a package in a workspace
* write a publisher node that publishes on /cmd/vel and creates a pattern as shown in image below 


![you have to recreate similar pattern](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/ROS_SIM.png)

You have to submit only task 3, Create a zip file containing video and code for submission
## [Click here to submit](https://forms.gle/YEZacNvAEBcZq3pAA)
### Deadline for submission is 6th JUNE EOD.
