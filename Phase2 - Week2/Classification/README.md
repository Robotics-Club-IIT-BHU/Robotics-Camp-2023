# Classification
## Introduction
<img align="right" src="https://github.com/Mitra-Pidaparti/Classification/assets/110911635/bb4f0ec9-c925-4d49-ba71-1a64442e2ec2" width="400">   


- The fundamental objective of classification is to make `predictions about the category or class` (represented by y) based on given inputs (represented by x).
- It is one of the most widely used techniques in machine learning, with a broad array of applications, including sentiment analysis, ad targeting, spam detection, risk assessment, medical diagnosis, and image classification.

![Dogs vs cats](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/a3ac2d07-3562-4887-9664-2aa91d79c548)

### How Image Classification actually works:

So we already learned about CNN's let us see how they are actually used in Image Classification:
#### Feature Extraction: 
- Feature maps are the output of the convolutional layers in the network. A feature map represents the presence or activation of specific features or patterns in the input image.
- When an image is passed through a CNN, the convolutional layers perform a series of convolutions by applying a set of learnable filters to the input image. Each `filter detects specific patterns or features at different spatial locations in the input, such as edges, textures, or shapes`.
- The result of these convolutions is a set of feature maps. Each feature map corresponds to a specific filter and represents the response or activation of that filter across the spatial dimensions of the input image. Each location in a feature map contains information about the presence or strength of a particular feature detected by the corresponding filter.

![FeatureExtract](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/6dd2bcaf-0791-49e8-8803-52d340395699)



![Pytorch Feature Extraction](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/4b8a93d3-f641-4b9d-b765-c441649310f1)


Above are 64 feature maps extracted using CNN. Notice how each feature map focuses on different things and highlights different aspects of the image

[More about feature extraction](https://towardsdatascience.com/convolutional-neural-network-feature-map-and-filter-visualization-f75012a5a49c)


#### Training and Learning: 
- The next step is to train a classification model using the extracted features. This involves adding fully connected layers on top of the convolutional layers to `learn the relationship between the features and classes`. The model is trained with labeled images, optimizing its parameters through backpropagation and gradient descent. Hyperparameters like learning rate, batch size, and regularization are adjusted to improve performance.
  
#### Evaluation: 
- After training, the model's performance is evaluated using a separate set of test images using various evaluation metrics.
  
#### Prediction: 
 - After training and evaluation, the model can classify new images. It takes an input image, applies preprocessing, extracts features using the trained CNN, and `predicts the class label based on learned relationships`. This allows the model to make informed decisions when classifying unseen images.

### Image Preprocessing:
 Often a  critical and underappreciated step in the image classification pipeline. While much focus is placed on the model architecture and training process, image preprocessing plays a vital role in improving the quality and effectiveness of the model.

- Image preprocessing is the steps taken to format images before they are used by model training and inference. This includes but is not limited to, `resizing, orienting, and color corrections
- Fully connected layers in convolutional neural networks, a typical architecture in computer vision, require that all images are the `same sized arrays`. If your images are not in the same size, your model may not perform as expected

```{python}
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('birds.jpg')
h, w, c = img.shape
print(f"Height and width of original image: {h}, {w}" )

#resize the image
new_size = (450, 340) # new_size=(width, height)
print(f"New height and width: {new_size[1]}, {new_size[0]}" )
resize_img = cv2.resize(img, new_size)

 #Convert the images from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
resize_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2RGB)

plt.subplot(121),plt.imshow(img), plt.title("Original Image")
plt.subplot(122), plt.imshow(resize_img), plt.title("Resized Image")
plt.show()
```

![Height,widht](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/42d053eb-eb79-41fb-9037-14dcbf59f8d8)
![Resized Image](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/a74fe301-af78-4f0f-86bc-148504dc39c4)



- Learning the OpenCV library is pretty useful: Here is the documentation, play around with some images:)[OpenCV](https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html)

**Image Augmentation**:
- Image augmentation `creates diverse versions of similar images through transformations like rotation, brightness, and scale changes`. By exposing the model to a broader range of training examples, it learns to recognize subjects in different situations, enhancing its ability to handle real-world variations. This expands the training dataset, improving model generalization and performance.
- `Image Augmentation is only applied to the training set`
- The `ImageDataGenerator` class from Keras generates batches of image data with real-time data augmentation.
  Example: For an image like this:
  
![Airplane](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/4c3d90fc-1565-40ea-adbc-d6358c50c269)


  
We can perform a bunch of operations to give these kinds of images:


![airplaneaugmented](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/12dc420c-80d7-4112-a974-55abe3350aa6)

How to code these:[Augmentation](https://towardsdatascience.com/image-data-augmentation-for-deep-learning-77a87fabd2bf#:~:text=Image%20augmentation%20comes%20in%20many,%2C%20and%20Zoom%20In%2FOut.)
, [When to use](https://blog.roboflow.com/why-preprocess-augment/)

  
### Evaluation Metrics:
- Some new terms: `True Positives, True Negatives, False Positives, False Negatives`:
Here is an example:
![Application of binary](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/d17c74b9-14e8-4a2d-baa5-17d4a7372f41)



<img align="right" src="https://github.com/Mitra-Pidaparti/Classification/assets/110911635/f9f91f40-8303-42b5-948f-160b8c54e210" width="500"> 

- True Positive (TP): The patient is diseased and the model predicts "diseased"
- False Positive (FP): The patient is healthy but the model predicts "diseased"
- True Negative (TN): The patient is healthy and the model predicts "healthy"
- False Negative (FN): The patient is diseased and the model predicts "healthy"

For a better understanding of Confusion Matrix: [Confusion Matrix](https://youtu.be/Kdsp6soqA7o)-->

  Now, here are some metrics for evaluation that use the above

  ![Evaluation metrics](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/809fa922-9ab6-4b8b-921d-489e61a3a916)




**When to use which metric?**
- Accuracy is obviously the most straight-forward as it tells us the fraction of how many predictions were right
but accuracy is not necessarily the best. Check this article out: [Accuracy, Precision, Recall or F1?](https://towardsdatascience.com/accuracy-precision-recall-or-f1-331fb37c5cb9)



## Implementation
Lets look at a step by step implmentation to classify animals as dogs or cats

#### Importing Dependencies and Preparing Directories
```{python}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Installing visualkeras
!pip install visualkeras   
import visualkeras
import warnings
warnings.filterwarnings('ignore')
import os
os.chdir('/kaggle/input/')
os.listdir()
```
#### Setting Data Directories
```{python}
train_dir = '/kaggle/input/cats-and-dogs-image-classification/train'
test_dir = '/kaggle/input/cats-and-dogs-image-classification/test'
```
####  Creating Image Generators for Train and Test Data
- When using the image_dataset_from_directory function, it automatically assigns labels to the images based on the subdirectory structure. Each subdirectory represents a different class or category, and the function assigns a unique label to each class.
```{python}
from keras.utils import image_dataset_from_directory
train_generator = image_dataset_from_directory(train_dir, image_size=(64, 64), batch_size=32)
test_generator = image_dataset_from_directory(test_dir, image_size=(64, 64), batch_size=32)
```
#### Visualizing Samples from the Train Dataset
```{python}
# showing only the first 10 samples of our training data set
plt.figure(figsize=(10, 10))
for images, labels in test_generator:
    for i in range(9):
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(images[i].numpy().astype("uint8"))
        plt.title(int(labels[i]))
        plt.axis("off")
```

![DatasetVis](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/0ef1ea46-0f47-4083-80fc-1a2e8a8b9087)




#### Building the CNN Model
```{python}
# building CNN
model = keras.Sequential([
    # Conv layer 1:
    keras.layers.Conv2D(128, (3, 3), input_shape=(64,64,3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size = (2, 2)),
    
    # Conv layer 2:
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size = (2, 2)),
    
    # Conv layer 3:
    keras.layers.Conv2D(32, (3, 3), activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(pool_size = (2, 2)),
    
    keras.layers.Flatten(),
    
    # fully connected layers:
    keras.layers.Dense(units = 128, activation = 'relu'),
    keras.layers.Dense(units =1, activation = 'sigmoid')
    
])

model.compile(optimizer = keras.optimizers.Adam(learning_rate=0.001), loss = 'binary_crossentropy', metrics ='accuracy')

model.summary()

```
#### Visualizing the Model Architecture
```{python}
visualkeras.layered_view(model)
```
![Model_viz](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/d6812b9d-7cb7-4fdf-9c2f-4d75271e50c5)


#### Training the model
```{python}
# Create an instance of EarlyStopping callback
es = keras.callbacks.EarlyStopping(monitor='val_loss', patience=7, restore_best_weights=True, verbose=1)
```
- EarlyStopping stops training if validation loss does not improve for 7 consecutive epochs
- restore_best_weights=True restores the model weights to the best found during training
- verbose=1 prints messages about the progress of early stopping
```{python}
# Create an instance of ReduceLROnPlateau callback
red_lr = keras.callbacks.ReduceLROnPlateau(monitor='val_loss', patience=3, factor=0.1, verbose=1)
```
- ReduceLROnPlateau reduces learning rate if validation loss does not improve for 3 consecutive epochs
- factor=0.1 determines the factor by which the learning rate will be reduced (multiplied by 0.1)
- verbose=1 prints messages about the learning rate reduction
```{python}
# Start model training
logs = model.fit(train_generator, epochs=50, validation_data=test_generator, validation_steps=2000/32, callbacks=[es, red_lr])
```
- model.fit trains the model using the provided data generators for training and validation
- epochs=50 specifies the number of training epochs (complete passes through the training data)
- validation_data=test_generator provides the data generator for the validation set
- validation_steps=2000/32 determines the number of steps (batches) to evaluate the validation data (2000 samples divided by batch size 32)
- callbacks=[es, red_lr] passes the EarlyStopping and ReduceLROnPlateau callbacks to monitor the training progress and apply necessary actions


#### Plotting Training History
```{python}
plt.title('Training Log')
plt.plot(logs.history['loss'], label='Training Loss')
plt.plot(logs.history['accuracy'], label='Training Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Score')
plt.legend()
plt.show()
```
![Traininplot](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/43a6aa9c-30a7-42fe-bfad-388626cedb1d)

####  Evaluating on the Test Dataset
```{python}
res = model.evaluate(test_generator)
accuracy = res[1]
print(accuracy)
```
![loss](https://github.com/Mitra-Pidaparti/Classification/assets/110911635/3f7c1358-2f7c-466b-9d1f-7e7335f939c3)

Not satisfied with this accuracy? Well, there are ways you can improve it

- Of course, Adding more layers to your model increases its ability to learn your dataset’s features more deeply, helping it to extract more complex features from the image
- Getting more data, also Image augmentation will help.
- Here is an additional method called `Transfer Learning`, it's like using pre-trained knowledge to solve a new problem.
  Check this article out for [Transfer Learning](https://towardsdatascience.com/a-comprehensive-hands-on-guide-to-transfer-learning-with-real-world-applications-in-deep-learning-212bf3b2f27a)

## Resources:
- **Medium** articles are awesome. I suggest you subscribe if possible
- [Codebasics](https://www.youtube.com/@codebasics) playlists are pretty cool
- You can audit **Coursera** courses(option where you can view the content for free without certification)
  
  


