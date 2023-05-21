Before moving forward, here is a dictionary of sample examples that contains implementation of various functions.
<p align="center"><a href="https://github.com/bulletphysics/bullet3/tree/master/examples/pybullet/examples"><b>PyBullet Sample Code Directory</b></a></p>

# Query Robot's Info
As we have discussed that any robot has various links and joints including the base link. At any point of time, we might need some information about the robot's current configuration like the position, orientation or velocity of any link or joint. Or in general, we can query about the number of joints in the robot, what are the various joint names, their types, their parent and child links etc. So, a bunch of querying functions are available in pybullet. But before diving into that, go through the bible-based definition of base, joints and links, and how their indices are assigned:
- [Base, Joints and Links](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.e27vav9dy7v6)
<p align="center">
  <img width=500 src="https://media0.giphy.com/media/ZvjRrOBjxFdWo/giphy.webp?cid=ecf05e47anbia4v85w9eyr8kp48nmx5tdt2pxr51f6gvtzqb&rid=giphy.webp&ct=g"><br>
  <i>Is the picture clear till now?</i>
  </p>
  
#### Cool, now let's look at each of the functions one by one...
## Base Info
- [getBasePositionAndOrientation](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.vy9p26bpc9ft)
- [getBaseVelocity](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.4vxw9j7piyjd)

## Links Info
- [getLinkState](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.3v8gjd1epcrt)

## Joints Info
- [getNumJoints](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.la294ocbo43o)
- [getJointInfo](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.la294ocbo43o)
- [getJointState](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.p3s2oveabizm)

Sometimes, if you are stuck, then **stackoverflow** also has some really great explanations.
<br>
<p align=center>
  <img width=500 src="https://iq.opengenus.org/content/images/2021/08/stackoverflow-2.jpg">
  <br><i>Yay!! StackOverFlow!!</i>
  </p>
  
Yeah, but you can be down on your luck sometimes...
<br>
<p align="center">
  <img width=500 src="https://scontent.fktu1-1.fna.fbcdn.net/v/t1.6435-9/64717123_366582473989897_7901991890445139968_n.png?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_ohc=vgm8wS1lupQAX8bxMjC&_nc_ht=scontent.fktu1-1.fna&oh=00_AT8NjCYOfuUKsqfQkABfznSTLHy6O-AqrMTwSRcW8xkaBA&oe=62B91826">
  </p>
