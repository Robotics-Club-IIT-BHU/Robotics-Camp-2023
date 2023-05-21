
## What is  Simulation?

![ComputerInitiateCombatSimulationSmorgasborgSamanthanRutherfordGIF](https://github.com/vaibhavgupta0403/trial_1/assets/100301165/74d65aa1-15ae-4d05-955d-45724f883b2e)
   
[Is Reality Real? The Simulation Argument](https://www.youtube.com/watch?v=tlTKTTt47WE)

### Defined as: 
   Simulation software is based on the process of modeling a real phenomenon with a set of **mathematical formulas**. It is, essentially, a program that allows the user to observe an operation through simulation without actually performing that operation.Thus, it proves to be a very close proxy to the real-world i.e. a mathematical model of the real world processes. The simulation plays a very important role in robotics. Different tools are used for the analysis of kinematics(does not include the cause of motion), dynamics(includes the cause of motion) of robotic manipulators, for off-line programming, to design different control algorithms, to design mechanical structure of robots, to design robotic cells and production lines, etc.

## Why use simulations?

* Simulations are the best place to start when developing a new robot. By using a simulator to develop your robot, you can quickly identify if your idea is feasible or not with almost no expense. Additionally, you can easily test and discover which are the physical constraints that your robot must face to accomplish its goal.
* Simulators allow the easy and quick test of many different ideas for the same robotic problem, test them, and then decide which one to build based on actual data.
* Since your robot has been defined and tested in the simulator, you can start its physical construction. The good thing with simulators is that they allow you to keep doing tests even if your robot is not built yet.
* Bugs found in your robot software can be debugged first in the simulator.
* By debugging in the simulator you will save a lot of time since testing on the real robot is very time-consuming.
* Given that simulation is the way to go, there are plenty of options available for robotics  namely Bullet, Gazebo, V-Rep, Webots, Open Dynamics Engine, MujoCo, etc.

## PyBullet
Bullet is a **physics engine** that simulates **collision detection, soft and rigid body dynamics**. It has been used in video games as well as for visual effects in movies.PyBullet is an easy to use Python module for physics simulation, robotics, and deep reinforcement learning based on the Bullet Physics SDK.

Given the options, the reason for selecting PyBullet is,
* It's a lightweight software and opens source with an active community.
* Built for python development, hence gives more informative and clear approach for beginners. 
* No external dependencies except a fully working python interpreter.

Here are some simulations in PyBullet (Some of you might have already experienced it during VISION'23) :

<p align="center">
   <img width="480" height="320" src="gif01.gif">
</p>
<p align="center">
   <img width="480" height="320" src="gif02.gif">
</p>
<p align="center">
   <img width="480" height="320" src="gif03.gif">
</p>

### Installation of PyBullet ( EXTRA BUT CAN TRY FOR PYBULLET INSTALLATION IN WINDOWS )

The installation of PyBullet is as simple as:
(sudo)`pip install PyBullet` (Python 2.x), 
`pip3 install PyBullet`
This will expose the PyBullet module as well as pybullet_envs Gym environments.

If you are getting Visual C++ version issues in Windows, then

1. First of all uninstall everything you have installed till now, like any Python platform such as anaconda, jupyter, Python idle, visual studio... including visual studio basic tools and related softwares and restart the machine (Important).
2. Install Python idle v3.7.7 from [here](https://www.python.org/ftp/python/3.7.7/python-3.7.7-amd64.exe), you can go for the latest one too which is supported by your machine, but just because older versions are more compatible, here v3.7.7 is included. While installation go through default installation, kindly check mark Add to path option.
3. Install visual studio basic tools from [here](https://drive.google.com/file/d/1rhnHXYUMPnS9Z3ygkJMOJ40bkZiTSonF/view?usp=drivesdk), (approx 3MB file) Kindly use institute mail id only. This is the web based setup, this will cost you around 400mb of data, but install through this link only (Important). If you are able to successfully install visual studio basic tools then jump to step 6
4. If you get an error while installing visual studio basic tools such as .Net framework 4.5 or above is required then install it from [here](https://www.microsoft.com/en-in/download/details.aspx?id=30653). This link is for framework 4.5 you can install the latest one too, which is supported by your machine. If you don't get any error in this them jump to Step 6.
5. While installation of .Net framework, if you get error such as package is not applicable to your computer, that's mostly because service pack update is missing, or if it says that a particular update package is needed, then kindly update your windows through windows update, and try searching for that particular update package on the web, although windows update will fix this. Maybe windows update can't install all the updates in one go, so after taking updates and restarting the machine, search for updates via windows update again until you get windows is up to date message from windows update.
6. Open command prompt (cmd.exe), Type commands
   1. pip install pybullet (important)
   2. pip install wheel (if you get some wheel related error while running above command)
   3. pip install --upgrade pip(optional)
7. Open Python idle this will open the shell, under file tab click new, in newly opened window you can type you code and run it.

#### If the above process doesn't work for windows users then try: 

1. Install Visual Studio 2019 Community version [here](https://visualstudio.microsoft.com/downloads/).
2. In the setup, in workloads select “Python Development” and “Desktop development with C++”.
3. After installation, launch Visual Studio and create a new python project.
4. Goto Tools>Python>Python Environments.
5. In the Overview bar on the right side, select “Open in Powershell”
<p align="center">
   <img  src="Powershell.jpg">
</p>

6. Once your Powershell pops up, type “pip3 install PyBullet” and press enter.
7. You can install any python package using pip in the Powershell.
8. Try running this example code:
```python
import pybullet as p
import time
import pybullet_data
physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("r2d2.urdf",cubeStartPos, cubeStartOrientation)
for i in range (10000):
    p.stepSimulation()
    time.sleep(1./240.)
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print(cubePos,cubeOrn)
p.disconnect()
```
**Contact us if you face any difficulties with the installation.**

## Note:
   As a prescribed text we share the [PyBullet_Quickstart_Guide](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Mastering__Pybullet/PART_1/(1)%20Installation%20and%20Starter%20Code/PyBullet_Quickstart_Guide.pdf) for quick reference.It contains almost all the functions and the necassary details for using Pybullet,in short its like your bible for this course.Thus, through out this camp it is advised you constanly refer this for better understanding.

We will go through each line of the above given code and understand what it does,
1. First we import the required libraries i.e. pybullet, time and pybullet_data
2. **connect**
* After importing the PyBullet module, the first thing to do is 'connecting' to the physics simulation. PyBullet is designed around a client-server driven API, with a client sending commands and a physics server returning the status. PyBullet has some built-in physics servers: DIRECT and GUI. Both GUI and DIRECT connections will execute the physics simulation and rendering in the same process as PyBullet.
* The connect function returns a physics client id.
* The DIRECT connection sends the commands directly to the physics engine, without using any transport layer and no graphics visualization window, and directly returns the status after executing the command.
* The GUI connection will create a new graphical user interface (GUI) with 3D OpenGL rendering, within the same process space as PyBullet.
3. **setAdditionalSearchPath** is used to add pybullet_data to the path which contains many examples, urdf files, etc.
4. **setGravity**:By default, there is no gravitational force enabled. setGravity lets you set the default gravity force for all objects.
The setGravity input parameters are: (no return value):


parameter type  | Name | type | Description
--- | --- | --- | ---
required  | gravityX | float | gravity force along the X world axis
required  | gravityY | float | gravity force along the Y world axis
required  | gravityZ | float | gravity force along the Z world axis
optional  | physicsClientId | int | if you connect to multiple physics servers, you can pick which one.

5. **loadURDF**: The loadURDF will send a command to the physics server to load a physics model from a Universal Robot Description File (URDF).

Some important arguments of loadURDF are:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | fileName | string | a relative or absolute path to the URDF file on the file system of the physics server.
optional  | basePosition | vec3 | create the base of the object at the specified position in world space coordinates [X,Y,Z]. Note that this position is of the URDF link position. If the inertial frame is non-zero, this is different from the center of mass position. Use resetBasePositionAndOrientation to set the center of mass location/orientation.
optional  | baseOrientation | vec4 | create the base of the object at the specified orientation as world space quaternion [X,Y,Z,W]. See note in basePosition.

6. We store the initial position of our urdf file in the variable cubsStartPos.

7. We store the initial Quaternion orientation of our urdf file in cubeStartOrientation
**(More details about Quaternions will be given in Part 2)**

8. We import our r2d2 robot urdf file in the desired position and orientation.

9. **stepSimulation**:stepSimulation will perform all the actions in a single forward dynamics simulation step. The default timestep is 1/240 second, it can be changed using the setTimeStep or setPhysicsEngineParameter API.

10.**getBasePositionAndOrientation**:getBasePositionAndOrientation reports the current position and orientation of the base (or root link) of the body in Cartesian world coordinates. The orientation is a quaternion in [x,y,z,w] format.
The arguments of getBasePositionAndOrientation are:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | objectUniqueId | int | object unique id, as returned from loadURDF.
optional  | physicsClientId | int | if you are connected to multiple servers, you can pick one.

11.**disconnect**: You can disconnect from a physics server. A 'DIRECT' or 'GUI' physics server will shutdown. A separate (out-of-process) physics server will keep on running. See also 'resetSimulation' to remove all items.

![INeedMoreMikhailVarshavskiGIF](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/100301165/fa78be65-73b4-4f47-bbfe-f4a72bd025c8)



See you in the next Part !!!!
