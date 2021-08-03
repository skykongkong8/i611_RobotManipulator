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
![ex_screenshot](./non_python_materials/homogeneous_transformation_matrix_img.png)    

### teleoperation
This is just for test. This code might not work.