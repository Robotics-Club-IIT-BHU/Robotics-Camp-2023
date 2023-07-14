# CNN(Convolution Neural Network)

Till Now we have seen how to deal when there are numbers as our input features in neural networks.But what about images????
Isn't it interesting to classify images. Example- just by looking at images your algorithm can predic whether the image is containing dog or a cat
But how can we do this??? Let's see!!!

## Images

Generally images are of two types colour images and greyscale images.Color image includes the color information for each pixel while greyscale
images contains shades of grey.

### Image Resolution

#### Grey-scale image

<img align="center" src="https://cdn-5f733ed3c1ac190fbc56ef88.closte.com/wp-content/uploads/2019/03/imagematrix.png">

#### Coloured image

<img src = "https://www.nzfaruqui.com/wp-content/uploads/2019/03/Accessing-pixel-values-color-image.jpg" width="700">


Image resolution could be defined as the number of pixels present in an image.Every image has its own shape i.e their number of rows and columns. On increasing 
them pixel value in an images increases and hence the quality.
Each pixel value has its specific value which acts as input in our CNN model.


More about them would be covered in computer vision part of this week.

Also refer to this web page to know more: [Analytics Vidya](https://www.analyticsvidhya.com/blog/2021/09/a-beginners-guide-to-image-processing-with-opencv-and-python/?utm_source=reading_list&utm_medium=https://www.analyticsvidhya.com/blog/2021/06/everything-happening-in-computer-vision-that-you-should-know/).

## CNN Architecture

<img src="https://editor.analyticsvidhya.com/uploads/59954intro%20to%20CNN.JPG">

Steps:

1. Convolution Operation
2. Passing through Non linearity layer
3. Pooling
4. Flattening
5. Full Connection

### 1. Convolution Operation
<br>
<img src = "https://miro.medium.com/v2/resize:fit:2340/1*Fw-ehcNBR9byHtho-Rxbtw.gif" width="500">
<br>

This layer performs a dot product between two matrices, where one matrix is known as a kernel, and the other matrix is the restricted 
portion of the image.
In above demonstration the blue matrix which is the bigger one is the input image the moving 3x3 matrix is the kernel and the gray output blocks 
are the dot product of the input image and the kernel known as feature map or the activation map.

<img src = "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*r13ZUdVTQwVuhDPmo3JKag.png" width = "500">

A question must come to our mind why we are doing convolution whats the need of it?? 

Do read [this](https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939) to know it.

Also we pass our activation map to ReLU layer to increase non-linearity between pixels since our input image would be most probably non-linear.

<br>
<br>

### 2. Passing through Non linearity layer

Since convolution is a linear operation and images are far from linear, non-linearity layers are often placed directly after the convolutional 
layer to introduce non-linearity to the activation map.eg.- sigmoid,tanh, ReLU etc.


### 3. Pooling 

Pooling layers are used to futher decrease the size of our feature map by taking summary of regions.
Let's assume we have a image of dog in our train but while predicting we have similar kind of image but slightly tilted, then pooling layer would
help us to take that dissimilarity into our account.There are different kinds of pooling such as max pooling, average pooling etc.
Below is an example of the max pooling 

<br>
<img src = "https://miro.medium.com/v2/resize:fit:1400/format:webp/1*sK7oP1m129V_oNGSsHIm_w.png" width="500">


### 4. Flattening

This layer is basically used to convert our pooled feature map into an 1-d array which could act as a input to our fully connected layer 
which is noting but simple ann kind of network.

### 5. Fully Connected Layer

<img src="https://indiantechwarrior.com/wp-content/uploads/2022/05/Hidden-Layer-1-1024x603.png">


<br>
# That's all???How would you implement??😯😯

 for implementation part you have to follow some resources:

 - [Tensorflow Docs](https://www.tensorflow.org/tutorials/images/cnn)(Documentation is always the best and most accurate place to implement anything)
 - [Towards Data Science](https://towardsdatascience.com/convolutional-neural-networks-explained-9cc5188c4939)
 - [analytics Vidya](https://www.analyticsvidhya.com/blog/2022/01/convolutional-neural-networkcnn/)
