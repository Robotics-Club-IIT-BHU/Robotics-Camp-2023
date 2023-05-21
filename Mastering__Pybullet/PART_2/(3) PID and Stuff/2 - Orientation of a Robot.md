# Orientation
To define a robot's configuration, another important thing you need to understand is the orientation. In real world scenarios, multiple GPS and compass sensors are used to measure current position and orientation in space. The goal is to define rotations with respect to the object's local frame. There are a few ways to determine the orientation and rotations of objects in 3D space:
- Axis angles
- Euler angles
- Quaternions

This video 👇gives great intuition about what Euler angles actually are:<br>
- [Euler Angles](https://www.youtube.com/watch?v=qqlLshaHqeE)

But there is a problem with Euler angles, referred to as Gimbal Lock, most commonly heard in the movie Apollo 13. Check out this video:<br>
- [Gimbal Lock](https://www.youtube.com/watch?v=zc8b2Jo7mno)

Sometimes, the actual definition of Euler angles and the definition while defining Gimbal Lock can be confusing.<br>
- [Check out this video for a clear picture](https://www.youtube.com/watch?v=Mm8tzzfy1Uw)

Before moving to the next part, make sure to clarify everything about Euler angles. Clean your mind, relax, because the next way to determine rotations is...is...is...
<br>
<p align="center">
  <img width=350 src="https://media1.giphy.com/media/jivGITd768psP80B2i/200.webp?cid=ecf05e474nzcty27otsfi9ya3hiyi6sdape6k6k2u1206b0b&rid=200.webp&ct=g">
  </p>

  <h1 align="center">Quaternionsss!!!</h1>

Quaternions make use of imaginary numbers, yes you heard that right. But the idea behind them turns out to be really beautiful, although not so elegant. Now, if you want me to explain quaternions, be ready to be disappointed, cuzzz....
<br>
<p align="center">
  <img width=350 src="https://media3.giphy.com/media/tLGBynLboUTLy/200w.webp?cid=ecf05e47a76u0aq2ch1iklzzzewijl8wsvbtqb6vafxmeo47&rid=200w.webp&ct=g">
  </p>
  
  And...I don't think Quaternions can be explained any better than in this animation by 3 Blue 1 Brown:
  - [Quaternions - 3B1B](https://www.youtube.com/watch?v=d4EgbgTm0Bg)
