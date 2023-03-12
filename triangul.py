A = [[3,2,4],[1,1,2],[4,3,-2]]
B = [1,2,3]

def outputTeste():
    global A
    for i in range(len(A)):
        output = ''
        for j in range(len(A[i])):
            output += str(A[i][j]) + ' '
        output += '|' + str(B[i])
        print(output)

def EliminGauss():
    global A
    for i in range(len(A)):
        pivo = A[i][i]
        linha = A[i]
        for j in range(i + 1,len(A)):
            m = A[j][i] / pivo
            for k in range(i, len(A)):
                A[j][k] =  round(A[j][k] - m*linha[k], 3)
            B[j] = round(B[j] - m*B[i], 3)
        

    outputTeste()
EliminGauss()