# Mechanical Analysis
external libraries: numpy, sympy
### 1. Assign LinkFrames
### 2. Obtain Denavit-Hartenberg Kinematic Parameters
### 3. Formulate homogeneous transformation matrix with euler angle for each links
[Step 1,2,3 had done like here](https://github.com/skykongkong8/i611_RobotManipulator/blob/master/non_python_materials/analysis_trial.pdf)
```python
Changed_Like = {
   theta_1 : a,
   theta_2 : b,
   theta_3 : c,
   theta_4 : d,
   theta_5 : e,
   theta_6 : f,
   d_1 : u,
   d_2 : v,
   d_3 : w,
   d_4 : x,
   d_5 : y,
   d_6 : z,
   l_3 : l
}
```
### 4. Calculate homogeneous transformation matrix from GND to EndEffector
```python
Homogeneous_Transformation_Matrix=[
    [cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*cos(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*sin(e)*cos(f) + cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*sin(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*-cos(d)*(-1)*sin(f), cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*-sin(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*cos(e), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w)],
    [(sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(cos(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(sin(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e))*(z) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(x) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(l)*(cos(c)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(w)],
    [(sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(cos(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(sin(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(sin(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(-cos(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e))*(z) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(y) + (l)*(sin(c)) + (v) + (u)],
    [0,0,0,1]]
```
### 5. From endpoint position, obtain Jacobian matrix
```python
endpoint=[
    (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w),
    (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e))*(z) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(x) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(l)*(cos(c)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(w),
    (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e))*(z) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(y) + (l)*(sin(c)) + (v) + (u)
]
```
```python
Jacobian = [
    [-l*sin(b)*cos(a)*cos(c) + w*cos(a)*cos(b) - x*cos(a)*cos(b) + y*sin(b)*sin(c)*cos(a)*cos(d) - z*cos(a)*cos(b)*cos(e) - 3*sin(a)*sin(b) - 5*sin(a)*cos(b) + sin(b)*sin(c)*sin(d)*sin(e)*cos(a) - sin(b)*sin(d)*cos(a)*cos(c) - sin(b)*cos(a)*cos(c)*cos(d), -l*sin(a)*cos(b)*cos(c) - w*sin(a)*sin(b) + x*sin(a)*sin(b) + y*sin(a)*sin(c)*cos(b)*cos(d) + z*sin(a)*sin(b)*cos(e) + sin(a)*sin(c)*sin(d)*sin(e)*cos(b) - sin(a)*sin(d)*cos(b)*cos(c) - sin(a)*cos(b)*cos(c)*cos(d) - 5*sin(b)*cos(a) + 3*cos(a)*cos(b), l*sin(a)*sin(b)*sin(c) + y*sin(a)*sin(b)*cos(c)*cos(d) + sin(a)*sin(b)*sin(c)*sin(d) + sin(a)*sin(b)*sin(c)*cos(d) + sin(a)*sin(b)*sin(d)*sin(e)*cos(c), -y*sin(a)*sin(b)*sin(c)*sin(d) + sin(a)*sin(b)*sin(c)*sin(e)*cos(d) + sin(a)*sin(b)*sin(d)*cos(c) - sin(a)*sin(b)*cos(c)*cos(d), z*sin(a)*sin(e)*cos(b) + sin(a)*sin(b)*sin(c)*sin(d)*cos(e), 0],
    [-l*sin(a)*sin(b)*cos(c) + w*sin(a)*cos(b) - x*sin(a)*cos(b) + y*sin(a)*sin(b)*sin(c)*cos(d) - z*sin(a)*cos(b)*cos(e) + sin(a)*sin(b)*sin(c)*sin(d)*sin(e) - sin(a)*sin(b)*sin(d)*cos(c) - sin(a)*sin(b)*cos(c)*cos(d) + 3*sin(b)*cos(a) + 5*cos(a)*cos(b), l*cos(a)*cos(b)*cos(c) + w*sin(b)*cos(a) - x*sin(b)*cos(a) - y*sin(c)*cos(a)*cos(b)*cos(d) - z*sin(b)*cos(a)*cos(e) - 5*sin(a)*sin(b) + 3*sin(a)*cos(b) - sin(c)*sin(d)*sin(e)*cos(a)*cos(b) + sin(d)*cos(a)*cos(b)*cos(c) + cos(a)*cos(b)*cos(c)*cos(d), -l*sin(b)*sin(c)*cos(a) - y*sin(b)*cos(a)*cos(c)*cos(d) - sin(b)*sin(c)*sin(d)*cos(a) - sin(b)*sin(c)*cos(a)*cos(d) - sin(b)*sin(d)*sin(e)*cos(a)*cos(c), y*sin(b)*sin(c)*sin(d)*cos(a) - sin(b)*sin(c)*sin(e)*cos(a)*cos(d) - sin(b)*sin(d)*cos(a)*cos(c) + sin(b)*cos(a)*cos(c)*cos(d), -z*sin(e)*cos(a)*cos(b) - sin(b)*sin(c)*sin(d)*cos(a)*cos(e), 0], 
    [0, 0, l*cos(c) - y*sin(c)*cos(d) - z*sin(c)*sin(d)*sin(e) + sin(d)*cos(c) + cos(c)*cos(d), -y*sin(d)*cos(c) + z*sin(e)*cos(c)*cos(d) - sin(c)*sin(d) + sin(c)*cos(d), z*sin(d)*cos(c)*cos(e), 0]]
```
### 6. Since Jacobian is not square matrix, compute Psuedo-Inverse-Matrix
```python
jacobian = Matrix(Jacobian)
psuedo_inv_jacobian = jacobian.T*((jacobian * jacobian.T)**-1)
```
### 7. Calculate Endpoint Compliance with Servo Stiffness matrix
```python
# Servo Stiffness
K = Matrix([
    [1,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,1,0,0,0],
    [0,0,0,0.15,0,0],
    [0,0,0,0,0.27,0],
    [0,0,0,0,0,0.33]])
```
```python
Compliance = psuedo_inv_jacobian * (K**-1) * (psuedo_inv_jacobian.T)
```

### 8. Obtain eigen values and eigen vectors via optimization problem
```python
# Typically, we use determinant of subtraction between squared compliance and identical matrix multiplied by lambda to obtain eigen values but here, we have abstracted functions
squared_compliance = Compliance * Compliance

# Eigen vectors represent the directions of each force when it is maximized or minimized
eigenvalues = squared_compliance.eigenvals()
eigenvectors = squared_compliance.eigenvects()
```