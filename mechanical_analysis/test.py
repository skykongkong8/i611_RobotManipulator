from sympy import sin, cos, abc, symbols, diff

x = symbols('x')
y = symbols('y')

variable_list = [x,y]

sine = (sin(x))*(-cos(y))
sine_diff = 0
for var in variable_list:
    sine_diff += sine.diff(var)

#sin_diff = sine.diff(x)
#print(sine_diff)

string_mat = """[
    (cos(a))(cos(b)) + (-sin(a))(sin(b))(cos(c))(cos(d)) + (cos(a))(cos(b)) + (-sin(a))(sin(b))(sin(c))(sin(d))(-sin(e)) + (cos(a))(sin(b)) + (-sin(a))(-cos(b))(-1)(cos(e))(z) + (cos(a))(cos(b)) + (-sin(a))(sin(b))(cos(c))(sin(d)) + (cos(a))(cos(b)) + (-sin(a))(sin(b))(sin(c))(-cos(d))(y) + (cos(a))(sin(b)) + (-sin(a))(-cos(b))(-1)(x) + (cos(a))(cos(b)) + (-sin(a))(sin(b))(l)(cos(c)) + (cos(a))(sin(b)) + (-sin(a))(-cos(b))(w),
    (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(cos(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(sin(d))(-sin(e)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(cos(e))(z) + (sin(a))(cos(b)) + (cos(a))(sin(b))(cos(c))(sin(d)) + (sin(a))(cos(b)) + (cos(a))(sin(b))(sin(c))(-cos(d))(y) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(-1)(x) + (sin(a))(cos(b)) + (cos(a))(sin(b))(l)(cos(c)) + (sin(a))(sin(b)) + (cos(a))(-cos(b))(w),
    (sin(c))(cos(d)) + (-cos(c))(sin(d))(-sin(e))(z) + (sin(c))(sin(d)) + (-cos(c))(-cos(d))(y) + (l)(sin(c)) + (v) + (u)
]"""

new_mat = string_mat.replace(')(', ')*(')
print(new_mat)