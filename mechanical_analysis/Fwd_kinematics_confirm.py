from numpy.testing._private.utils import tempdir
from sympy import sin, cos, abc, symbols, pi, sqrt, Matrix
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

# """SI : mm"""
# u = 145
# v = 135
# w = 135
# x = 270
# y = 100
# z = 65
 
# l = 390
# l = 

# """SI : rad"""
# a = pi/6
# b = pi/6
# c = pi/6
# d = pi/6
# e = pi/6
# f = pi/6

"""Obtain Denavit-Hartenberg Kinematic Parameters"""
DH_params = [
    [0,0,a,u],
    [l,-pi/2,b,v],
    [0,0,c,w],
    [0, pi/2,d,x],
    [0,-pi/2,e,y],
    [0,pi/2,f,z]
]

def single_angle_i611_DH_params(angle):
    angle += -pi/2
    dh =[
    [0,-pi/2,angle ,145],
    [390,0,angle,135],
    [0,pi/2,angle,135],
    [0, -pi/2,angle,270],
    [0,pi/2,angle,100],
    [0,0,angle,65]
    ]

    return dh



"""Formulate homogeneous Transformation matrix for each link"""
# dh = DH_params
# i = 0
# homogeneous_matrix = [
#     [cos(dh[2]), -sin(dh[2])*cos(dh[1]), sin(dh[2])*sin(dh[1]), dh[0]*cos(dh[2])],
#     [sin(dh[2]), cos(dh[2])*cos(dh[1]), -cos(dh[2])*sin(dh[1]), dh[0]*sin(dh[2])],
#     [0, sin(dh[1]), cos(dh[1]), dh[3]],
#     [0,0,0,1]
# ]
def Homogeneous_Transformation_Matrix(DH_params):
    homogeneous_matricies = []
    for i in range(6):
        dh = DH_params[i]
        homogeneous_matricies.append([
            [cos(dh[2]), -sin(dh[2])*cos(dh[1]), sin(dh[2])*sin(dh[1]), dh[0]*cos(dh[2])],
            [sin(dh[2]), cos(dh[2])*cos(dh[1]), -cos(dh[2])*sin(dh[1]), dh[0]*sin(dh[2])],
            [0, sin(dh[1]), cos(dh[1]), dh[3]],
            [0,0,0,1]])

    M1 = np.array(homogeneous_matricies[0])
    M2 = np.array(homogeneous_matricies[1])
    M3 = np.array(homogeneous_matricies[2])
    M4 = np.array(homogeneous_matricies[3])
    M5 = np.array(homogeneous_matricies[4])
    M6 = np.array(homogeneous_matricies[5])


    M1M2 = M1@M2
    # print(M1M2)

    M1M2M3 = np.dot(M1M2,M3)
    M1M2M3M4 = np.dot(M1M2M3, M4)

    M1M2M3M4M5 = np.dot(M1M2M3M4,M5)
    M1M2M3M4M5M6 = np.dot(M1M2M3M4M5,M6)


    result = M1M2M3M4M5M6
    return result


# Orientation = [
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# for i in range(len(result)-1):
#     for j in range(len(result[0])-1):
#         Orientation[j][i] = result[j][i]
# print(Orientation)

# Orientation = [[-sqrt(3)/8 - 3/16, -7/8, 3/8 - sqrt(3)/16]
#  , [-3/8 + 5*sqrt(3)/16, sqrt(3)/8, 5/16 + 3*sqrt(3)/8]
# , [-3*sqrt(3)/8 - 1/4, sqrt(3)/4, -3/8 + sqrt(3)/4]]

# Position = [0,0,0]
# for i in range(len(result)-1):
#     Position[i] = result[i][-1]
# Position = [-1209*sqrt(3)/16 - 20.78125, 825*sqrt(3)/32 + 229.6875, 67*sqrt(3)/8 + 550.25]


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

true_value = [
        [100, 0, 870.307999],#0
        [332.5090, -352.8620,665.053],#30
        [491.596, -345.586, 459.361196089336701],#45
        [594.331999, -229.05199999,239.494]#60
]
angle_list = [0, pi/6, pi/4, pi/3]

position_list = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
]

from math import sqrt

def calculate_and_print(Position):
    flag_list = [True, True, True]
    pos_list=[]
    for i in range(3):
        if Position[i] < 0:
            flag_list[i] = False
        pos_list.append((Position[i])**2)

        if flag_list[i]:
            pos_list[i]=sqrt(pos_list[i])
        else:
            pos_list[i] = -sqrt(pos_list[i])

    return pos_list

def switch_dimension_order(approx):
    tmp = approx[0]
    approx[0] = approx[1]
    approx[1] = tmp

    return approx


"""Print Result"""
if __name__ == '__main__':
    axis = ['x', 'y', 'z']
    approx = []

    for i in range(len(angle_list)):
        dh_params = single_angle_i611_DH_params(angle_list[i])                                    
        result = Homogeneous_Transformation_Matrix(dh_params)

        Position = [0,0,0]
        for i in range(len(result)-1):
            Position[i] = result[i][-1]

        
        approx.append(calculate_and_print(Position))
    

    cnt =0
    err_sum = 0
    for i in range(4):
        err = 0
        print(f"For {angle_list[i]} radian ")
        approx[i] = switch_dimension_order(approx[i])
        for j in range(3):
            print(f"Approx {axis[j]}: {approx[i][j]}\tTrue : {true_value[i][j]}")
            try:
                abs_diff = abs((abs(approx[i][j]) - abs(true_value[i][j]))/true_value[i][j])
            except:
                print("ZeroDivisionError! : compute with formal error.")
                pass
            err += abs_diff
        print(f"Error : {err*100}")
        print("\n")
        err_sum += err
        cnt +=1
    print(f"Total Average Error : {err_sum/cnt*100}")