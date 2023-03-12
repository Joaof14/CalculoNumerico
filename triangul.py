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
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        linha = A[i]
        if pivo == 0:
            pass
        for j in range(i + 1,len(A)):
            #define multiplicador da linha
            m = A[j][i] / pivo
            for k in range(i, len(A)):
                #atualiza elementos da linha j com operações elementares entre 
                #ela, multiplicador e elementos da linha anteriormente definidos
                A[j][k] =  round(A[j][k] - m*linha[k], 3)
            #atualiza vetor b para manter equivalência do sistema linear
            B[j] = round(B[j] - m*B[i], 3)
    outputTeste()

EliminGauss()