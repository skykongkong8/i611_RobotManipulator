# Zeus i611 Robot Arm and Manipulator

## Introduction
Since this robot system is based on the internal library from the manufacturer, the structure of the code is quite tricky to comprehend even with the distributed manual from [here](http://zero.globalzeus.com/scara/).    
Thus I would like to make more user-friendly interface of using it, in order to let the user to feel more comfortable when encountered the robot interface for the first time.    
This interface might not give you as sophisticated control as the original library, but *WAY* simpler, thus easier to adapt and proceed to real interface.   

## How to use (T.B.A.)
1. RUN main.py

## Structure (Temporary)
### mechanical_analysis
Here I tried to set mechanical model and solve the equation with Denavit-Hartenberg Kinematic Parameters and Homogenous Transformation Matrix with euler angles. (Basically Robot Forward Kinematics)   
In addition, this directory includes matrix calculator with characters, which can be utilized in versatile purposes.    

### non_python_materials
Here I tried to visualize the results made from mechanical_analysis directory. However since the matrix was too complex, I chosed to leave the files like this instead.   
Please click the image below or check this matrix. 
![ex_screenshot](./non_python_materials/homogeneous_transformation_matrix_img.png)   
```python
Homogeneous_Transformation_Matrix=[
    [cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*cos(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*sin(e)*cos(f) + cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*sin(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*-cos(d)*(-1)*sin(f), cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*-sin(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*cos(e), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w)],
    [(sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(cos(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(sin(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e))*(z) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(x) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(l)*(cos(c)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(w)],
    [(sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(cos(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(sin(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(sin(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(-cos(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e))*(z) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(y) + (l)*(sin(c)) + (v) + (u)],
    [0,0,0,1]]
```
for more information like this, please check [here](https://github.com/skykongkong8/i611_RobotManipulator/tree/master/mechanical_analysis)

### teleoperation
*This is just for test for now. Some codes might not work.*
#### robotarm_teleoperation_keyboard
* By Telnet connection (Tera Term recommended), after sending all the files via FFFTP, run:
```python
python main.py -keyboard
```
* keyboard operation
```command
_____________________________
| Moving around x-y plane:  |
|     w                     |
| a   s   d                 |
|     x                     |
|                           |
| Moving around z-axis:     |
|                           |
| h (high)   l (low)        |
|                           |
| u (undo)                  |
|___________________________|
```
#### robotarm_teleoperation_command
* By Telnet connection (Tera Term recommended), after sending all the files via FFFTP, run:
```python
python main.py -command (your_command)
```
* Command Examples:
```command
[axis control]
    +x -x
    +y -y
    +z -z

[additional control]
    -home
    -undo
```