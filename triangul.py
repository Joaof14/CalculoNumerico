#A = [[3,2,4],[1,1,2],[4,3,-2]]
A = [[3,5,2,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]]
#B = [1,2,3]
B = [7,1,6,8]

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
    global B
    for i in range(len(A)):
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        linha = A[i]
        if pivo == 0:
            for j in range(i,len(A)-1):
                if abs(A[j][i]) < abs(A[j+1][i]):
                    aaux = A[j]
                    A[j] = A[j+1]
                    A[j+1] = aaux
                    baux = B[j]
                    B[j] = B[j+1]
                    B[j+1] = baux
                    break
            pivo = A[i][i]
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