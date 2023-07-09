# LINEAR REGRESSION
* `Linear Regression` is a `Machine Learning` algorithm based on Supervised Learning. It performs a Regression task. It is mostly used for finding out the
relationship between feature variables (`X`) and labels (`Y`). <br>
* For simple linear regression, the model has two parameters `w` and `b` whose values are `fit` using `training data`.
* Once a model's parameters (`w` and `b`) have been determined, the model can be used to make predictions on some new data. <br> <br>
<img align="right" src="https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/25ab798f-0b01-4ec7-ad18-ffa5dc2e5683" width="380">

Now the question arises, how is it able to do this... <br> `How is it able to predict something...` <br> It simply tries to fit a line to the training data 
and when a new data point is given, it gives a prediction based on that. <br><br>
The model estimates the coefficients or weights (`w` and `b`) associated with each independent variable to make predictions using linear regression. 
These coefficients represent the contribution of each independent variable to the dependent variable. The model aims to find the `best-fitting line` that 
minimizes the difference between the predicted and actual values in the training data. <br> <br>
* Note - Don't confuse with `w` and `b`, they are simply $m$ (`slope`) and $c$ (`intercept`) in the equation of line, $y = mx+ c$.


## MODEL FUNCTION

<img align="left" src="https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/089a631a-e17a-4001-81f7-2582d795e173" style=" width:380px; padding: 10px; " >
The model function for linear regression (which is a function that maps from `x` to `y`) is represented as 

$$ f_{w,b}(x^{(i)}) = wx^{(i)} + b \tag{1}$$

The formula above is how you can represent straight lines - different values of $w$ and $b$ give you different straight lines on the plot. 
<br/> <br>
Don't get scared by looking at this, it's just the equation of a line ($y = mx+ c$) written in a fashionable way. <br/> <br/> <br/> 

## COMPUTING COST
The term `cost` is a measure of how well our model predicts the target (`Y`). The equation for cost with one variable is:
  $$J(w,b) = \frac{1}{2m} \sum\limits_{i = 0}^{m-1} (f_{w,b}(x^{(i)}) - y^{(i)})^2 \tag{1}$$ 
where 
  $$f_{w,b}(x^{(i)}) = wx^{(i)} + b \tag{2}$$
  
- $f_{w,b}(x^{(i)})$ is our prediction for example $i$ using parameters $w,b$.  
- $(f_{w,b}(x^{(i)}) -y^{(i)})^2$ is the squared difference between the target value and the prediction.   
- These differences are summed over all the $m$ examples and divided by `2m` to produce the cost, $J(w,b)$.

### Now Let's get out hands dirty with some Code.
<img src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/1ebab18c-3fbe-4aa1-ac6c-977cbb062b01" style=" width:512px; padding: 10px; "/>

## COST FUNCTION CODE
<img align = "left" src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/159e2c8c-c184-4a95-908d-f589e245f6ec" style=" width:400px; height:230px; padding: 10px; "/>
<img align = "right" src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/5565451e-33b4-400e-bb8c-ac19a0e07caf" style=" width:430px; height:230px; padding: 10px; "/>
<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>
As you can see, the cost values for different `w` and `b`. And hence, our aim is to get such values for `w` and `b`, such that we get the least cost possible,
or in other words, best model possible. <br><br>

But will you be calculating `w` and `b` randomly and get the least possible values ?? No, right .... <br>
Here's where the `Gradient Descent Algorithm` comes into play, `The OG of Linear Regression`, which uses Calculus to calculate the minimum values of `w` and `b`,
cause remember, the minimum the values, the better the model and our predictions. <br>
<img src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/dd441998-413e-4eb4-aad1-38f94eeee838" style=" width:512px; padding: 10px; "/>

## GRADIENT DESCENT
<img src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/858bb904-5427-4b26-9f5e-2b42c71a8079" style="padding: 10px; "/> <br> 
### PS - Don't get scared by all these mathematical equations, it's just for understanding, you won't be doing all these maths for implementing Linear Regression.
<img src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/4ef4f87c-7925-460c-a20e-5c804505b33f" style="padding: 10px; "/> <br>
### Notice the decrease in the cost value as we carry on with our iterations. From 10 ^ 4 to 10 ^ -5.
Initially Cost being much higher and decreasing it with subsequent iterations. <br><br>
<img src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/ad5f6a18-a9b8-4d01-83b4-e55d74294e6a" style="padding: 10px; "/> <br>
### Animation to understand better, how Gradient Descent works.
![image](https://raw.githubusercontent.com/mattnedrich/GradientDescentExample/master/gradient_descent_example.gif)

## MAKING PREDICTIONS
We got the optimal value of `w` and `b`, which can now be used to predict a new data point, simply by putting the new data point into our Model Function. <br>

## EXAMPLE USING SCIKIT-LEARN
Let's start with a basic Dataset on Salary Prediction on the basis of experience. <br>
PS - First Try it yourself.
Dataset Link: https://www.kaggle.com/datasets/shsrivas/salary-data
### Visualising the Dataset
<img align = "left" src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/0b7108d0-45b6-403a-a788-5e4656d59463" style="width: 180px; padding: 10px; "/> <br>
<img align = "centre" src = "https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/d4706828-daca-4fcd-810b-971012e81846" style="width: 400px; padding: 10px; "/> <br>
<br>
![image](https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/e516cb8a-838c-404a-9790-f7ca2768558b)
![Screenshot (617)](https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/f0bbf62a-a720-4902-bf4b-1491cf493656)
<br>
### After training our Linear Regression Model
![image](https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/ae0bfc2a-3ed1-4d1e-be38-030096b3a29e) <br>
You can even get the $w$ abd $b$ of your model. <br>
![image](https://github.com/mitanshu17/Heart-Disease-Classification-using-ML/assets/118126264/8188f350-97b5-46f8-bf66-1456877227bf)



