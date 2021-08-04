from math import sqrt, pi
from sympy import sin, cos, symbols

a = symbols('a')
b = symbols('b')
c = symbols('c')


x = -1209*sqrt(3) - 20.78125
y = 825*sqrt(3)/32 +229.6875
z = 67*sqrt(3)/8 +550.25

rx = 42.236789
ry = 34.228842
rz = 85.9764997

a = rx/pi * 180
b = ry/pi *180
c = rz/pi * 180

euler_matrix = [
    [cos]
]

print(x,y,z)