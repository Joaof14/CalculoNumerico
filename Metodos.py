from auxiliar import retrosub
import numpy as np

A = np.array([[3,2,4],[1,1,2],[4,3,-2]],dtype=float)
#A = [[3,5,9,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]]
B = np.array([1,2,3], dtype= float)
#B = [7,1,6,8]
m = []
metodos = ("Eliminação de Gauss", "Fatoração LU")
def pivoteamento(i):
    for j in range(i+1,len(A)):
        A[[i,j]] = A[[j,i]]
        if A[i][i] != 0:
            break

def escalonamento(i,pivo,atb):
    for j in range(i + 1,len(A)):
        #define multiplicador da linha
        m.append(A[j][i] / pivo)
        #atualiza elementos da linha j com operações elementares entre 
        #ela, multiplicador e elementos da linha anteriormente definidos
        A[j] =  np.round(A[j] - m[-1]*A[i], 3)
        if atb == True:
            #atualiza vetor b para manter equivalência do sistema linear
            B[j] = np.round(B[j] - m[-1]*B[i], 3)


def outputTeste(mb):
    global A
    for i in range(len(A)):
        output = ''
        for j in range(len(A[i])):
            output += str(A[i][j]) + ' '
        if mb:
            output += '|' + str(B[i])
        print(output)

def EliminGauss():
    global A
    global B
    print("Método de Eliminação de Gauss")
    for i in range(len(A)):
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]
        escalonamento(i,pivo,True)
    print("Matriz A")   
    outputTeste(mb = True)
    retrosub(A,B, True)

#metodo de fatoração LU
def FatorLu():
    global A
    global B
    print("Método do fator LU")
    for i in range(len(A)):
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]
        escalonamento(i,pivo,False)
    L = np.zeros(np.shape(A))
    u = A
    k = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                L[i][j]=(1.000)
            elif i < j:
                L[i][j]=(0.000)
            else:
                L[i][j]=(np.round(m[k], 3))
                k+=1
    print("Matriz U:")
    outputTeste(mb = False)
    #output de teste
    print("Matriz L:")
    for i in range(len(L)):
        output = ''
        for j in range(len(L[i])):
            output += str(L[i][j]) + ' '
        print(output)
    #retrosubstuição ao contrário
    y = retrosub(L,B,False)
    #retrosubstuição normal
    retrosub(u,y,True)



FatorLu()

#EliminGauss()