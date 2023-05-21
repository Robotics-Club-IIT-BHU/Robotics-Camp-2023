# Task for the part

**Task 1**
- For this part, you need to create a URDF similar to the one in the figure.
- The URDF is a 2R planar robot mounted on a revolving disc at a location near its circumference.
- Implement Inverse Kinematics for this system.
- Using the above implemented fuction, keep the system's end effector stationary while the disc keeps rotating.
- Consider any of the necessary constants on your own (i.e., lenght of links, radius of disc, etc).
###### - You are not allowed to use the inbuilt function in pybullet for calculating Inverse Kinematics. Write this function on your own.
<p align="center">
    <img width = "400" height = "300" src="task.gif">
    <img width = "400" height = "300" src="task_ik.png">
</p>

Before moving on to the next task, It can get fairly complicated for building a IK function from scratch at times. So, Pybullet has an inbuilt function for solving the Inverse Kinematics for a given robot urdf. As the saying goes...*for enlightenment, read the bible!!!*

<div align = "center">
   
   [calculateInverseKinematics](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.9i02ojf4k3ve)

</div>

**Task 1.5:**

Well, you guessed it right !!

Use the inbuilt function to complete the above task.

You need to create the URDF file required to complete the above tasks on your own (note that same URDF will work for both the tasks). Submit the URDF along with the .py files for both the tasks in the following link:
Also submit short videos of the working simulation on the link.
- [Submission_Link](https://forms.gle/n3cV9KfRjCeu4cp2A)
