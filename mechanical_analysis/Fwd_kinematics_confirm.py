from sympy import sin, cos, abc, symbols, pi, sqrt
from i611_MCS import *
from i611_extend import *

############################
#Section 1 : Our Prediction#
############################

a = symbols('a')
b = symbols('b')
c = symbols('c')
d = symbols('d')
e = symbols('e')
f = symbols('f')

u = symbols('u')
v = symbols('v')
w = symbols('w')
x = symbols('x')
y = symbols('y')
z = symbols('z')

l = symbols('l')

"""SI : mm"""
u = 145
v = 135
w = 135
x = 270
y = 100
z = 65
 
l = 390

"""SI : rad"""
a = pi/6
b = pi/6
c = pi/6
d = pi/6
e = pi/6
f = pi/6

Homogeneous_Transformation_Matrix=[
    [cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*cos(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*sin(e)*cos(f) + cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*sin(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*-cos(d)*(-1)*sin(f), cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*-sin(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*cos(e), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w)],
    [(sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(cos(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(sin(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e))*(z) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(x) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(l)*(cos(c)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(w)],
    [(sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(cos(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(sin(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(sin(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(-cos(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e))*(z) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(y) + (l)*(sin(c)) + (v) + (u)],
    [0,0,0,1]]

# print(Homogeneous_Transformation_Matrix)
result = [
    [sqrt(3)/8 + 21/8, sqrt(3)/4 + 31/32, 3*sqrt(3)/32 + 93/32, -1209*sqrt(3)/16 - 665/32], 
    [5/8 + 11*sqrt(3)/8, 1/4 + 33*sqrt(3)/32, 23/32 + 35*sqrt(3)/32, 825*sqrt(3)/32 + 3675/16], 
    [-1/8 + sqrt(3)/16, 3*sqrt(3)/8, 1/16 + 5*sqrt(3)/8, 67*sqrt(3)/8 + 2201/4], 
    [0, 0, 0, 1]]

# Orientation = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# for i in range(len(result)-1):
#     for j in range(len(result[0])-1):
#         Orientation[j][i] = result[j][i]
Orientation = [
    [sqrt(3)/8 + 2.625, sqrt(3)/4 + 0.96875, 3*sqrt(3)/32 + 2.90625], 
    [0.625 + 11*sqrt(3)/8, 0.25 + 33*sqrt(3)/32, 0.71875 + 35*sqrt(3)/32], 
    [-0.125 + sqrt(3)/16, 3*sqrt(3)/8, 0.0625 + 5*sqrt(3)/8]]

# Position = [0,0,0]
# for i in range(len(result)-1):
#     Position[i] = result[i][-1]
Position = [-1209*sqrt(3)/16 - 20.78125, 825*sqrt(3)/32 + 229.6875, 67*sqrt(3)/8 + 550.25]



##########################
#Section 2 : i611 library#
##########################

rb = i611Robot()
j1 = Joint(30,30,30,30,30,30)
p1 = rb.Joint2Position(j1)

print(p1)


"""
Compare p1 values with Orientation/Position from above. 
Especially use Euler transformation matrix or Roll-Pitch-Yaw matrix to clearly confirm rz, ry, rx
"""