Before starting with the main functions of PyBullet, let's play with some cool features in it.
# Get KeyBoard or Mouse inputs
Taking a real world analogy, suppose you wish that on pressing a specific button, the robot does some particular tasks, and on pressing some other button, another set of tasks should be done. Although, we won't be making an actual button-signal system over here, but the idea is to command the robot based on the given inputs..
<br>
<p align="center">
  <img width=500 src="https://user-images.githubusercontent.com/77807055/170840626-6cd4c50c-d81d-4143-9e4e-2728d5b33c1f.gif">
  <br><i>Let me give command to the robot</i>
  </p>
  
This can be done by giving inputs using keyboard or mouse, and let the robot react accordingly.
#### How to implement it?
## getKeyboardEvents
#### Follow the words of the bible...
> You can receive all keyboard events that happened since the last time you called 'getKeyboardEvents'. Each event has a keycode and a state. The state is a bit flag combination of KEY_IS_DOWN, KEY_WAS_TRIGGERED and KEY_WAS_RELEASED. If a key is going from 'up' to 'down' state, you receive the KEY_IS_DOWN state, as well as the KEY_WAS_TRIGGERED state. If a key was pressed and released, the state will be KEY_IS_DOWN and KEY_WAS_RELEASED.

> Some special keys are defined: B3G_F1 … B3G_F12, B3G_LEFT_ARROW, B3G_RIGHT_ARROW, B3G_UP_ARROW, B3G_DOWN_ARROW, B3G_PAGE_UP, B3G_PAGE_DOWN, B3G_PAGE_END, B3G_HOME, B3G_DELETE, B3G_INSERT, B3G_ALT, B3G_SHIFT, B3G_CONTROL, B3G_RETURN.

> The input of getKeyboardEvents is an optional physicsClientId:

> |optional|physicsClientId|int|if you are connected to multiple servers, you can pick one|
> |---|---|---|---|

> The output is a dictionary of keycode 'key' and keyboard state 'value'.

#### Check out [this code - KeyboardInputs.py](KeyboardInputs.py) to test the above function, where spheres are spawned at locations depending on the pressed keys. URDF of the sphere can be accessed from [here](https://github.com/Robotics-Club-IIT-BHU/Robotics-Camp-2023/blob/main/Mastering__Pybullet/PART_1/(3)%20Cool%20Features/sphere.urdf). Make sure that the pybullet window is selected while giving inputs
## getMouseEvents
Mouse events include the movements of the pointer as well as triggering of any mouse button. Let's look what bible has to say for that...
> Similar to getKeyboardEvents, you can get the mouse events that happened since the last callto getMouseEvents. All the mouse move events are merged into a single mouse move eventwith the most up-to-date position. In addition, all mouse button events for a given button aremerged. If a button went down and up, the state will be 'KEY_WAS_TRIGGERED '. We reuse the KEY_WAS_TRIGGERED /KEY_IS_DOWN /KEY_WAS_RELEASED for the mouse button states.

> Input arguments to getMouseEvents are:

> |optional|physicsClientId|int|if you are connected to multiple servers, you can pick one|
> |---|---|---|---|

> The output is a list of mouse events in the following format:

> |eventType|int|MOUSE_MOVE_EVENT=1, MOUSE_BUTTON_EVENT=2|
> |:---:|:---:|:---:|
> |**mousePosX**|**float**|**x-coordinates of the mouse pointer**|
> |**mousePosY**|**float**|**y-coordinates of the mouse pointer**|
> |**buttonIndex**|**int**|**button index for left/middle/right mouse button**|
> |**buttonState**|**int**|**flag KEY_WAS_TRIGGERED /KEY_IS_DOWN /KEY_WAS_RELEASED**|

#### Check out [this kool implementation - MouseInputs.py](MouseInputs.py) of the above function and watch the spheres being spawned as you move the pointer. Again, this will work only when your pointer will hover over the simulation window.
<br>
<p align="center">
  <img width="500" src="https://user-images.githubusercontent.com/77807055/170861742-00286866-183b-4934-8ca2-c31f9b9a2963.gif"><br>
  <i>Inputs...Inputs everywhere!!!</i>
</p>

#### Now that you know, how to give inputs to the system, it's time to fill it with colors🎨🖌
# Draw Lines (Function - addUserDebugLine)
Sometimes, it is useful to draw lines in 3D space of the simulation world for visualization purpose, and pybullet surely provides the utility. You can add a 3d line specified by a 3d starting point (from) and end point (to), a color [red,green,blue], a line width and a duration in seconds. The arguments to addUserDebugline are:

|optional/required|parameter name|data type|description|
|:---------------:|:----------:|:------:|:---------:|
|required|lineFromXYZ|vec3, list of 3 floats|starting point of the line in Cartesian world coordinates|
|required|lineToXYZ|vec3, list of 3 floats|end point of the line in Cartesian world coordinates|
|optional|lineColorRGB|vec3, list of 3 floats|RGB color [Red, Green, Blue] each component in range [0..1]|
|optional|lineWidth|float|line width (limited by OpenGL implementation)|
|optional|lifeTime|float|use 0 for permanent line, or positive time in seconds (afterwards the line with be removed automatically)|
|optional|parentObjectUniqueId|int|draw line in local coordinates of a parent object/link|
|optional|parentLinkIndex|int|draw line in local coordinates of a parent object/link|
|optional|replaceItemUniqueId|int|replace an existing line (to improve performance and to avoid flickering of remove/add)|
|optional|physicsClientId|int|if you are connected to multiple servers, you can pick one|

addUserDebugLine will return a non-negative unique id, that lets you remove the line using removeUserDebugItem.

    LineID = p.addUserDebugLine([0,0,0], [1,1,1], [0,0,1], 2, 0) # This will draw a permanent blue line from origin to (1,1,1)

# Add Text (Function - addUserDebugText)
You can add some 3d text at a specific location using a color and size. The input arguments are:

|optional/required|parameter name|data type|description|
|:---------------:|:----------:|:------:|:---------:|
|required|text|string|text represented as a string (array of characters)|
|required|textPosition|vec3, list of 3 floats|3d position of the text in Cartesian world coordinates [x,y,z]|
|optional|textColorRGB|vec3, list of 3 floats|RGB color [Red, Green, Blue] each component in range [0..1]|
|optional|textSize|float|Text size|
|optional|lifeTime|float|use 0 for permanent text, or positive time in seconds (afterwards the text with be removed automatically)|
|optional|textOrientation|vec4, list of 4 floats|By default, debug text will always face the camera, automatically rotation. By specifying a text orientation (quaternion), the orientation will be fixed in world space or local space (when parent is specified). Note that a different implementation/shader is used for camera facing text, with different appearance: camera facing text uses bitmap fonts, text with specified orientation uses TrueType fonts..|
|optional|parentObjectUniqueId|int|draw line in local coordinates of a parent object/link|
|optional|parentLinkIndex|int|draw line in local coordinates of a parent object/link|
|optional|replaceItemUniqueId|int|replace an existing text item (to avoid flickering of remove/add)|
|optional|physicsClientId|int|if you are connected to multiple servers, you can pick one|

addUserDebugText will return a non-negative unique id, that lets you remove the line using removeUserDebugItem.

    TextID = p.addUserDebugText("Hello", [1,1,1], [0,0,1], 1, 0, p.getQuaternionFromEuler([1.57,0,0])) # Play with it to get familiar with the features
    
# Creating trackbars (Function - addUserDebugParameter)
Sometimes, you need to tune some parameters to their optimal values. Changing the parameter manually everytime can be tedious, but if there is a trackbar where you can slide the button and change the values, it will be more handy. Here is how you can create one:<br>
addUserDebugParameter lets you add custom sliders and buttons to tune parameters. It will return a unique id. This lets you read the value of the parameter using readUserDebugParameter. The input parameters of addUserDebugParameter are:

|required/optional|parameter name|data type|description|
|:---------------:|:------------:|:-------:|:---------:|
|required|paramName|string|name of the parameter|
|required|rangeMin|float|minimum value. If Minimum value > maximum value a button instead of slider will appear|
|required|rangeMax|float|maximum value|
|required|startValue|float|starting value|
|optional|physicsClientId|int|if you are connected to multiple servers, you can pick one|

The input parameters of readUserDebugParameter are:

|required|itemUniqueId|int|the unique id returned by addUserDebugParameter|
|:---:|:---:|:---:|:---:|
|**optional**|**physicsClientId**|**int**|**if you are connected to multiple servers, you can pick one**|

Return value is the most up-to-date reading of the parameter, for a slider. For a button, the value of getUserDebugParameter for a button increases 1 at each button press.

Check out this implementation of [slider.py](slider.py) where the slider value is the x coordinate. If you change the value of slider, a new sphere will be spawned at that new x position.
<br>
<p align="center">
  <img width=500 src="https://media2.giphy.com/media/3oriO1ZZCvLseIxbTa/200w.webp?cid=ecf05e4746mt2f00zl2bv62hvx135ae7oaihtvw4sv5cf5t5&rid=200w.webp&ct=g"><br>
  <i>Slide! Slide! Slide!</i>
  </p>
  
# Getting an image from camera

<p align="middle">
 <img  width="350" height="300" src="controlling-your-robot-using-a-camera-vs-autonomous-code-it-39558286.png"><br>
</p>

* An image from a camera in the simulator has lots of uses in Computer Vision-based controllers, Object detection, etc.
* There are **3 important functions** to get an image by placing camera anywhere in the simulator:
1. **computeViewMatrix**:

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | cameraEyePosition | vec3, list of 3 floats | eye position in Cartesian world coordinates
required  | cameraTargetPosition | vec3, list of 3 floats | position of the target (focus) point, in Cartesian world coordinates
required  | cameraUpVector | vec3, list of 3 floats | up vector of the camera, in Cartesian world coordinates
optional  | physicsClientId | int | unused,added for API consistency

* cameraEyePosition is the position where the camera is to be placed.
* cameraTargetPosition is the focal point of the camera
* cameraUpVector is a 3D vector that points in the general direction of “up” from the camera.
* Output is the 4x4 view matrix, stored as a list of 16 floats.

2.**computeProjectionMatrixFOV**

parameter type  | Name | type | Description
--- | --- | --- | ---
required  | fov | float | field of view
required  | aspect | float | aspect ratio
required  | nearVal | float | near plane distance
required  | farVal | float | far plane distance
optional  | physicsClientId | int | unused,added for API consistency

* field of view:  the field of view is that part of the world that is visible through the camera at a particular position and orientation in space; objects outside the FOV when the picture is taken are not recorded in the photo.
* aspect ration: the ratio of the width to the height of an image or screen.
* near plane distance: The distance from the camera to the nearest object in the scene.
* far plane distance: The distance from the camera to the farthest object in the scene.

3. **getCameraImage**

* View Matrix and Projection matrix computed above are used in this function to set the parameters of the camera
* You can refer to this documentation for a description of this function:
<div align="center">
 
 [getCameraImage](https://docs.google.com/document/d/10sXEhzFRSnvFcl3XxNGhnD4N2SedqwdAvK3dsihxVUA/preview#heading=h.u1jisfnt6984)
  
</div>

* Here is an example for your understanding of the above functions [camera_example.py](camera_example.py)
* Try to change different parameters in the above example and see how the image changes.

# Task for the Part
- For this part, you need to spawn a sphere at some height at x=0, y=0.
- There should be a camera attached to the sphere, such that it points in y direction always.
- The camera should move with the sphere when the sphere falls.
- Also, spawn a cube along the y axis as shown in the video.
- When the sphere reaches at around 0.5 height, respawn the sphere at its current location and set the gravity to 0, so that the sphere stops there.
- Now, on pressing the key 'q', the text "Hurray!!" should be visible on the cube (in the simulation window).

**Note: You can play with the gravity's magnitude and can set it to any value, not necessarily -10.**
<br>
<p align="center">
  <a href="task.mp4"><img width=500 src="https://media3.giphy.com/media/Q59SaNn2vX1Sb8XIrf/200.webp?cid=ecf05e47rfui1d3iimcxprawfik07hmdmuv38je8hwtjquub&rid=200.webp&ct=g"></a><br>
  <i>You can have a look at the sample video by clicking above. Since the video is a bit large, please download it first. After every timestep, I am displaying the camera feed using cv2.imshow function. Left is the simulation window and on the right is the rendered image using cv2 function.</i>
  </p>
  
Make a video of the same and submit the video along with the code on the following link 👇
- [SUBMISSION_LINK](https://forms.gle/oMcCX2vf2m2jbfTS8)

