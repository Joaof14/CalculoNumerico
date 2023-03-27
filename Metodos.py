from auxiliar import retrosub
import numpy as np

#A = np.array([[3,2,4],[1,1,2],[4,3,-2]],dtype=float)
A = np.array([[3,5,9,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]])
#B = np.array([1,2,3], dtype= float)
B = np.array([7,1,6,8])

#A = np.array([[10,2,1],[1,5,1],[2,3,10]])
#B = np.array([7,-8,6])

        
m = []
nomes = ("Eliminação de Gauss", "Fatoração LU", "Gauss-Jacobi", "Gauss-Seidel")
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

def Gauss_Jacobi():
    x = np.zeros((2,B.size))
    rep = 0
    p = 0.05
    #aplicar substuição
    while rep < 100:

        for i in range(B.size):
            soma = 0
            for j in range(B.size):
                soma  += A[i][j]*x[0][j]
            x[1][i] = ((B[i] - soma)/A[i][i]) + x[0][i]
        #verificar convergencia
        
        vetor = x[1]-x[0]
        dr = np.max(np.abs(vetor))/(np.max(np.abs(x[1])))
        print(dr)
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1
    for i, s in enumerate(x[1]):
        print(f"x.{i+1} = {s}") 
def Gauss_Seidel():
    rep = 0
    p = 0.05
    x = np.zeros((2,B.size))
    #aplicar substuição
    while rep < 100:
        for i in range(B.size):
            soma = 0
            for j in range(B.size):
                if j < i and rep > 0:
                    soma  += A[i][j]*x[1][j]
                else:
                    soma  += A[i][j]*x[0][j]
            x[1][i] = ((B[i] - soma)/A[i][i]) + x[0][i]
        #verificar convergencia
        
        vetor = x[1]-x[0]
        dr = np.max(np.abs(vetor))/(np.max(np.abs(x[1])))
        print(dr)
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1
    for i, s in enumerate(x[1]):
        print(f"x.{i+1} = {s}") 
metodos = (EliminGauss, FatorLu, Gauss_Jacobi, Gauss_Seidel)
func = int(input("método que você quer \n"))
metodos[func]()
#FatorLu()
#EliminGauss()
#Gauss_Jacobi()
#Gauss_Seidel()