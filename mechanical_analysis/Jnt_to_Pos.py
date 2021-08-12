from numpy.testing._private.utils import tempdir
from sympy import sin, cos, abc, symbols, pi, sqrt, Matrix
import numpy as np
from math import sqrt

class i611FwdKinematics():
    def __init__(self):
        self.true_value = [
        [100, 0, 870.307999],#0
        [332.5090, -352.8620,665.053],#30
        [491.596, -345.586, 459.361196089336701],#45
        [594.331999, -229.05199999,239.494]#60
        ]
        
        self.angle_list = [0, pi/6, pi/4, pi/3]

        self.position_list = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
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
    
