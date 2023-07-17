**OBJECT DETECTION**

One of the important fields of Artificial Intelligence is Computer Vision. Computer Vision is the science of computers and software systems that can recognize and understand images and scenes. Computer Vision is also composed of various aspects such as image recognition, object detection, image generation, image super-resolution and more. Object detection is probably the most profound aspect of computer vision due the number practical use cases

Object detection refers to the capability of computer and software systems to locate objects in an image/scene and identify each object. Object detection has been widely used for face detection, vehicle detection, pedestrian counting, web images, security systems and driverless cars. There are many ways object detection can be used as well in many fields of practice. Like every other computer technology, a wide range of creative and amazing uses of object detection will definitely come from the efforts of computer programmers and software developers

**IMAGE AI**

One of the most famous CV libraries is OpenCV, since the accuracy of its  algorithms are not the best. Other object detection algorithms like RCNN, fast RCNN, faster RCNN, Retinanet and YOLO were used and better accuracies were obtained.

In this tutorial we will make use of ImageAI, a python library that helps beginners with object detection in short lines of code which is easy to understand and execute.

REQUIREMENTS OF SYSTEM

To perform object detection using ImageAI, all you need to do is
* Install Python on your computer system
* Install ImageAI and its dependencies
* Download the Object Detection model file(resnet50_coco_best_v2.1.0.h5)
* Run the sample codes (which is as few as 10 lines)

![img ins](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/114572870/90c72dfb-145c-4cf1-b60e-c7d6b6546639)
* Download model from (https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5/)

**CODE FOR OBJECT DETECTION**


from imageai.Detection import ObjectDetection

import os

execution_path = os.getcwd()

detector = ObjectDetection()

detector.setModelTypeAsRetinaNet()

detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))

detector.loadModel()

detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

for eachObject in detections:

    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

**IMAGES BEFORE DETECTION**
![imgai 1](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/114572870/ae3fa456-a3d7-4087-9009-24cbc6f60136)

![imagai 2](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/114572870/ec94f928-ce2e-4497-ae05-773cee22f1da)

**AFTER DETECTION**

![imagai 3](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/114572870/35347de1-f0e0-4cb4-9127-ae219804525f)

Console result for above image:

person : 55.8402955532074

person : 53.21805477142334

person : 69.25139427185059

person : 76.41745209693909

bicycle : 80.30363917350769

person : 83.58567953109741

person : 89.06581997871399

truck : 63.10953497886658

person : 69.82483863830566

person : 77.11606621742249

bus : 98.00949096679688

truck : 84.02870297431946

car : 71.98476791381836

![imagai 4](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/assets/114572870/cf715e88-6d6a-476b-92d7-4a6a703afbfb)

Console result for above image:

person : 71.10445499420166

person : 59.28672552108765

person : 59.61582064628601

person : 75.86382627487183

motorcycle : 60.1050078868866

bus : 99.39600229263306

car : 74.05484318733215

person : 67.31776595115662

person : 63.53200078010559

person : 78.2265305519104

person : 62.880998849868774

person : 72.93365597724915

person : 60.01397967338562

person : 81.05944991111755

motorcycle : 50.591760873794556

motorcycle : 58.719027042388916

person : 71.69321775436401

bicycle : 91.86570048332214

motorcycle : 85.38855314254761

**CODE EXPLANATION**

We imported the ImageAI object detection class in the first line, imported the python os class in the second line and defined a variable to hold the path to the folder where our python file, RetinaNet model file and images are in the third line

Then we defined our object detection class, set the model type to RetinaNet, set the model path to the path of our RetinaNet model, load the model into the object detection class, then we called the detection function and parsed in the input image path and the output image path.

**CONCLUSION**

This is the basic object detection tutorial for beginners, I hope you guys has got some basic knowledge about object detection, it has many uses in real life innovations, make sure to master object detection and CV libraries
