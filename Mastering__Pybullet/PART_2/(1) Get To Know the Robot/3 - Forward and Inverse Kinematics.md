# Forward and Inverse Kinematics
<br>
<p align="center">
  <img width=300 src="cheems.png">
  <br><i>Remember I told you that physics will haunt you forever!!</i>
  </p>

#### So, here we go back to our dear kinematics. But you need not worry, because this is not the horrible version of kinematics that you learnt in your earlier classes. See, we will stick to the same definition that "kinematics deals with motion of the bodies without worrying about its cause", but here the focus will be on the position of the links and the velocities of the joints. You have learnt how to control the joints, but if you have some desired task in your mind, then what should be the commands given to the various links. Although forces and torques are responsible for such a motion, but still sticking to the pure kinematics definition is a good idea...
#### The kinematics Problem that we are interested in...
So, by Kinematics what we mean is a way to transform from the robot space system to the world space system and vice versa. Meaning we are in search of ways to find which orientation of specific links can allow the endpoint of a given chain of links/arm to reach a given point in the 3D cartesian space.

Given a robot system, the link at the end of the link chain is generally called the end-effector (E). We are interested in its target motion based on the positions of the rest of the joints. So, let's assume a 2R planar robot as follows:
<br>
<p align="center">
  <img width=500 src=https://user-images.githubusercontent.com/77807055/170985482-f893da93-4613-485a-8ab4-35510a51f096.png>
  </p>
  
If I want the end-effector to reach at some arbitrary position, say ($x_0$, $y_0$, $z_0$), what should be the positions of the joints (i.e., what should be the values of $q_1$ and $q_2$)?

First thing that you should ask is whether such a coordinate is even accessible by the end-effector or not, given the fixed lengths $a_1$ and $a_2$ and joint angle limits??
<br>
<p align="center">
  <img width=500 src=https://user-images.githubusercontent.com/77807055/170986544-6a1a44d7-eca0-4b24-982f-209a50f09d6f.jpg>
  </p>
  
Now, there are two problems:
- Given a some values of $q_1$ and $q_2$, where will the end-effector land at??
- If I know the final position of the end-effector, what should be the joint angles??

These two questions seem inverse to each other and hence give rise to two broad categories...
- Given a value for each joint angles where will my end effector be? - *answered by **Forward Kinematics***
- Given a value, the end effector target position, what will by corresponding joint angles be to reach such a configuration? - *answered by **Inverse Kinematics***

While applying inverse kinematics, multiple set of joint values can be returned. You must keep in mind that the joint values returned should reside within the joint limits. If for any set, any of the joint value crosses the limits, then the set is discarded.

Again, there is a built-in function to calculate inverse kinematics...
<p align=center><a href="https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.9i02ojf4k3ve"><b>calculateInverseKinematics</b></a></p>

Forward Kinematics seems fairly straightforward, but the problem arises while using inverse Kinematics (unless you are using the inbuilt function of course). So, the inverse kinematics problem can be restated as:

For a robot system with N links, if the position and orientation of the Nth link (the end-effector) is given, then what are the possible sets of joint values (within their limits), such that, at those joint values, the end-effector reach its current position and orientation?

An analytical solution of the above 2R planar robot problem can be found in this video: <p><a href="https://www.youtube.com/watch?v=Ad5DLd8vrbQ">Robotics - Direct and Inverse Kinematics of 2 DoF planar robot</a></p>

## Additional Video resources:

1. Coding Challenge - by Daniel Shiffman, is a serious of computer programming challenges generally in JAVA based platforms.

    1. [Forward Kinematics](https://www.youtube.com/watch?v=xXjRlEr7AGk)
    2. [Inverse Kinematics](https://www.youtube.com/watch?v=hbgDqyy8bIw)

**Note:** In the above videos, **just refer to his explanation and approach he takes for implementing a IK and FK for an n-link 2D planar chain**, while it is not required to take his exact approach or try programing in **processing** like him.


2. [FK vs IK , an animation based explanation](https://www.youtube.com/watch?v=0a9qIj7kwiA)

3. [Hardware implementation of IK an FK on a 2R robot](https://www.youtube.com/watch?v=3rFaZMvgNe8)
