# LOCALISATION
Robot localization is the process of determining where a mobile robot is located with respect to its environment. Localization is one of the most fundamental competencies required by an autonomous robot as the knowledge of the robot's own location is an essential precursor to making decisions about future actions. In a typical robot localization scenario, a map of the environment is available and the robot is equipped with sensors that observe the environment as well as monitor its own motion. The localization problem then becomes one of estimating the robot position and orientation within the map using information gathered from these sensors. Robot localization techniques need to be able to deal with noisy observations and generate not only an estimate of the robot location but also a measure of the uncertainty of the location estimate. 

## Gaussian Distribution
Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. In graphical form, the normal distribution appears as a "bell curve".

![gaussian distribution](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/29adc295-c3f3-4311-8fa7-5efdd9f048ab)

![gaussian formula](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/00a158fd-f5a2-4310-89e5-128fcac5f675.png )



# Optimal Estimation Algorithms: Kalman and Particle Filters

+ ## **Kalman filter**

video link: [Matlab playlist Link](https://www.youtube.com/playlist?list=PLn8PRpmsu08pzi6EMiYnR-076Mh-q3tWr)
+ ## **Particle filter**
Particle FIlters can be used in order to solve non-gaussian noises problems, but are generally more computationally expensive than Kalman Filters. That’s because Particle Filters uses simulation methods instead of analytical equations in order to solve estimation tasks.
Particle Filters are based on **Monte Carlo Methods** and manage to handle non-gaussian problems by discretizing the original data into particles (each of them representing a different state). The greater the number of particles and the better our Particle Filter would be able to handle any possible type of distribution.

Like Kalman Filters, Particle Filters also make use of an iterative process in order to produce its estimations. Each iteration can be broken down into three main steps:
+ Take multiple samples (particles) from an original distribution.
+ Weight all the sampled particles in order of importance (the more particles fall in a given interval and the higher is their probability density).
+ Resampling by replacing more unlikely particles with more likely ones (like in evolutionary algorithms, only the fittest elements of a population survive).

![particle filter](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/7e72d386-ead8-43bc-bedb-3c62c083865c)


[Autonomous Navigation](https://youtu.be/Fw8JQ5Q-ZwU)

[Particle Filter](https://youtu.be/NrzmH_yerBU)
