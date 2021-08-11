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
    dh =[
    [0,0,angle,145],
    [390,-pi/2,angle,135],
    [0,0,angle,135],
    [0, pi/2,angle,270],
    [0,-pi/2,angle,100],
    [0,pi/2,angle,65]
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

    # print(homogeneous_matricies)

    M1 = np.array(homogeneous_matricies[0])
    M2 = np.array(homogeneous_matricies[1])
    # print(M1)
    # print(M2)
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





# all 60
# -503.76029715641096
# -2.4615704891007937
# 533.75
"""???
-631
218
278
"""
# all 45
# -450.9619
# 490
# 325.9619

# all 30
#x = -296.8140183434757
#y = 408.48634232239635
#z = 613.1458256229943
"""???
-169
629
358
"""


# Jacobian =[
#     [-l*sin(a)*cos(b) - l*sin(b)*cos(a) + w*(sin(a)*sin(b) - cos(a)*cos(b)) + x*(sin(a)*sin(b) - cos(a)*cos(b)) + y*((-sin(a)*cos(b) - sin(b)*cos(a))*sin(c)*cos(d) + (-sin(a)*cos(b) - sin(b)*cos(a))*sin(d)*cos(c)) + z*((sin(a)*sin(b) - cos(a)*cos(b))*cos(e) + (-(-sin(a)*cos(b) - sin(b)*cos(a))*cos(c)*cos(d) - (sin(a)*cos(b) + sin(b)*cos(a))*sin(c)*sin(d))*sin(e)), -l*sin(a)*cos(b) - l*sin(b)*cos(a) + w*(sin(a)*sin(b) - cos(a)*cos(b)) + x*(sin(a)*sin(b) - cos(a)*cos(b)) + y*((-sin(a)*cos(b) - sin(b)*cos(a))*sin(c)*cos(d) + (-sin(a)*cos(b) - sin(b)*cos(a))*sin(d)*cos(c)) + z*((sin(a)*sin(b) - cos(a)*cos(b))*cos(e) + (-(-sin(a)*cos(b) - sin(b)*cos(a))*cos(c)*cos(d) - (sin(a)*cos(b) + sin(b)*cos(a))*sin(c)*sin(d))*sin(e)), y*(-(-sin(a)*sin(b) + cos(a)*cos(b))*sin(c)*sin(d) + (-sin(a)*sin(b) + cos(a)*cos(b))*cos(c)*cos(d)) + z*((-sin(a)*sin(b) + cos(a)*cos(b))*sin(c)*cos(d) - (sin(a)*sin(b) - cos(a)*cos(b))*sin(d)*cos(c))*sin(e), y*(-(-sin(a)*sin(b) + cos(a)*cos(b))*sin(c)*sin(d) + (-sin(a)*sin(b) + cos(a)*cos(b))*cos(c)*cos(d)) + z*((-sin(a)*sin(b) + cos(a)*cos(b))*sin(d)*cos(c) - (sin(a)*sin(b) - cos(a)*cos(b))*sin(c)*cos(d))*sin(e), z*(-(-sin(a)*cos(b) - sin(b)*cos(a))*sin(e) + (-(-sin(a)*sin(b) + cos(a)*cos(b))*cos(c)*cos(d) - (sin(a)*sin(b) - cos(a)*cos(b))*sin(c)*sin(d))*cos(e)), 0], 
#     [-l*sin(a)*sin(b) + l*cos(a)*cos(b) + w*(-sin(a)*cos(b) - sin(b)*cos(a)) + x*(-sin(a)*cos(b) - sin(b)*cos(a)) + y*((-sin(a)*sin(b) + cos(a)*cos(b))*sin(c)*cos(d) + (-sin(a)*sin(b) + cos(a)*cos(b))*sin(d)*cos(c)) + z*((-sin(a)*cos(b) - sin(b)*cos(a))*cos(e) + (-(-sin(a)*sin(b) + cos(a)*cos(b))*cos(c)*cos(d) - (sin(a)*sin(b) - cos(a)*cos(b))*sin(c)*sin(d))*sin(e)), -l*sin(a)*sin(b) + l*cos(a)*cos(b) + w*(-sin(a)*cos(b) - sin(b)*cos(a)) + x*(-sin(a)*cos(b) - sin(b)*cos(a)) + y*((-sin(a)*sin(b) + cos(a)*cos(b))*sin(c)*cos(d) + (-sin(a)*sin(b) + cos(a)*cos(b))*sin(d)*cos(c)) + z*((-sin(a)*cos(b) - sin(b)*cos(a))*cos(e) + (-(-sin(a)*sin(b) + cos(a)*cos(b))*cos(c)*cos(d) - (sin(a)*sin(b) - cos(a)*cos(b))*sin(c)*sin(d))*sin(e)), y*(-(sin(a)*cos(b) + sin(b)*cos(a))*sin(c)*sin(d) + (sin(a)*cos(b) + sin(b)*cos(a))*cos(c)*cos(d)) + z*(-(-sin(a)*cos(b) - sin(b)*cos(a))*sin(d)*cos(c) + (sin(a)*cos(b) + sin(b)*cos(a))*sin(c)*cos(d))*sin(e), y*(-(sin(a)*cos(b) + sin(b)*cos(a))*sin(c)*sin(d) + (sin(a)*cos(b) + sin(b)*cos(a))*cos(c)*cos(d)) + z*(-(-sin(a)*cos(b) - sin(b)*cos(a))*sin(c)*cos(d) + (sin(a)*cos(b) + sin(b)*cos(a))*sin(d)*cos(c))*sin(e), z*(-(-sin(a)*sin(b) + cos(a)*cos(b))*sin(e) + (-(-sin(a)*cos(b) - sin(b)*cos(a))*sin(c)*sin(d) - (sin(a)*cos(b) + sin(b)*cos(a))*cos(c)*cos(d))*cos(e)), 0], 
#     [0, 0, y*(-sin(c)*cos(d) - sin(d)*cos(c)) - z*(sin(c)*sin(d) - cos(c)*cos(d))*sin(e), y*(-sin(c)*cos(d) - sin(d)*cos(c)) - z*(sin(c)*sin(d) - cos(c)*cos(d))*sin(e), -z*(-sin(c)*cos(d) - sin(d)*cos(c))*cos(e), 0]]

# # print(Jacobian)
# jacobian = Matrix(Jacobian)
# psuedo_inverse_matrix = jacobian.T * ((jacobian * jacobian.T)**-1)
# # print(psuedo_inverse_matrix)

# psuedo_inverse_matrix = Matrix([
#     [(-1625*sqrt(3)/8 - 555/2)*(318191855469046341347070409800*sqrt(3) + 551205801347830351314906246097)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000) + (-1006816121332318434990840 - 581017519140967441119809*sqrt(3))*(1105/8 - 355*sqrt(3)/2)/(39954503928463158137875200*sqrt(3) + 69687685573335823638996000), (1105/8 - 355*sqrt(3)/2)*(720556866041049743001608*sqrt(3) + 1248067475833304020049783)/(13318167976154386045958400*sqrt(3) + 23229228524445274546332000) + (-2049497787057041395383393946680 - 1183270218535585561065888701287*sqrt(3))*(-1625*sqrt(3)/8 - 555/2)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000), (1105/8 - 355*sqrt(3)/2)*(898909100802504998554244*sqrt(3) + 1556981511899889620768229)/(19977251964231579068937600*sqrt(3) + 34843842786667911819498000) + (-852225509914986189150134526820 - 492030085922764232336849119847*sqrt(3))*(-1625*sqrt(3)/8 - 555/2)/(40815708374757401621190625276800*sqrt(3) + 70702002284551986625366341798000)]
#     , [(-1625*sqrt(3)/8 - 555/2)*(318191855469046341347070409800*sqrt(3) + 551205801347830351314906246097)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000) + (-1006816121332318434990840 - 581017519140967441119809*sqrt(3))*(1105/8 - 355*sqrt(3)/2)/(39954503928463158137875200*sqrt(3) + 69687685573335823638996000), (1105/8 - 355*sqrt(3)/2)*(720556866041049743001608*sqrt(3) + 1248067475833304020049783)/(13318167976154386045958400*sqrt(3) + 23229228524445274546332000) + (-2049497787057041395383393946680 - 1183270218535585561065888701287*sqrt(3))*(-1625*sqrt(3)/8 - 555/2)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000), (1105/8 - 355*sqrt(3)/2)*(898909100802504998554244*sqrt(3) + 1556981511899889620768229)/(19977251964231579068937600*sqrt(3) + 34843842786667911819498000) + (-852225509914986189150134526820 - 492030085922764232336849119847*sqrt(3))*(-1625*sqrt(3)/8 - 555/2)/(40815708374757401621190625276800*sqrt(3) + 70702002284551986625366341798000)] 
#     ,[(-1006816121332318434990840 - 581017519140967441119809*sqrt(3))*(195/8 + 25*sqrt(3))/(39954503928463158137875200*sqrt(3) + 69687685573335823638996000) + (65*sqrt(3)/8 + 25)*(318191855469046341347070409800*sqrt(3) + 551205801347830351314906246097)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000) + (-914182685605332 - 520755438647311*sqrt(3))*(65/4 - 50*sqrt(3))/(37791977918198400*sqrt(3) + 85206534432130800), (65/4 - 50*sqrt(3))*(649877722633620*sqrt(3) + 1126308207830521)/(12597325972732800*sqrt(3) + 28402178144043600) + (-2049497787057041395383393946680 - 1183270218535585561065888701287*sqrt(3))*(65*sqrt(3)/8 + 25)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000) + (195/8 + 25*sqrt(3))*(720556866041049743001608*sqrt(3) + 1248067475833304020049783)/(13318167976154386045958400*sqrt(3) + 23229228524445274546332000), (65/4 - 50*sqrt(3))*(812444316575632*sqrt(3) + 1408276661385147)/(18895988959099200*sqrt(3) + 42603267216065400) + (-852225509914986189150134526820 - 492030085922764232336849119847*sqrt(3))*(65*sqrt(3)/8 + 25)/(40815708374757401621190625276800*sqrt(3) + 70702002284551986625366341798000) + (195/8 + 25*sqrt(3))*(898909100802504998554244*sqrt(3) + 1556981511899889620768229)/(19977251964231579068937600*sqrt(3) + 34843842786667911819498000)]
#     , [(-1006816121332318434990840 - 581017519140967441119809*sqrt(3))*(195/8 + 25*sqrt(3))/(39954503928463158137875200*sqrt(3) + 69687685573335823638996000) + (65*sqrt(3)/8 + 25)*(318191855469046341347070409800*sqrt(3) + 551205801347830351314906246097)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000) + (-914182685605332 - 520755438647311*sqrt(3))*(65/4 - 50*sqrt(3))/(37791977918198400*sqrt(3) + 85206534432130800), (65/4 - 50*sqrt(3))*(649877722633620*sqrt(3) + 1126308207830521)/(12597325972732800*sqrt(3) + 28402178144043600) + (-2049497787057041395383393946680 - 1183270218535585561065888701287*sqrt(3))*(65*sqrt(3)/8 + 25)/(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000) + (195/8 + 25*sqrt(3))*(720556866041049743001608*sqrt(3) + 1248067475833304020049783)/(13318167976154386045958400*sqrt(3) + 23229228524445274546332000), (65/4 - 50*sqrt(3))*(812444316575632*sqrt(3) + 1408276661385147)/(18895988959099200*sqrt(3) + 42603267216065400) + (-852225509914986189150134526820 - 492030085922764232336849119847*sqrt(3))*(65*sqrt(3)/8 + 25)/(40815708374757401621190625276800*sqrt(3) + 70702002284551986625366341798000) + (195/8 + 25*sqrt(3))*(898909100802504998554244*sqrt(3) + 1556981511899889620768229)/(19977251964231579068937600*sqrt(3) + 34843842786667911819498000)]
#     , [195*(-914182685605332 - 520755438647311*sqrt(3))/(4*(37791977918198400*sqrt(3) + 85206534432130800)) + 65*sqrt(3)*(318191855469046341347070409800*sqrt(3) + 551205801347830351314906246097)/(8*(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000)) - 325*(-1006816121332318434990840 - 581017519140967441119809*sqrt(3))/(8*(39954503928463158137875200*sqrt(3) + 69687685573335823638996000)), -325*(720556866041049743001608*sqrt(3) + 1248067475833304020049783)/(8*(13318167976154386045958400*sqrt(3) + 23229228524445274546332000)) + 65*sqrt(3)*(-2049497787057041395383393946680 - 1183270218535585561065888701287*sqrt(3))/(8*(81631416749514803242381250553600*sqrt(3) + 141404004569103973250732683596000)) + 195*(649877722633620*sqrt(3) + 1126308207830521)/(4*(12597325972732800*sqrt(3) + 28402178144043600)), -325*(898909100802504998554244*sqrt(3) + 1556981511899889620768229)/(8*(19977251964231579068937600*sqrt(3) + 34843842786667911819498000)) + 65*sqrt(3)*(-852225509914986189150134526820 - 492030085922764232336849119847*sqrt(3))/(8*(40815708374757401621190625276800*sqrt(3) + 70702002284551986625366341798000)) + 195*(812444316575632*sqrt(3) + 1408276661385147)/(4*(18895988959099200*sqrt(3) + 42603267216065400))]
#     , [0, 0, 0]])










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
    tmp = approx[1]
    approx[1] = approx[2]
    approx[2] = tmp

    return approx


"""Print Result"""
if __name__ == '__main__':
    approx = []

    for i in range(len(angle_list)):
        dh_params = single_angle_i611_DH_params(angle_list[i])                                    
        result = Homogeneous_Transformation_Matrix(dh_params)

        Position = [0,0,0]
        for i in range(len(result)-1):
            Position[i] = result[i][-1]

        
        approx.append(calculate_and_print(Position))
    

    cnt =0
    total_avg_err = 0
    for i in range(4):
        err = 0
        print(f"For {angle_list[i]} degree ")
        approx[i] = switch_dimension_order(approx[i])
        for j in range(3):
            print(f"Approx : {approx[i][j]}\tTrue : {true_value[i][j]}")
            try:
                abs_diff = abs((abs(approx[i][j]) - abs(true_value[i][j]))/true_value[i][j])
            except:
                print("ZeroDivisionError! : compute with formal error.")
                pass
            err += abs_diff
        print(f"Error : {err*100}")
        print("\n")
        if cnt > 1:
            total_avg_err += err
        cnt +=1
    cnt -=1
    print(f"Total Average Error : {total_avg_err/cnt*100}")