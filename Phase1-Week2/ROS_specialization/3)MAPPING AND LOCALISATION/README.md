
# Mapping 

***To understand this concept lets assume I drop you in a city of TYPE 4 civilisation on another planet and I order you to reach nearest launch pad for airlift will you be able to do it ?
Obviously no..
Because the city is completely unknown to you, You neither know where you are in the city nor where is the launch pad. Similar is the case of an autonomous bot. This is when mapping and Localisation comes into play
Mapping is when a robot explores its surroundings and creates a detailed map, just like drawing a blueprint of a house or a city. It notes down all the walls, furniture, and objects it encounters, so it knows where everything is.
this is done with the help of sensors like lidar, depth camera etc.***

> In the camp we have used gmapping since it is easiest and beginner friendly but it maps the environment in 2 dimensions therefore it is not widely used in realworld application

>Mapping techniques like Rtab mapping, Octomapping, ORB SLAM etc are much more advanced but also consumes a lot of resources.

![RTAB mapping](https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/rtab.jpg)
<p align="center">  RTAB mapping  </p>

# Localisation

***Localization is like a robot's ability to know where it is on that map. Just as we use landmarks and signs to figure out our location, a robot uses sensors to determine its position on the map it created. It's like saying, "I'm right here on the map!"
Guess which sensors are usefull for localisation , YES GPS the most obvious. We can also localise our bot by using vision (camera data) for this we place fiducial markers in our environment and the camera finds out its position w.r.t to markers in the environment thus localising it.
An inertial measurement unit consists of several sensors like accelerometer, Gyroscope, Barometer which estimates the change in position from initial position. If initially we know where our bot was on the map we can use data from IMU To estimate its current position but this method is generally not used because the error in position keeps on increasing with time.
We can also fuse data from all the sources to get the data as accurate as possible using  Kalman filters whose algorithm has already been discussed. In all cases you need a map to localise on unless you are implementing SLAM (Simultaneously Localising and Mapping) ***

__SLAM is when a robot does mapping and localization at the same time. It's like exploring a new place while creating a map and constantly figuring out where you are as you go. The robot uses sensors to detect its surroundings, build a map, and update its location on that map in real-time.__

![Localisation](https://github.com/panchal-harsh/Robotics-Camp-2023/blob/main/Phase1-Week2/ROS_specialization/images/WhatsApp%20Image%202023-06-01%20at%2015.54.38.jpeg)
<p align="center">  Localisation using fiducial markers  </p>
