from sympy import sin, cos, abc, symbols, pi, sqrt
# from i611_MCS import *
# from i611_extend import *

############################
#Section 1 : Our Prediction#
############################

import numpy as np


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

"""Obtain Denavit-Hartenberg Kinematic Parameters"""
DH_params = [
    [0,0,a,u],
    [l,-pi/2,b,v],
    [0,0,c,w],
    [0, pi/2,d,x],
    [0,-pi/2,e,y],
    [0,pi/2,f,z]
]

"""Formulate homogeneous Transformation matrix for each link"""
# dh = DH_params
# i = 0
# homogeneous_matrix = [
#     [cos(dh[2]), -sin(dh[2])*cos(dh[1]), sin(dh[2])*sin(dh[1]), dh[0]*cos(dh[2])],
#     [sin(dh[2]), cos(dh[2])*cos(dh[1]), -cos(dh[2])*sin(dh[1]), dh[0]*sin(dh[2])],
#     [0, sin(dh[1]), cos(dh[1]), dh[3]],
#     [0,0,0,1]
# ]

homogeneous_matricies = []
for i in range(6):
    dh = DH_params[i]
    homogeneous_matricies.append([[cos(dh[2]), -sin(dh[2])*cos(dh[1]), sin(dh[2])*sin(dh[1]), dh[0]*cos(dh[2])],
    [sin(dh[2]), cos(dh[2])*cos(dh[1]), -cos(dh[2])*sin(dh[1]), dh[0]*sin(dh[2])],
    [0, sin(dh[1]), cos(dh[1]), dh[3]],
    [0,0,0,1]])

# print(homogeneous_matricies)

M1 = np.array(homogeneous_matricies[0])
M2 = np.array(homogeneous_matricies[1])
M3 = np.array(homogeneous_matricies[2])
M4 = np.array(homogeneous_matricies[3])
M5 = np.array(homogeneous_matricies[4])
M6 = np.array(homogeneous_matricies[5])

M1M2 = np.dot(M1,M2)
M1M2M3 = np.dot(M1M2,M3)
M1M2M3M4 = np.dot(M1M2M3, M4)
M1M2M3M4M5 = np.dot(M1M2M3M4,M5)
M1M2M3M4M5M6 = np.dot(M1M2M3M4M5,M6)

result = M1M2M3M4M5M6
# print(result)

Orientation = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(result)-1):
    for j in range(len(result[0])-1):
        Orientation[j][i] = result[j][i]
print(Orientation)
# Orientation = [[-sqrt(3)/8 - 3/16, -7/8, 3/8 - sqrt(3)/16]
#  , [-3/8 + 5*sqrt(3)/16, sqrt(3)/8, 5/16 + 3*sqrt(3)/8]
# , [-3*sqrt(3)/8 - 1/4, sqrt(3)/4, -3/8 + sqrt(3)/4]]

Position = [0,0,0]
for i in range(len(result)-1):
    Position[i] = result[i][-1]
# Position = [-1209*sqrt(3)/16 - 20.78125, 825*sqrt(3)/32 + 229.6875, 67*sqrt(3)/8 + 550.25]
# if __name__ == '__main__':
#     print(f'x : {Position[0]}\n', f'y : {Position[1]}\n', f'z : {Position[2]}\n')

#x = -169.3140183434757
#y = 629.3228202874282
#z = 358.14582562299427











##########################
#Section 2 : i611 library#
##########################

# rb = i611Robot()
# j1 = Joint(30,30,30,30,30,30)
# p1 = rb.Joint2Position(j1)

# print(p1)


"""
Compare p1 values with Orientation/Position from above. 
Especially use Euler transformation matrix or Roll-Pitch-Yaw matrix to clearly confirm rz, ry, rx
"""