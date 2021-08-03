from sympy import sin, cos, abc, symbols, diff, pi, Matrix
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

# 3x6 matrix
Jacobian = [
    [-l*sin(b)*cos(a)*cos(c) + w*cos(a)*cos(b) - x*cos(a)*cos(b) + y*sin(b)*sin(c)*cos(a)*cos(d) - z*cos(a)*cos(b)*cos(e) - 3*sin(a)*sin(b) - 5*sin(a)*cos(b) + sin(b)*sin(c)*sin(d)*sin(e)*cos(a) - sin(b)*sin(d)*cos(a)*cos(c) - sin(b)*cos(a)*cos(c)*cos(d), -l*sin(a)*cos(b)*cos(c) - w*sin(a)*sin(b) + x*sin(a)*sin(b) + y*sin(a)*sin(c)*cos(b)*cos(d) + z*sin(a)*sin(b)*cos(e) + sin(a)*sin(c)*sin(d)*sin(e)*cos(b) - sin(a)*sin(d)*cos(b)*cos(c) - sin(a)*cos(b)*cos(c)*cos(d) - 5*sin(b)*cos(a) + 3*cos(a)*cos(b), l*sin(a)*sin(b)*sin(c) + y*sin(a)*sin(b)*cos(c)*cos(d) + sin(a)*sin(b)*sin(c)*sin(d) + sin(a)*sin(b)*sin(c)*cos(d) + sin(a)*sin(b)*sin(d)*sin(e)*cos(c), -y*sin(a)*sin(b)*sin(c)*sin(d) + sin(a)*sin(b)*sin(c)*sin(e)*cos(d) + sin(a)*sin(b)*sin(d)*cos(c) - sin(a)*sin(b)*cos(c)*cos(d), z*sin(a)*sin(e)*cos(b) + sin(a)*sin(b)*sin(c)*sin(d)*cos(e), 0],
    [-l*sin(a)*sin(b)*cos(c) + w*sin(a)*cos(b) - x*sin(a)*cos(b) + y*sin(a)*sin(b)*sin(c)*cos(d) - z*sin(a)*cos(b)*cos(e) + sin(a)*sin(b)*sin(c)*sin(d)*sin(e) - sin(a)*sin(b)*sin(d)*cos(c) - sin(a)*sin(b)*cos(c)*cos(d) + 3*sin(b)*cos(a) + 5*cos(a)*cos(b), l*cos(a)*cos(b)*cos(c) + w*sin(b)*cos(a) - x*sin(b)*cos(a) - y*sin(c)*cos(a)*cos(b)*cos(d) - z*sin(b)*cos(a)*cos(e) - 5*sin(a)*sin(b) + 3*sin(a)*cos(b) - sin(c)*sin(d)*sin(e)*cos(a)*cos(b) + sin(d)*cos(a)*cos(b)*cos(c) + cos(a)*cos(b)*cos(c)*cos(d), -l*sin(b)*sin(c)*cos(a) - y*sin(b)*cos(a)*cos(c)*cos(d) - sin(b)*sin(c)*sin(d)*cos(a) - sin(b)*sin(c)*cos(a)*cos(d) - sin(b)*sin(d)*sin(e)*cos(a)*cos(c), y*sin(b)*sin(c)*sin(d)*cos(a) - sin(b)*sin(c)*sin(e)*cos(a)*cos(d) - sin(b)*sin(d)*cos(a)*cos(c) + sin(b)*cos(a)*cos(c)*cos(d), -z*sin(e)*cos(a)*cos(b) - sin(b)*sin(c)*sin(d)*cos(a)*cos(e), 0], 
    [0, 0, l*cos(c) - y*sin(c)*cos(d) - z*sin(c)*sin(d)*sin(e) + sin(d)*cos(c) + cos(c)*cos(d), -y*sin(d)*cos(c) + z*sin(e)*cos(c)*cos(d) - sin(c)*sin(d) + sin(c)*cos(d), z*sin(d)*cos(c)*cos(e), 0]]

jacobian = Matrix(Jacobian)
psuedo_inv_jacobian = jacobian.T*((jacobian * jacobian.T)**-1)

print(psuedo_inv_jacobian)
# Servo Stiffness matrix from user manual (6*6 matrix) - approximated
