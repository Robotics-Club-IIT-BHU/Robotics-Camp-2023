# Semantic Segmentation
<img align="right" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/d9f629cc-437f-4f4f-a785-83ec7bb3f60c" width="380">
Semantic segmentation is the process of assigning a class label to each pixel in an image (aka semantic classes). The labels may say things like “dog,” 
“vehicle,” “sky,” etc. The same-class pixels are then grouped together by the ML model. Semantic segmentation can be, thus, compared to pixel-level image 
categorization. As a result, each pixel of a picture is assigned a specific class label in semantic segmentation.
<br><br>
As the name implies, semantic segmentation means dividing an image into multiple segments. Sounds simple enough, right? However, to make the process run 
smoothly and let the machines learn as effectively as possible, semantic image segmentation is actually a multistep process that requires a variety of methods, 
models, and both ML and DL techniques.

# Instance Segmentation
<img align="right" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/2cb07cc5-8e3e-4b78-b583-540584e1f744" width="380">

Instance segmentation is one step ahead of semantic segmentation wherein along with pixel level classification, we expect the computer to `classify each
instance of a class separately`. For example in the image above there are 3 people, technically 3 instances of the class “Person”. All the 3 are classified
separately (in a different color). But semantic segmentation does not differentiate between the instances of a particular class.

# Applications
## 1. Autonomous Vehicles
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/336bc48f-0f2c-44a3-b945-da3d1a7619ab)
## 2. Bio Medical Image Diagnosis
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/81000679-c91e-48c4-9195-89cf81051224)
## 3. Geo Sensing
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/aa4c918c-53df-4c54-9fa8-57d86f901ab8)

### Now Let us understand how to carry out the task and the model used.
Semantic Segmentation often requires the extraction of features and representations, which can derive meaningful correlation of the input image, 
essentially removing the noise. CNN consists of a convolutional layer, a pooling layer, and a non-linear activation function. In most cases, CNN
has a fully connected layer at the end in order to make class label predictions.
<br><br>
But When it comes to semantic segmentation, `we usually don’t require a fully connected layer` at the end because our goal isn’t to predict the class label 
of the image. In semantic segmentation, our aim is to extract features before using them to separate the image into multiple segments.
However, the issue with convolutional networks is that the size of the image is reduced as it passes through the network because of the max-pooling layers.
To efficiently separate the image into multiple segments, `we need to upsample it using an interpolation technique, which is achieved using deconvolutional layers`.

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/d8f98ff2-f38f-4d4a-8602-b35c85c819e3)
<br>
In general AI terminology, the convolutional network that is used to extract features is called an encoder. The encoder also downsamples the image, 
while the convolutional network that is used for upsampling is called a decoder.
<br>
Here’s a visual representation of convolutional encoder-decoder.
<br><br>
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/3bbbd9d3-b303-496b-baa1-21eb9b23f480)
 <br>
The output yielded by the decoder is rough, because of the information lost at the final convolution layer i.e., the 1 X 1 convolutional network. This makes
it very difficult for the network to do upsampling by using this little information. <br><br>

# UNET Architecture
The U-net has a similar design of an encoder and a decoder. The former is used to extract features by downsampling, while the latter is used for 
upsampling the extracted features using the deconvolutional layers.
The shortcut connection in the U-Net is designed to tackle the information loss problem.
The U-net is designed in such a manner that there are blocks of encoder and decoder. These blocks of encoder send their extracted features to its 
corresponding blocks of decoder, forming a U-net design. <br><br>
<img align = "center" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/e764c125-c381-4e26-97f0-83e9c86f145e" width="512">

### Now How would the Dataset look like ?
It would consist of an image along with it's mask which would look something like this.
![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/db8745a3-175f-4bef-b8c8-afad6d701933)

### The Architecture
```
def conv2d_block(input_tensor, n_filters, kernel_size = 3):
  x = input_tensor
  for i in range(2):
    x = tf.keras.layers.Conv2D(filters = n_filters, kernel_size = (kernel_size, kernel_size),\
            kernel_initializer = 'he_normal', padding = 'same')(x)
    x = tf.keras.layers.Activation('relu')(x)
  
  return x
```
<br>

### Encoder
<br>

```
def encoder_block(inputs, n_filters=64, pool_size=(2,2), dropout=0.3):
  f = conv2d_block(inputs, n_filters=n_filters)
  p = tf.keras.layers.MaxPooling2D(pool_size=(2,2))(f)
  p = tf.keras.layers.Dropout(0.3)(p)

  return f, p


def encoder(inputs):
  f1, p1 = encoder_block(inputs, n_filters=64, pool_size=(2,2), dropout=0.3)
  f2, p2 = encoder_block(p1, n_filters=128, pool_size=(2,2), dropout=0.3)
  f3, p3 = encoder_block(p2, n_filters=256, pool_size=(2,2), dropout=0.3)
  f4, p4 = encoder_block(p3, n_filters=512, pool_size=(2,2), dropout=0.3)

  return p4, (f1, f2, f3, f4)
```

<br>

### Bottleneck

```
def bottleneck(inputs):
  bottle_neck = conv2d_block(inputs, n_filters=1024)
  return bottle_neck
```

 <br>

 ### Decoder

```
 def decoder_block(inputs, conv_output, n_filters=64, kernel_size=3, strides=3, dropout=0.3):
  u = tf.keras.layers.Conv2DTranspose(n_filters, kernel_size, strides = strides, padding = 'same')(inputs)
  c = tf.keras.layers.concatenate([u, conv_output])
  c = tf.keras.layers.Dropout(dropout)(c)
  c = conv2d_block(c, n_filters, kernel_size=3)

  return c


def decoder(inputs, convs, output_channels):
  f1, f2, f3, f4 = convs

  c6 = decoder_block(inputs, f4, n_filters=512, kernel_size=(3,3), strides=(2,2), dropout=0.3)
  c7 = decoder_block(c6, f3, n_filters=256, kernel_size=(3,3), strides=(2,2), dropout=0.3)
  c8 = decoder_block(c7, f2, n_filters=128, kernel_size=(3,3), strides=(2,2), dropout=0.3)
  c9 = decoder_block(c8, f1, n_filters=64, kernel_size=(3,3), strides=(2,2), dropout=0.3)

  outputs = tf.keras.layers.Conv2D(output_channels, (1, 1), activation='softmax')(c9)

  return outputs
```

<br>

### Putting it all together

```
def unet():
  inputs = tf.keras.layers.Input(shape=(128, 128,3,))
  encoder_output, convs = encoder(inputs)

  bottle_neck = bottleneck(encoder_output)

  outputs = decoder(bottle_neck, convs, output_channels=OUTPUT_CHANNELS)
  model = tf.keras.Model(inputs=inputs, outputs=outputs)

  return model

model = unet()

model.summary()

model.compile(optimizer=tf.keras.optimizers.Adam(), loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
              
model_history = model.fit(train_dataset, epochs=EPOCHS,
                          steps_per_epoch=STEPS_PER_EPOCH,
                          validation_steps=VALIDATION_STEPS,
                          validation_data=test_dataset)
```

<br><br> 

![image](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/118126264/5b3530e5-55f5-4d39-86b1-d5abf0dff472)

### Well That's a lot, but the most vital step which you would need to carry out won't be the architecture or model. It would be the image preparation.
You would have to prepare consistent `images` and `masks`, which would then be fed to the UNet Architecture.
<br><br>
Here are some code examples for the data preparation.
```
idd_images = np.zeros((len(imagedir), 128, 128, 3), dtype = np.float32)
for i in tqdm(range(0, len(imagedir))):
    img = Image.open(IMG_DIR + imagedir[i]).resize((128, 128))
    img = np.array(img, dtype = np.float32)/255.0
    idd_images[i] = img
idd_images.shape
```
PS - Do import: `from PIL import Image, ImageOps`

```
idd_masks = np.zeros((len(maskdir), 128, 128), dtype = np.float32)
for i in tqdm(range(0, len(maskdir))):
    img = Image.open(MASK_DIR + maskdir[i]).resize((128, 128))
    img = ImageOps.grayscale(img)
    img = np.array(img, dtype = np.float32)
    idd_masks[i] = img
idd_masks = np.expand_dims(idd_masks, axis = 3)
idd_masks.shape
```

### Here I'll be providing a Kaggle notebook, where you can run the code and carry out segmentation yourself, which would help you better understand this process.
Kaggle Notebook: https://www.kaggle.com/code/mitanshuchakrawarty/segmentation-exp <br>
Dataset Link: https://www.kaggle.com/datasets/mitanshuchakrawarty/new-idd-dataset

**Note**: <br>
Adding data to the notebook (in case it's not added), Go to the `Add Data` option and search for the dataset (`new-idd-dataset`), then click `+` to add it.
Secondly, do look out for the address as it may differ, change it if required. <br><br>
**Note**: <br>
Don't get confused if you find the architecture different. It's the same but written in a different way. You can go and try out both ;) <br>
Just remember to prepare images and masks properly and define the architecture correctly. Do look out for shapes and if you encounter any error, search the net, 
if you are unable to find any solution, you may approach any of us anytime :) <br>

### Have A Nice Day :)




