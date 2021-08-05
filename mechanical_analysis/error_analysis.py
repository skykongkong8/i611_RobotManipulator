from math import sqrt

# 30 - 45 - 60
predict = [
    [-296.814, 408.4863, 613.145],
    [-480,962,490,325.9619],
    [-631, 218, 278]
]

actual = [
    [332.509, -352.862, 665.053],
    [491.596, -345.586, 459.3611],
    [594.3319, -229.052, 239.494]
]

"""Standard Relative Error"""
standard_rel_err = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(len(predict)):
    predict[i][0]*=(-1)
    predict[i][1]*=(-1)

    for j in range(len(predict[0])):
        err = (predict[i][j] - actual[i][j])
        err = abs(err/actual[i][j])
        standard_rel_err[i][j] = err*100
print(standard_rel_err)

avg_standard_err = 0
cnt =0
for i in range(len(standard_rel_err)):
    for j in range(len(standard_rel_err)):
        avg_standard_err+=standard_rel_err[i][j]
        cnt += 1

avg_standard_err/=cnt

print(avg_standard_err)

# Trial 1 : error = 27.64146641886702 (porcentaje)