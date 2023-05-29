# LOCALISATION

### (we have the map but we don't know where we are- ultra pro max dilemma!!!)
![where-the-hell-am-i-where-am-i (1)](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/4a40e343-e73c-4117-8870-b29408d9cdcb)


Robot localization is the process of determining where a mobile robot is located with respect to its environment. Localization is one of the most fundamental competencies required by an autonomous robot as the knowledge of the robot's own location is an essential precursor to making decisions about future actions. In a typical robot localization scenario, a map of the environment is available and the robot is equipped with sensors that observe the environment as well as monitor its own motion. 

The localization problem then becomes one of estimating the robot position and orientation within the map using information gathered from these sensors. Robot localization techniques need to be able to deal with noisy observations and generate not only an estimate of the robot location but also a measure of the uncertainty of the location estimate. 


![agreed-nodding](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/aca44478-3fd7-4a78-ade9-98cf5f787e5b)

## Gaussian Distribution
**Normal distribution**, also known as the Gaussian distribution, is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. In graphical form, the normal distribution appears as a "bell curve".

![gaussian distribution](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/29adc295-c3f3-4311-8fa7-5efdd9f048ab)

![gaussian formula](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/00a158fd-f5a2-4310-89e5-128fcac5f675.png )


# Optimal Estimation Algorithms: Kalman and Particle Filters

+ ## **Kalman filter**
 Kalman filters are often used to optimally estimate the internal states of a system in the presence of uncertain and indirect measurements.
They take some input data, perform some calculations in order to make an estimate, calculate its estimation error and iteratively repeat this process in order to reduce the final loss. The iterative process performed by a Kalmar Filter can be summarised in 3 main steps:
+ **Kalman Gain Calculation**: is computed by using the error in the input data and in the estimation.
+ **Current Estimate Calculation**: is computed using the raw input data, our previous estimate and the Kalman Gain.
+ **Estimation Error Calculation**: is finally calculated using the Kalman Gain and our Current Estimate.

There exist different varieties of Kalman Filters, some examples are: linear Kalmar Filter, Extended Kalman filter and Unscented Kalman Filter.

### Check out videos 1 to 4 of this really cool playlist, it will get you covered --->: [Kalman Filter Playlist](https://www.youtube.com/playlist?list=PLn8PRpmsu08pzi6EMiYnR-076Mh-q3tWr)



Now, you know what Kalman Filter actually does!


![octopus](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/37bf9dfc-3649-4dd6-b951-b3cb779188f3)

**BUT!!!!!**

One of the main problems of Kalman Filters is that they can only be used in order to model situations which can be described in terms of Gaussian Noises. Although, many non-gaussian processes can be either approximated in gaussian terms or transformed in Gaussian distributions through some form of transformation (eg. logarithmic, square root, etc..).


In order to overcome this type of limitation, an alternative method can be used: **Particle Filters.**

+ ## **Particle filter**

Particle FIlters can be used in order to solve non-gaussian noises problems, but are generally more computationally expensive than Kalman Filters. That’s because Particle Filters uses simulation methods instead of analytical equations in order to solve estimation tasks.
Particle Filters are based on **Monte Carlo Methods** and manage to handle non-gaussian problems by discretizing the original data into particles (each of them representing a different state). The greater the number of particles and the better our Particle Filter would be able to handle any possible type of distribution.

Like Kalman Filters, Particle Filters also make use of an iterative process in order to produce its estimations. Each iteration can be broken down into three main steps:
+ Take multiple samples (particles) from an original distribution.
+ Weight all the sampled particles in order of importance (the more particles fall in a given interval and the higher is their probability density).
+ Resampling by replacing more unlikely particles with more likely ones (like in evolutionary algorithms, only the fittest elements of a population survive).

Watch the following video to understand how the above-mentioned process of resampling helps in estimationg the location. [Particle Filter](https://youtu.be/aUkBa1zMKv4)


![1_-kqCmIHcHam8tedYyf6RJA](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/33f749f2-9533-4ebb-a6e0-3d3540ef69ea)



### Time to checkout another playlist to get a better grip over particle filters in autonomous navigation. Watch videos 1-4. [Autonomous Navigation](https://youtu.be/Fw8JQ5Q-ZwU)


**Understood???**

![4BJW (1)](https://github.com/ePSA-eJya/Robotics-Camp-2023-forked/assets/120899038/dedd15ec-ef96-4840-8488-75c186c8d13b)

**Great!!!**

## NOW WITH THE TASKS!!!



The task for this part would be implementing the Kalman Filter algorithm and the Particle Filter algorithm in python.
[Kalman Filter task](/Phase1-Week2/Localisation/kalman.pdf)
