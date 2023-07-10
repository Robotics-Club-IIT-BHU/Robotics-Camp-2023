# Neural Networks
So far you have learned about Linear Regression and Logistic Regression. 
* `Linear Regression` deals with the regression problem where you have to predict the value of something which can be any value on real number line.
* On the other hand, `Logistic Regression` deals with the classification problem, where you have to predict the correct class among number of classes, technically Logistic Regression is for binary classification but it's extension `Softmax Regression` deals with varying number of classes.

Neural Networks are different class of set of algorithms which in general deals with problems like classification. It's a huge field of study in itself and are the building blocks of what is known as `Deep Learning`. So let's embark on a journey of exploring and understanding Neural Networks and Deep Learning in general.

## Problem with Logistic Regression
Logistic Regression is a fantastic algorithm for the classification problem, but it's a `linear classifier`.<br> 

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/c2111c5f-31a0-4bf8-95b6-2fe9c1542a83)


What do we mean by a linear classifier ?<br>
* A linear classifier achieves it's aim by making a classification decision based on the value of a linear combination of the characteristics. Thus, they are limited to the data which are linearly separable.

You may recall in logistic regression we calculate our input as:

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/8619e2c2-d4a3-4fee-8e9e-2cfd192f34a1)

You can see the input are linear combination of our x's. This input is then pass on to the the sigmoid function which classify our data linearly into 2 class.<br>
If you wanna dig deep refer to this: https://sebastianraschka.com/faq/docs/logistic_regression_linear.html<br>

But what if our data is lot more complicated than that ? What if just linear classfiers are not enough ?<br>

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/eaaf1604-3891-488e-8380-745fdc5fe4f4)

Here, `neural networks` comes into picture.

## What are Neural Networks exactly ?

To be loosely vague and honest, they are just a bunch of matrix dot product with some extra flavours added to it. We take our data and take it's dot product with a number of layers of weights and pass it on to function such as softmax to generate probability of different number of classes. It learn the right sets of weights and biases using gradient descent just like we saw previously.

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/9353e1c5-2713-44c7-b6e0-8ec0bd91cfcf)

This a simple neural network with just 1 hidden layer. We take our input in form of vectors and pass it on to the hidden layer but taking the product of input with weights connecting each input node to each hidden layer node. <br>

You can see each node in out input layer has a connection leading to each node in hidden layer, these connections are nothing but weights and the biases. You should think of it as each node in hidden layer has conncetions to all the inputs, which is given by own set of weights for a node in hidden layer.

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/9339b92f-ce15-4f23-82b0-6678f4741855)

We then similarly take our hidden layer in vector form and take it's dot product with certain weights and this lead to our output. We can then apply softmax function to get probability of each class. We can add a number of hidden layers to make our neural network deeper. Hence, the word "Deep Learning". 

You maybe thinking how this is different from logistic regression with no hidden layer. We take our inputs and take it dot product with bunch of weights which leads to our output. <br>
Well, you are right. As a matter of fact no matter how deep your neural network is you can always shrink it into just a input and a output.<br>

**Problem:** For any two consecutive weighted sums of the input, there exists a single
weighted sum with exactly identical behavior. 

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/e5332780-f2cf-413c-a06f-1c6bf782c9e2)

So neural networks posses exactly the same problem we had with our Logistic Regression. The output is linear combination of the inputs and hence they are also linear classifiers. But remember, I said something about they having some extra flavors, well this flavors make our neural network non-linear classifiers. After each hidden layer, we add a non-linearity to our neural networks and this non-linearity is known as a `Activation Functions`.















