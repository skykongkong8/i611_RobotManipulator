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

m1 = [
    ['(c_1)', '(-s_1)', '0','0'],
    ['(s_1)','(c_1)','0','0'],
    ['0','0','1', 'u'],
    ['0','0','0','1']
]

m2 = [
    ['(c_2)', '0', '(-s_2)', '(l)(c_2)'],
    ['(s_2)', '0', '(c_2)', '(l)(s_2)'],
    ['0', '-1', '0', 'v'],
    ['0', '0', '0', '1']
]

matrix_printer(matrix_prettier(matrix_with_variables_calculator(m1,m2,result_4)))