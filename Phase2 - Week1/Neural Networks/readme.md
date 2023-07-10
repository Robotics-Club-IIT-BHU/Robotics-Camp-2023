# Neural Networks
So far you have learned about Linear Regression and Logistic Regression. 
* `Linear Regression` deals with the regression problem where you have to predict the real number value of something like price prediction etc.
* On the other hand, `Logistic Regression` deals with the classification problem, where you have to predict the correct class among a number of classes, technically Logistic Regression is for binary classification but its extension `Softmax Regression` deals with multiple classes.

Neural Networks are a different class of algorithms that in general deals with problems like classification. They are the building blocks of what is known as `Deep Learning`. So let's embark on a journey of exploring and understanding Neural Networks and Deep Learning in general.

## Problem with Logistic Regression
Logistic Regression is a fantastic algorithm for the classification problem, but it's a `linear classifier`.<br> 

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/c2111c5f-31a0-4bf8-95b6-2fe9c1542a83)


What do we mean by a linear classifier ?<br>
* A linear classifier achieves it's aim by making a classification decision based on the value of a linear combination of the characteristics. Thus, they are limited to the data which are linearly separable.

You may recall in logistic regression we calculate our input as:

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/8619e2c2-d4a3-4fee-8e9e-2cfd192f34a1)

You can see the output is linear combination of our x's. This output is then pass on to the the sigmoid function which classify our data linearly into 2 class.<br>
If you wanna dig deep refer to this: https://sebastianraschka.com/faq/docs/logistic_regression_linear.html<br>

But what if our data is lot more complicated than that ? What if just linear classfiers are not enough ?<br>
Like here, `A` is linearly separable, whereas `B` is not. We can't use linear classifiers for `B`.

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/eaaf1604-3891-488e-8380-745fdc5fe4f4)

This is where `neural networks` comes in!

## What are Neural Networks exactly ?

To be loosely vague and honest, they are just a bunch of matrix dot products with some extra flavors added to them. We take our input and  its dot product with several layers of weights and pass it on to a function such as softmax to generate the probability of different classes. It learns the right set of weights and biases using gradient descent which you have learned about by now.<br>

<img src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/0ffbe5fb-758b-4f02-a708-2fe89731f06e" width = "600" height = "400">


This here is a simple neural network with just a single hidden layer. We take our input in as vectors and pass it on to the hidden layer by taking the dot product of input with weights connecting each input node to each hidden layer node. <br>

You can see each node in our input layer has a connection leading to each node in the hidden layer. These connections are nothing but weights and biases. 
All our inputs in the input layer have connections to each node in the hidden layer, which are given by their own sets of weights and biases. <br>

For example, for the first 
node in hidden layer, the sets of weghts are [w11, w12, w13], where `wij` refers to the connection between `ith` node in next layer and `jth` node in previous layer.

<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/bcad1a3b-f158-4f6e-8da2-2f4ae995ab02" width = "400" height = "400" >


Similarly, we take our hidden layer in vector form and take its dot product with its own set of weights, which leads to our output and then apply the softmax function to get the probability of each class. We can add several hidden layers to make our neural network deeper. Hence, the word "Deep" Learning. Also, the reason we vectorize our weights and biases is that matrix and vector
multiplication is a very efficient way of taking dot products.

You may be thinking about how this is different from logistic regression with no hidden layer. We take our inputs and take it dot product with a bunch of weights which leads to our output. <br>
Well, you are right. No matter how deep your neural network is, you can always shrink it by removing hidden layers in between.

**Problem:** For any two consecutive weighted sums of the input, there exists a single
weighted sum with exactly identical behavior.<br>

<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/e5332780-f2cf-413c-a06f-1c6bf782c9e2" width = "300" height = "200" >


<br>So if this is all that neural networks are, they posses the same problem we had with our Logistic Regression. The output is a linear combination of the inputs. So, they should also be linear classifiers. But remember, I said something about them having some extra flavors, well these flavors make our neural network non-linear classifiers. After each hidden layer, we add a non-linearity to our neural networks. This non-linearity is known as an Activation Functions.

<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/815eee5a-98d6-40ee-ad1b-8e02e670610c" width = "800" height = "400" >

Before we move on some key resources you should go through:
* `3 blue 1 brown` is the best place to learn about mathematics and stuff. We're blessed that Grant Sanderson decided to pour his understanding of neural networks upon us through his brilliant series.:<br>
  https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
* John Stammer's `StatsQuest` is also a great place to start with machine learning stuff :<br>
   https://youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1 [Videos: **1 - 13**]

These resources will give you an in-depth understanding that you should have about Neural Networks. They also have great videos regarding the topic that we will go through next.

## Activation Functions

We have talked about how to give our neural networks the power of `non-linearity`, we use Activation Functions. They are simple functions that are non-linear.
Passing our outputs through these activation functions allows neural nets to add non-linear relations between layers. These function needs to be differentiable since, while using gradient descent to update our weights and biases, we will have to caculate their derivatives.

`See, the thing about Deep Learning is that there is a lot of stuff that
is hard to understand. It's a big field and a lot goes into making these neural networks learn. But don't get overwhelmed you learn some of this stuff, you implement them, and as you progress , you improve your
understanding. Researchers are scratching their brains in interpreting these models, and you are just beginning your journey, so be at ease. The resources we have provided, will help
you a lot, and you can always search for medium articles on any topic.`

Coming back to activation functions, in general we use 3-4 types depending on our need:

**ReLU**

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/ac101848-40b1-4b52-a5af-801cb0538bfb)

ReLU is given by max(0,x) and thus allow only positive outputs to pass through.

**Sigmoid**

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/15ffa064-eb88-405d-be44-8e289fbb7afe)

You have already seen this one in logistic regression. It compresses values of outputs between [0,1], thus it acts like a probability function and is used
when we have to calculate the probability of something, like in case of our classification problem.

**Tanh**

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/7e36704c-0b4b-4733-aec0-f418ae5f327a)

It's somewhat simliar to sigmoid function, only difference being it compresses the outputs in bewteen [-1,1]. It converges better than sigmoid, but it shouldn't be used after our final output layer since we generally want our output to be a probability, i.e. in between [0,1].

**Softmax**

<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/c02173c8-de8c-4ab8-8c10-57b3b264295d" width = "300" height = "150" >

Softmax is an extension of the sigmoid function but is much better. Sigmoid compresses each output in between [0,1], whereas softmax gives output as a  probability distribution. The sum of all the output values in the case of softmax will be 1, which is not the case with sigmoid. Softmax assigns a higher probability to a correct class and a lower to 
wrong classes.

These four activation functions are commonly used. Tanh and ReLU are used with hidden layers, while softmax and sigmoid with output layer. I have just given you a overview of activation functions
but there is a lot that goes around. To dig deeper: https://medium.com/@vinodhb95/activation-functions-and-its-types-8750f1287464

## Backpropagation

By now, you know what neural networks are and how they are different from linear models. The main key here is neural net learns a function that takes our x's as input and predicts y as our output. As the neural net learns, this function gets closer to the true original function that would have generated (x,y) pairs in our dataset.<br>

This function, in general, is non-linear since we gave activation function power to our neural networks and generally involves a lot of weights and biases. We train our network to learn the right sets of these. How we do that: We use gradient descent in general. You have learned about gradient descent, in the regression section or through the resources we gave above. Yeah! you
should go through the resources by now.<br>

In the case of linear and logistic regression, we were manually calculating gradients and applying gradient descent to them. But neural networks are much deeper and generally involve more than
single layer with a lot of weight. It's not possible to calculate their gradients manually. Hence we use this beautiful algorithm of backpropagation. It starts from your output layer, and 
starts calculating gradients for each input and moves backwards till your input layer. We only require gradients for weights and biases to update them for better convergence. <br>

**Resources for backprop**
  * The ones we provided earlier.
  * To dig deeper: Well it's my own blog but I think it will give you a fair idea of things, https://www.notion.so/dhruv-jain/backpropagation-with-autograd-Part-1-08a42839108b44299fcd86374844e583. Sorry for shameless self promotion XD.

## Stochastic Gradient Descent

Gradient Descent is a powerful algorithm. But in a real-world scenarios with ever growing datasets, it has two major limitations:
* Calculating derivatives for the entire dataset is time consuming,
* Memory required is proportional to the size of the dataset.<br>
Gradient Descent’s update rule is applied to all data points in the dataset, it all in one step. As the dataset increases this computation becomes much slower, so the time to convergence will increase.

This is where `Stochastic Gradient Descent` comes in!

Stochastic Gradient Descent is a probabilistic approximation of Gradient Descent. It is an approximation because, at each step, the algorithm calculates the gradient for one observation picked at random, instead of calculating the gradient for the entire dataset. We take a random input, calcu;ate the gradients and do the updates. We call backprop for one input at a time.

<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/b5e926f0-d6e8-4dce-851a-4191864d9c29" width = "500" height = "250" >


Compared to Gradient Descent, Stochastic Gradient Descent is much faster, and more suitable to large-scale datasets.

But since the gradient it’s not computed for the entire dataset, and only for one random point on each iteration, the updates have a higher variance. This makes the cost function fluctuate more on each iteration, when compared to Gradient Descent, making it harder for the algorithm to converge.

There is a middle ground between Stochastic Gradient Descent and plain  Gradient Descent: `Batch Stochastic Gradient Descent` <br>
We neither take our whole dataset at once nor a single data at a time. Instead, we randomly sample a batch of our data. The batch size is a hyperparameter but 
is usually the power of 2: [**32, 64, 128, 256**]

## Loss Functions

You know what a loss function is. I will list some commonly used loss function. You can search them individually to learn more.

**Classification Problem**
* `Binary Cross Entropy Loss: ` Used when we have to classifiy between two classes.
* `Cross Entropy Loss: ` Used when we have to classifiy between multiple classes.
*  `Negative log likelihood: ` Used when we have to classifiy between multiple classes.

**Non-Classification Problems/ Regression Problems**
* `L2 Loss: ` Used when we predict some real value output as we saw in Linear Regression.
* `L1 Loss: ` Used when we predict some real value output as we saw in Linear Regression.

You can always google to know more and you should.

## Resources and Tasks

I have given you a rough overview of what goes on in Deep Learning and Neural Networks. This by no means is self suffficient. Watch videos, read more, read blogs and spend some time.
We will provide you with some resoruces here to help you out.
* `3 blue 1 brown`: https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi
* `StatsQuest`: https://youtube.com/playlist?list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1 [Videos: **1 - 13**]
* `Grokking Deep Learning` by Andrew Trask, read this book and you will be glad you did.
* `Deep Lizard`: https://youtube.com/playlist?list=PLZbbT5o_s2xq7LwI2y8_QtvuXZedL6tQU
* `Google`: Find your own set of resources that suits you best.

**Task**

Here is the colab file which will guide you through your task:
* https://colab.research.google.com/drive/1OsB3pL78j8gr7KEg23nmOpGRjA0mXaEi?usp=sharing
* Make sure you create a copy of this file in your own drive.

You will need to know some more stuff for the task.:
* `Numpy`: Go through numpy resources we provided in Intro to ML section.
* `Weight Intialization`: https://towardsdatascience.com/weight-initialization-techniques-in-neural-networks-26c649eb3b78

Maybe some of the stuff may look overwhelming but it's just implementation of everything you have learned so far. Go thorugh codes, debug them and understand. If you face any problem don't hesitate to ask in 
group. Best of luck!

**Submission Link:** https://forms.gle/CGFXf7MgTjVC8Af9A






























