# Object Detection

Over the past decade, Deep learning has drawn much greater attention and become imperious technology in the Artificial intelligence area. Object detection is considered one of the noteworthy areas in the deep learning and Computer vision. Object detection has been determined the numerous applications in computer vision such as object tracking, retrieval, video surveillance, image captioning, Image segmentation, Medical Imagine and several greater number other applications as well. In this track, we are going to be understanding all the fundamental things about object detection. So, Let’s get started.

[For more detailing you can visit out this link ](https://machinelearningmastery.com/object-recognition-with-deep-learning/)

<p align="center" width="100%">
    <img width="40%" src="https://user-images.githubusercontent.com/76533398/182803919-b7858dfa-7d64-4ea3-9627-03dd412c82cb.png">
</p>

Object detection algorithms are broadly classified into two categories based on how many times the same input image is passed through a network.
The state-of-the-art methods can be categorized into two main types: one-stage methods and two stage-methods. One-stage methods prioritize inference speed, and example models include YOLO, SSD and RetinaNet. Two-stage methods prioritize detection accuracy, and example models include Faster R-CNN, Mask R-CNN and Cascade R-CNN.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/100301165/c7ab7a22-f0d5-451f-b1e3-f61f4d2f7d2b.png">
</p>

#### Here , we will be mainly focussing upon the use of YOLO Architecture for Object Detection ( Mainly YOLOv5 and YOLOv3 model)

# YOLO (You Only Look Once) Algorithm

Yolo is a state-of-the-art, real-time object detection system. This algorithm is popular because of its speed and accuracy. It has been used in various applications to detect traffic signals, people, parking meters, and animals.

Biggest advantages:

- Speed (45 frames per second — better than realtime)
- Network understands generalized object representation (This allowed them to train the network on real world images and predictions on artwork was still fairly accurate).
- Faster version (with smaller architecture) — 155 frames per sec but is less accurate.
- Open source: https://pjreddie.com/darknet/yolo/

## How does YOLO work? YOLO Architecture

The YOLO algorithm takes an image as input and then uses a simple deep convolutional neural network to detect objects in the image. The architecture of the CNN model that forms the backbone of YOLO is shown below.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/100301165/45f87478-f99e-4ef5-a0f1-c7b921aaaee9.png">
</p>

The first 20 convolution layers of the model are pre-trained using ImageNet by plugging in a temporary average pooling and fully connected layer. Then, this pre-trained model is converted to perform detection since previous research showcased that adding convolution and connected layers to a pre-trained network improves performance. YOLO’s final fully connected layer predicts both class probabilities and bounding box coordinates.

YOLO divides an input image into an S × S grid. If the center of an object falls into a grid cell, that grid cell is responsible for detecting that object. Each grid cell predicts B bounding boxes and confidence scores for those boxes. These confidence scores reflect how confident the model is that the box contains an object and how accurate it thinks the predicted box is.

YOLO predicts multiple bounding boxes per grid cell. At training time, we only want one bounding box predictor to be responsible for each object. YOLO assigns one predictor to be “responsible” for predicting an object based on which prediction has the highest current [IOU (Intersection Over Union)](https://www.youtube.com/watch?v=XXYG5ZWtjj0&list=PLhhyoLH6Ijfw0TpCTVTNk42NN08H6UvNq&index=2) with the ground truth. This leads to specialization between the bounding box predictors. Each predictor gets better at forecasting certain sizes, aspect ratios, or classes of objects, improving the overall recall score.

One key technique used in the YOLO models is non-maximum suppression [(NMS)](https://www.youtube.com/watch?v=YDkjWEN8jNA&list=PLhhyoLH6Ijfw0TpCTVTNk42NN08H6UvNq&index=3). NMS is a post-processing step that is used to improve the accuracy and efficiency of object detection. In object detection, it is common for multiple bounding boxes to be generated for a single object in an image. These bounding boxes may overlap or be located at different positions, but they all represent the same object. NMS is used to identify and remove redundant or incorrect bounding boxes and to output a single bounding box for each object in the image.

*<i>(You can skip the PyTorch implementations in the following videos for now)</i>
#### Don't worry for there implementation part in Pytorch , below are some of the listed resourses in Tensorflow.

- [Intersection over Union](https://medium.com/@venuktan/vectorized-intersection-over-union-iou-in-numpy-and-tensor-flow-4fa16231b63d)
- [Non-Max Suppression](https://whatdhack.medium.com/reflections-on-non-maximum-suppression-nms-d2fce148ef0a)
- [Mean Average Precision](https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173)

### [YOLO Overview](https://www.v7labs.com/blog/yolo-object-detection#:~:text=One%20of%20the%20main%20advantages,driving%20cars%2C%2)


<p align="center" width="100%">
    <img width="50%" src="https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/100301165/ee15a3cb-be03-4fce-abe2-a57cab3f9959.png">
</p>

### How to train your own custom dataset with YOLOv5 ???

Given below is a attached github reference link where the whole process from creating the dataset in yolov5 format ( using either Roboflow or custom python code)
to training of the model or using pre trained model ( on a given dataset ) has been explained throughly so I would request everyone of you to go throughly through the content. ( Try playing with different models within yolov5 to get hands-on-experience on each of it).

#### [GITHUB LINK Yolov5](https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data)

### Creation of Dataset and Annotating Images of Dataset using Roboflow 
[ROBOFLOW](https://www.youtube.com/watch?v=x0ThXHbtqCQ&ab_channel=Roboflow)

### Some Helpfull Links :
- [Coco labels format -> Yolo format (Python Implementation)](https://medium.com/red-buffer/converting-a-custom-dataset-from-coco-format-to-yolo-format-6d98a4fd43fc)
- [PASCAL VOC XML format -> Yolo format](https://towardsdatascience.com/convert-pascal-voc-xml-to-yolo-for-object-detection-f969811ccba5)
- [Problems while training large models](https://medium.com/augmented-startups/the-4-problems-with-training-models-in-colab-9135d9702359)
- [CallBacks & Saving Models](https://towardsdatascience.com/keras-callbacks-and-how-to-save-your-model-from-overtraining-244fc1de8608)
- [Tensorflow guide for saving and loading models](https://www.tensorflow.org/tutorials/keras/save_and_load)
- [SCRATCH IMPLEMENTATION OF YOLOv5 (Not necessary to understand each line but good to get an overview)](https://medium.com/analytics-vidhya/object-detection-algorithm-yolo-v5-architecture-89e0a35472ef)
- [How to Import Files from Google Drive to Colab](https://saturncloud.io/blog/how-to-import-files-from-google-drive-to-colab/)

### [Implementation of Yolov3 Model in Google Collab using Tensorflow](https://colab.research.google.com/github/maticvl/dataHacker/blob/master/CNN/DataHacker_rs_%20YoloV3%20TF2.0.ipynb#scrollTo=E-sz8LcL01E7)

## TASK :)
We will be providing you a dataset that contains different classes of ANIMALS ( both  images and labels (for labels you will have to check if they are present in yolo format or else you have to convert them to yolo format ) , it is highly recommended to use yolov5 or yolov3 to train your model(in google collab).
Every one will use the images provided in the dataset only ,to train there yolo models ) .

Use of Pretrained model is strictly prohibited.

[Dataset_Link](https://drive.google.com/file/d/1uGLwPB7mnYWHFVQTbVhKOXWYWBds8h2O/view?usp=sharing)

[SUBMISSION_LINK](https://forms.gle/fCnRQobpDHTsoByK9)
Deadline : 26th July,2023 

Happy Learning !!!
