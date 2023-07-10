## Logistic Regression

You learned about Linear Regression and saw how it's implemented using Scikit Learn. Now we will shift out attention towards `Logistic Regression`.
<br>
Logistic Regression is a classification algorithm that classifies between two linearly seprabale classes.

**What is linearly seprabale classes ?**
<br>
We say classes are separable if there's a classifier whose decision boundary separates the positive objects from the negative ones. If such a decision boundary is a linear function of the features, we say that the classes are linearly separable.

  ![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/72b64a85-40f8-46eb-a4e9-bc5744071326)
  <br>
  

Coming back, Logistic Regression is one of key algorithm in the class of `linear classifiers`.<br>

In the case of `linear regression` we took our input x and some weights and the output was
given by the dot product of both. This resulted in a real valued number as our output. We then apply gradient descent to find the right sets of our weights and fit 
our model to our data. Logistic Regression is somewhat similar to this with a small but major change.<br>

As in case of linear regression we calculate our intermediate output as:

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/e6583f6a-a08e-47d8-a89d-5402558bd0b2)

We then pass it through a special kind of function know as `sigmoid` function:

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/98597396/f4fa44a4-e42b-438f-aea6-53fed030b6fc)

Sigmoid takes a real-valued number as an input and compresses it in between [0,1],  thus resulting in a probability. 
<br>

The intermediate output is passed through this sigmoid function and the final output is a probability. You see, logistic regression alone is not a classifier, its a probability generator. We then take this probability and choose a threshold. If the probability is above this threshold, we classify our input in one class and if the probability is below this threshold we classify our input into another class. Thus logistic regression is a binary classification algorithm.

`Logistic Regression + Threshold = Linear Classifier`<br>

Generally our threshold is **0.5**.<br>

Here are the materials to go through for in-depth understanding:
* `StatsQuest`: https://youtube.com/playlist?list=PLblh5JKOoLUKxzEP5HA2d-Li7IJkHfXSe **Videos [1 : 4]**
* https://medium.datadriveninvestor.com/logistic-regression-1532070cf349
* `Hands on ML Book` : You can go through the chapter on Logistic Regression.
* `Logistic Regression From Scartch` : https://youtu.be/JDU3AzH3WKg

## Softmax Regression (Bonus)

As you learned above, logistic regression is used in the case of binary classification i.e. for two classes only. Softmax Regression is an extension to it
and is also known as multinomial logistic regression.

You can go through this for learning about softmax regression: https://rasbt.github.io/mlxtend/user_guide/classifier/SoftmaxRegression/




