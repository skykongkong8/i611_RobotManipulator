from sympy import sin, cos, abc, symbols, pi, sqrt, Matrix

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

DH_params = [
    [0,0,a,u],
    [l,-pi/2,b,v],
    [0,0,c,w],
    [0, pi/2,d,x],
    [0,-pi/2,e,y],
    [0,pi/2,f,z]
]

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
print(M1)
print(M2)
M3 = np.array(homogeneous_matricies[2])
M4 = np.array(homogeneous_matricies[3])
M5 = np.array(homogeneous_matricies[4])
M6 = np.array(homogeneous_matricies[5])


M1M2 = M1@M2
print(M1M2)

M1M2M3 = np.dot(M1M2,M3)
M1M2M3M4 = np.dot(M1M2M3, M4)

M1M2M3M4M5 = np.dot(M1M2M3M4,M5)
M1M2M3M4M5M6 = np.dot(M1M2M3M4M5,M6)


result = M1M2M3M4M5M6

