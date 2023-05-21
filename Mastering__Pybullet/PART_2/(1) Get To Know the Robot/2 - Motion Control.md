# Motion Control
Now that you know the current state of your robot, you might want to change these states, or move some joints or apply some external forces. Again, pybullet has got you covered.

### Position, orientation or velocity of the base link can be changed anytime. In this manner, you can respawn the whole robot at any desired location.
Check out the functions:
<p align="center"><a href="https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.2n2evd7lqqe1"><b>resetBasePositionAndOrientation</b></a></p>
<p align="center"><a href="https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.4vxw9j7piyjd"><b>resetBaseVelocity</b></a></p>

### Positions of various joints can also be reset to any desired value. This should be done at the start of the simulation, and not in between. Because if you are trying to simulate real world, then it is impractical to instantaneously reset joint positions.
<p align="center"><a href="https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.p3s2oveabizm"><b>resetJointState</b></a></p>

### Motion of the joints...
Links in a robot are the parts that we want to move. Because ultimately they only are going to interact with the outer world. But in order to connect the links and move them in any restrained manner, we have introduced joints. Joints in turn are controlled by motors. Motors, as we know, are responsible to convert electrical energy to mechanical energy i.e., responsible for motion, be it rotational motion or translational motion. So, there are motors in the joints and these motors are connected to the controller. The controller (our python code in this case) sends commands to each of the motors as to how much force they need to apply to rotate or translate. The joints move along with the motors resulting in the motion of the links.

Now the actual structure and knitty gritty details of the motors and joint structure won't be covered as our main task is to control their motion. For each motor (or joint), there is some maximum value of force and velocity (in case of linear motion) or torque and angular velocity (for rotational motions). Obviously, you cannot keep increasing the force/torque on any motor, right? Also, there is a limit to the positions as well. For linear motion, there are minimum and maximum values of positions, and the joint can't translate any further than the maximum limit or any less than the minimum limit, similarly there are limits to the angles in case of rotational motion.

PyBullet provides a function called as setJointMotorControl2 to control various joints. Various control methods like POSITION_CONTROL, VELOCITY_CONTROL and TORQUE_CONTROL are available. They focus on how you want to control the joint. POSITION_CONTROL is when you have a desired target position, VELOCITY_CONTROL for desired velocity and TORQUE_CONTROL for desired force/torque.
<p align="center"><a href="https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.jxof6bt5vhut"><b>setJointMotorControl2</b></a></p>
<br>
<p align="center">
  <img width=500 src="https://media3.giphy.com/media/EBysPyjz3BHVu/200w.webp?cid=ecf05e476643s21hpk4vn3x8bb8g175mhsy371vwc6sj1red&rid=200w.webp&ct=g">
  <br><i>Look, I can control you man!</i>
  </p>

Check out [this basic implementation](car.py) of setJointMotorControl2.
