#A = [[3,2,4],[1,1,2],[4,3,-2]]
A = [[3,5,9,4],[0,0,1,5],[0,3,0,3],[0,9,7,4]]
#B = [1,2,3]
B = [7,1,6,8]
m = []
def pivoteamento(i):
    for j in range(i,len(A)-1):
        if abs(A[j][i]) < abs(A[j+1][i]):
            aaux = A[j]
            A[j] = A[j+1]
            A[j+1] = aaux
            baux = B[j]
            B[j] = B[j+1]
            B[j+1] = baux
            break

def escalonamento(i,pivo,atb):
    linha = A[i]
    for j in range(i + 1,len(A)):
        #define multiplicador da linha
        m.append(A[j][i] / pivo)
        for k in range(i, len(A)):
            #atualiza elementos da linha j com operações elementares entre 
            #ela, multiplicador e elementos da linha anteriormente definidos
            A[j][k] =  round(A[j][k] - m[-1]*linha[k], 3)
        if atb == True:
            #atualiza vetor b para manter equivalência do sistema linear
            B[j] = round(B[j] - m[-1]*B[i], 3)

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
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]
        escalonamento(i,pivo,True)
        
    outputTeste()

def FatorLu():
    global A
    global B
    for i in range(len(A)):
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]
        escalonamento(i,pivo,False)
    



EliminGauss()



