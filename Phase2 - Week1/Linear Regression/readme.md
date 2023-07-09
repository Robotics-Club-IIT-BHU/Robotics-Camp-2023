# LINEAR REGRESSION
* `Linear Regression` is a `Machine Learning` algorithm based on Supervised Learning. It performs a Regression task. It is mostly used for finding out the
relationship between feature variables (`X`) and labels (`Y`). <br>
* For simple linear regression, the model has two parameters `w` and `b` whose values are `fit` using `training data`.
* Once a model's parameters (`w` and `b`) have been determined, the model can be used to make predictions on some new data. <br> <br>
<img align="right" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/864df561-0f42-47b3-8905-1ca81f02efde" width="380">

Now the question arises, how is it able to do this... <br> `How is it able to predict something...` <br> It simply tries to fit a line to the training data 
and when a new data point is given, it gives a prediction based on that. <br><br>
The model estimates the coefficients or weights (`w` and `b`) associated with each independent variable to make predictions using linear regression. 
These coefficients represent the contribution of each independent variable to the dependent variable. The model aims to find the `best-fitting line` that 
minimizes the difference between the predicted and actual values in the training data. <br> <br>
* Note - Don't confuse with `w` and `b`, they are simply $m$ (`slope`) and $c$ (`intercept`) in the equation of line, $y = mx+ c$.


## MODEL FUNCTION

<img align="left" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/8e4d7950-96c1-4974-9401-bc0d1ca675e4" style=" width:380px; padding: 10px; " >

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
<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/1ed8fd6e-e3d6-4954-8a82-0557e8b2faf9" style=" width:512px; padding: 10px; "/>


## COST FUNCTION CODE
<img align = "left" src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/fc5eab77-ac8e-4bf5-b28c-fdf52cfca6bd" style=" width:400px; height:210px; padding: 10px; "/>

<img align = "right" src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/d1f7e9ac-027a-4272-bfa8-a144f78a07c9" style=" width:430px; height:210px; padding: 10px; "/>

<br> <br> <br> <br> <br> <br> <br> <br> <br> <br>
As you can see, the cost values for different `w` and `b`. And hence, our aim is to get such values for `w` and `b`, such that we get the least cost possible,
or in other words, best model possible. <br><br>

But will you be calculating `w` and `b` randomly and get the least possible values ?? No, right .... <br>
Here's where the `Gradient Descent Algorithm` comes into play, `The OG of Linear Regression`, which uses Calculus to calculate the minimum values of `w` and `b`,
cause remember, the minimum the values, the better the model and our predictions. <br>
<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/b63fa19c-a93e-427b-adac-131d838119bb" style=" width:512px; padding: 10px; "/>

## GRADIENT DESCENT
<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/d4a845e8-8a60-41d4-b965-04f70ddc8079" style="padding: 10px; "/> <br> 
### PS - Don't get scared by all these mathematical equations, it's just for understanding, you won't be doing all these maths for implementing Linear Regression.
<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/15ecbd63-b16f-40dc-bb81-fc9ca3d90f69" style="padding: 10px; "/> <br>
### Notice the decrease in the cost value as we carry on with our iterations. From 10 ^ 4 to 10 ^ -5.
Initially, The Cost is much higher and decreasing it with subsequent iterations. <br><br>
<img src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/fea4336a-7807-466d-99e6-978840dbc5a1" style="padding: 10px; "/> <br>
### Animation to understand better, how Gradient Descent works.
![gradient_descent_example](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/11b47bd8-174b-42c2-a0c6-162393e637c4)

## MAKING PREDICTIONS
We got the optimal value of `w` and `b`, which can now be used to predict a new data point, simply by putting the new data point into our Model Function. <br>

## EXAMPLE USING SCIKIT-LEARN
Let's start with a basic Dataset on Salary Prediction on the basis of experience. <br>
PS - First Try it yourself.
Dataset Link: https://www.kaggle.com/datasets/shsrivas/salary-data
### Visualising the Dataset
<img align = "left" src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/3c621a4a-0568-40b7-8fc4-4d2fd3dad3fd" style="width: 180px; padding: 10px; "/> <br>

<img align = "centre" src = "https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/4135acf9-d4b1-4425-9a15-01b53dc87ae6" style="width: 400px; padding: 10px; "/> <br>
<br>
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/a170c29c-e77c-4e38-842c-9dd56eb05b61)
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/046394df-ec6b-426e-8e51-745f6232d6d0)<br>

### After training our Linear Regression Model
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/2e461ae7-75b1-4b85-82be-f0580476893e) <br>
You can even get the $w$ and $b$ of your model. <br>
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/7475f84d-26bb-4971-9437-f60c6557946a)

