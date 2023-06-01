
# Task for this Subpart

From Pybullet camp, you are familiar with building urdfs(assuming only static models). In this task your aim is to build the geometrical tags for the below robot(Original Version developed by RoboREG-adversarial_cars team [here](https://github.com/Robotics-Club-IIT-BHU/gym-adversarial-cars/tree/main/adversarial-gym/adversarial_cars/envs/rsc/car)) and visulaise it in RViz and debug there.
<p align ="center">
<img width = 400 height=300 src = "https://github.com/Robotics-Club-IIT-BHU/gym-adversarial-cars/blob/main/media/auto.png"><br/>
<b>Credits for this URDF- gym-adversarial_cars team - RoboREG</b>
</p>

- [ ] You can use the above link to access the urdf and use this link [Visulaising urdf tutorial from ROS for your urdf](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch) to get started with visualizing it. The next task is to setup TF with this urdf [TF with Robot](http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF), Here they have used a laser but what i need you to do is setup tf from baselink to each wheels.

- [ ] After setting up Tf to test it out you have to print the coordinates, and orientation (prefered in euler angles) of the point [1,1,0] from 3 different frame of references (i.e., From the baselink, from left wheel, from right wheel) you may choose to add more frames but in the submission of this task you have to make a clear video while demonstrating your code running and the urdf spawnned on RVIZ. We strictly prefer the use of TF to complete this task but you are more than welcome to do it by hand but it is neccesary for using TF for the next task. 

- [ ] After you have used TF we just want you to submit the pdf generated using TF Frames, whos syntax can be found here.[Debugging tools](https://wiki.ros.org/tf/Debugging%20tools)

Happy `make`ing!!
