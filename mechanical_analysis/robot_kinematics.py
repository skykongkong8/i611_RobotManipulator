
###########################################
#i611 Robot Kinmatics Analysis with Python#
###########################################

from sympy import sin, cos, symbols, diff
from sympy.abc import a,b,c,d,e,f,u,v,w,x,y,z,l

"""Step#1 Assign Link Frames"""
"""Step#2 Obtain Denavit Hartenberg Kinematic Parameters"""
"""Step#3 Compute homogeneous transformation matrix with euler angles"""
"""Step#4 Calculate homogeneous transformation matrix from GND to End-Effector"""

result_4 = [['', '', '', ''],
        ['', '', '', ''],
        ['', '', '', ''],
        ['','','','']]
result_3 = [['','',''],
        ['','',''],
        ['','','']]

def matrix_with_variables_calculator(A,B, result):
    flag = False
    for i in range(len(A)): 
        for j in range(len(B[0])):  
            for k in range(len(B)):
                try:
                    if (A[i][k] != '0' and B[k][j] != '0'):
                        if result[i][j] == '1':
                            result[i][j] = (A[i][k] + B[k][j])
                            result[i][j] += ' + '
                        elif A[i][k] == '1':
                            result[i][j] += B[k][j]
                            result[i][j] += ' + '
                        elif B[k][j] == '1':
                            result[i][j] += A[i][k]
                            result[i][j] += ' + '
                        else:
                            result[i][j] += (A[i][k] + B[k][j])
                            result[i][j] += ' + '
                    
                    else:
                        pass
                except:
                    flag = True
                    print('\nERROR : INVALID MATRIX! BUT RESULT MAYBE STILL NOTEWORTHY!')
                if flag:
                    break
            if flag:
                break
        if flag:
            break
    return result

            
def matrix_prettier(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == '':
               matrix[i][j] = '0'
            if matrix[i][j][-1] == ' ':
                matrix[i][j] = matrix[i][j][:-3]
    return matrix

def matrix_printer(matrix):
    for i in range(len(matrix)):
        line = ''
        for j in range(len(matrix[0])):
            line+=matrix[i][j]
            line+='\t'
        print(line)




M1 =[
    ['(c_1)','(-s_1)','0','0'],
    ['(s_1)', '(c_1)', '0','0'],
    ['0', '0','1', '(d_1)'],
    ['0','0','0','1']
]

M2 = [
    ['(c_2)', '0', '(s_2)', '0'],
    ['(s_2)', '0', '(-c_2)', '0'],
    ['0', '1', '0', '(d_2)'],
    ['0','0','0','1']
]

M3 = [
    ['(c_3)','(s_3)','0','(l_3)(c_3)'],
    ['(s_3)', '(-c_3)', '0','(l_3)(s_3)'],
    ['0', '0','(-1)', '(d_3)'],
    ['0','0','0','1']
]

M4 = [
    ['(c_4)', '0', '(s_4)', '0'],
    ['(s_4)', '0', '(-c_4)', '0'],
    ['0', '1', '0', '(d_4)'],
    ['0','0','0','1']
]

M5 = [
    ['(c_5)', '0', '(-s_5)', '0'],
        ['(s_5)', '0', '(c_5)', '0'],
        ['0', '(-1)', '0', '(d_5)'],
        ['0','0','0','1']
]

M6 = [
    ['(c_6)', '0', '(s_6)', '0'],
    ['(s_6)', '0', '(-c_6)', '0'],
    ['0', '1', '0', '(d_6)'],
    ['0','0','0','1']
]

# matrix_list =[M1, M2, M3, M4, M5, M6]
matrix_list =[[
    ['(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(c_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(s_5)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(-1)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(-s_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(c_5)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(d_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(d_4) + (c_1)(c_2) + (-s_1)(s_2)(l_3)(c_3) + (c_1)(s_2) + (-s_1)(-c_2)(d_3)'], 
    ['(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(c_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(s_5)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(-1)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(-s_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(c_5)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(d_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(d_4) + (s_1)(c_2) + (c_1)(s_2)(l_3)(c_3) + (s_1)(s_2) + (c_1)(-c_2)(d_3)'], 
    ['(s_3)(c_4) + (-c_3)(s_4)(c_5)', '(s_3)(s_4) + (-c_3)(-c_4)(-1)', '(s_3)(c_4) + (-c_3)(s_4)(-s_5)', '(s_3)(s_4) + (-c_3)(-c_4)(d_5) + (l_3)(s_3) + (d_2) + (d_1)'], 
    ['0', '0', '0', '1']], M6]

# ACTUAL CALCULATING CODE
# if __name__ == "__main__":
    # new_matrix = matrix_prettier(matrix_with_variables_calculator(matrix_list[0],matrix_list[1],result))
    # for i in range(1,len(matrix_list)-1):
    #     new_matrix=matrix_prettier(matrix_with_variables_calculator(new_matrix, matrix_list[i+1], result))
    # print(new_matrix)



# matrix_printer(matrix_prettier(matrix_with_variables_calculator(A,B,result)))


#CALCULATION HISTORY -> get intermediate homogeneous transformation matrix if needed
M1M2 = [
    ['(c_1)(c_2) + (-s_1)(s_2)', '0', '(c_1)(s_2) + (-s_1)(-c_2)', '0'], 
    ['(s_1)(c_2) + (c_1)(s_2)', '0', '(s_1)(s_2) + (c_1)(-c_2)', '0'], 
    ['0', '1', '0', '(d_2) + (d_1)'], 
    ['0', '0', '0', '1']]

M1M2M3 = [
    ['(c_1)(c_2) + (-s_1)(s_2)(c_3)', '(c_1)(c_2) + (-s_1)(s_2)(s_3)', '(c_1)(s_2) + (-s_1)(-c_2)(-1)', '(c_1)(c_2) + (-s_1)(s_2)(l_3)(c_3) + (c_1)(s_2) + (-s_1)(-c_2)(d_3)'], 
    ['(s_1)(c_2) + (c_1)(s_2)(c_3)', '(s_1)(c_2) + (c_1)(s_2)(s_3)', '(s_1)(s_2) + (c_1)(-c_2)(-1)', '(s_1)(c_2) + (c_1)(s_2)(l_3)(c_3) + (s_1)(s_2) + (c_1)(-c_2)(d_3)'], 
    ['(s_3)', '(-c_3)', '0', '(l_3)(s_3) + (d_2) + (d_1)'], 
    ['0', '0', '0', '1']]
M1M2M3M4 = [
    ['(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)', '(c_1)(s_2) + (-s_1)(-c_2)(-1)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)', '(c_1)(s_2) + (-s_1)(-c_2)(-1)(d_4) + (c_1)(c_2) + (-s_1)(s_2)(l_3)(c_3) + (c_1)(s_2) + (-s_1)(-c_2)(d_3)'], 
    ['(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)', '(s_1)(s_2) + (c_1)(-c_2)(-1)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)', '(s_1)(s_2) + (c_1)(-c_2)(-1)(d_4) + (s_1)(c_2) + (c_1)(s_2)(l_3)(c_3) + (s_1)(s_2) + (c_1)(-c_2)(d_3)'], 
    ['(s_3)(c_4) + (-c_3)(s_4)', '0', '(s_3)(s_4) + (-c_3)(-c_4)', '(l_3)(s_3) + (d_2) + (d_1)'], 
    ['0', '0', '0', '1']]
M1M2M3M4M5 = [
    ['(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(c_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(s_5)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(-1)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(-s_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(c_5)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(d_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(d_4) + (c_1)(c_2) + (-s_1)(s_2)(l_3)(c_3) + (c_1)(s_2) + (-s_1)(-c_2)(d_3)'], 
    ['(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(c_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(s_5)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(-1)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(-s_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(c_5)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(d_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(d_4) + (s_1)(c_2) + (c_1)(s_2)(l_3)(c_3) + (s_1)(s_2) + (c_1)(-c_2)(d_3)'], 
    ['(s_3)(c_4) + (-c_3)(s_4)(c_5)', '(s_3)(s_4) + (-c_3)(-c_4)(-1)', '(s_3)(c_4) + (-c_3)(s_4)(-s_5)', '(s_3)(s_4) + (-c_3)(-c_4)(d_5) + (l_3)(s_3) + (d_2) + (d_1)'], 
    ['0', '0', '0', '1']]
M1M2M3M4M5M6 = [['(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(c_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(s_5)(c_6) + (c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(-1)(s_6)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(-s_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(c_5)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(c_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(s_5)(s_6) + (c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(-1)(-c_6)', '(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(-s_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(c_5)(d_6) + (c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(d_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(d_4) + (c_1)(c_2) + (-s_1)(s_2)(l_3)(c_3) + (c_1)(s_2) + (-s_1)(-c_2)(d_3)'], 
['(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(c_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(s_5)(c_6) + (s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(-1)(s_6)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(-s_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(c_5)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(c_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(s_5)(s_6) + (s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(-1)(-c_6)', '(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(-s_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(c_5)(d_6) + (s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(d_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(d_4) + (s_1)(c_2) + (c_1)(s_2)(l_3)(c_3) + (s_1)(s_2) + (c_1)(-c_2)(d_3)'], 
['(s_3)(c_4) + (-c_3)(s_4)(c_5)(c_6) + (s_3)(s_4) + (-c_3)(-c_4)(-1)(s_6)', '(s_3)(c_4) + (-c_3)(s_4)(-s_5)', '(s_3)(c_4) + (-c_3)(s_4)(c_5)(s_6) + (s_3)(s_4) + (-c_3)(-c_4)(-1)(-c_6)', '(s_3)(c_4) + (-c_3)(s_4)(-s_5)(d_6) + (s_3)(s_4) + (-c_3)(-c_4)(d_5) + (l_3)(s_3) + (d_2) + (d_1)'], 
['0', '0', '0', '1']]

# Final Endpoint Position:
endpoint = {
    'x' : '(c_1)(c_2) + (-s_1)(s_2)(c_3)(c_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(s_4)(-s_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(c_5)(d_6) + (c_1)(c_2) + (-s_1)(s_2)(c_3)(s_4) + (c_1)(c_2) + (-s_1)(s_2)(s_3)(-c_4)(d_5) + (c_1)(s_2) + (-s_1)(-c_2)(-1)(d_4) + (c_1)(c_2) + (-s_1)(s_2)(l_3)(c_3) + (c_1)(s_2) + (-s_1)(-c_2)(d_3)',
    'y' : '(s_1)(c_2) + (c_1)(s_2)(c_3)(c_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(s_4)(-s_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(c_5)(d_6) + (s_1)(c_2) + (c_1)(s_2)(c_3)(s_4) + (s_1)(c_2) + (c_1)(s_2)(s_3)(-c_4)(d_5) + (s_1)(s_2) + (c_1)(-c_2)(-1)(d_4) + (s_1)(c_2) + (c_1)(s_2)(l_3)(c_3) + (s_1)(s_2) + (c_1)(-c_2)(d_3)',
    'z' : '(s_3)(c_4) + (-c_3)(s_4)(-s_5)(d_6) + (s_3)(s_4) + (-c_3)(-c_4)(d_5) + (l_3)(s_3) + (d_2) + (d_1)'
}

# Changed_Like = {
#    theta_1 : a,
#    theta_2 : b,
#    theta_3 : c,
#    theta_4 : d,
#    theta_5 : e,
#    theta_6 : f,
#    d_1 : u,
#    d_2 : v,
#    d_3 : w,
#    d_4 : x,
#    d_5 : y,
#    d_6 : z,
#    l_3 : l
# }

# Constant_Values : LinkLength, Joint Offset at R-joint:
# d_1 = 145 mm
# d_2 = 135 mm
# d_3 = 135 mm
# d_4 = 270 mm
# d_5 = 100 mm
# d_6 = 65 mm
# 
# l_3 = 390 mm 

"""Step#5 Obtain Jacobian Matrix"""

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


"""
With Homogeneous Transformation Matrix, we can obtain endpoint position and orientation with joint angles, and check if it is singular point or not!
"""
"""[
    [cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*cos(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*sin(e)*cos(f) + cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*sin(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*-cos(d)*(-1)*sin(f), cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*-sin(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*cos(e), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w)], 
    [(sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(cos(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(sin(d))(cos(e)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(sin(e))(cos(f)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(sin(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(-cos(d))(-1)(sin(f)), (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(cos(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(sin(d))(-sin(e)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(cos(e)), (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(cos(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(sin(d))(cos(e)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(sin(e))(sin(f)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(sin(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(-cos(d))(-1)(-cos(f)), (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(cos(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(sin(d))(-sin(e)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(cos(e))(z) + (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(sin(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(-cos(d))(y) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(x) + (sin(a))(cos(b)) + (cos(a))(sin(b))(l)(cos(c)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(w)], 
    [(sin(c))(cos(d)) + (-cos(c))(sin(d))(cos(e))(cos(f)) + (sin(c))(sin(d)) + (-cos(c))(-cos(d))(-1)(sin(f)), (sin(c))(cos(d)) + (-cos(c))(sin(d))(-sin(e)), (sin(c))(cos(d)) + (-cos(c))(sin(d))(cos(e))(sin(f)) + (sin(c))(sin(d)) + (-cos(c))(-cos(d))(-1)(-cos(f)), (sin(c))(cos(d)) + (-cos(c))(sin(d))(-sin(e))(z) + (sin(c))(sin(d)) + (-cos(c))(-cos(d))(y) + (l)(sin(c)) + (v) + (u)], 
    [0,0,0,1]]"""
Homogeneous_Transformation_Matrix=[
    [cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*cos(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*sin(e)*cos(f) + cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*sin(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*-cos(d)*(-1)*sin(f), cos(a)*cos(b) + -sin(a)*sin(b)*cos(c)*cos(d) + cos(a)*cos(b) + -sin(a)*sin(b)*sin(c)*sin(d)*-sin(e) + cos(a)*sin(b) + -sin(a)*-cos(b)*(-1)*cos(e), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + 
(-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w)],
    [(sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(cos(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(sin(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(cos(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(sin(e))*(sin(f)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(-1)*(-cos(f)), (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e))*(z) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(x) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(l)*(cos(c)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(w)],
    [(sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(cos(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(sin(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(cos(e))*(sin(f)) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(-1)*(-cos(f)), (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e))*(z) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(y) + (l)*(sin(c)) + (v) + (u)],
    [0,0,0,1]]

endpoint=[
    (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(cos(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(cos(e))*(z) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(cos(c))*(sin(d)) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(-1)*(x) + (cos(a))*(cos(b)) + (-sin(a))*(sin(b))*(l)*(cos(c)) + (cos(a))*(sin(b)) + (-sin(a))*(-cos(b))*(w),
    (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(cos(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(sin(d))*(-sin(e)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(cos(e))*(z) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(cos(c))*(sin(d)) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(sin(c))*(-cos(d))*(y) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(-1)*(x) + (sin(a))*(cos(b)) + (cos(a))*(sin(b))*(l)*(cos(c)) + (sin(a))*(sin(b)) + (cos(a))*(-cos(b))*(w),
    (sin(c))*(cos(d)) + (-cos(c))*(sin(d))*(-sin(e))*(z) + (sin(c))*(sin(d)) + (-cos(c))*(-cos(d))*(y) + (l)*(sin(c)) + (v) + (u)
]

variable_list = [a,b,c,d,e,f]
Jacobian = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
for i in range(len(Jacobian[0])):
    for j in range(len(Jacobian)):
        Jacobian[j][i] = endpoint[j].diff(variable_list[i])

# print(Jacobian)
    
# # 3x6 matrix
# Jacobian = [0,0,0]
# variable_dict = {
#     0 : a,
#     1 : b,
#     2 : c,
#     3 : d,
#     4 : e,
#     5 : f
# }

# for i in range(len(Jacobian)):
#     Jacobian[i] = diff(endpoint[i], a, b, c, d, e, f)

# print(Jacobian)

"""Step#6 Inv Velocity Kinematics"""
"""Step#7 Obtain Endpoint Compliance with Servo Stiffness"""
"""Step#8 Optimize Problem : with eigenvalue, eigenvector, with determinant of (C^2-Ih)"""

"""Next : Robot Statics and Dynamics"""