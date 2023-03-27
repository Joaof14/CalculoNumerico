import numpy as np

A = np.array([[10,2,1],[1,5,1],[2,3,10]])
B = np.array([7,-8,6])
vetor = A[0] - A[1]
print(A)
print(B)
x = np.zeros((2,B.size))
print(x)
def Substituição():
    pass

def Gauss_Jacobi():
    
    rep = 0
    p = 0.05
    #aplicar substuição
    while rep < 100:
        global x
        for i in range(B.size):
            soma = 0
            for j in range(B.size):
                soma  += A[i][j]*x[0][j]
            x[1][i] = ((B[i] - soma)/A[i][i]) + x[0][i]
        #verificar convergencia
        print(x)
        vetor = x[1]-x[0]
        dr = np.max(np.abs(vetor))/(np.max(np.abs(x[1])))
        print(dr)
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1

def Gauss_Seidel():
    rep = 0
    p = 0.05
    #aplicar substuição
    while rep < 100:
        global x
        for i in range(B.size):
            soma = 0
            for j in range(B.size):
                if j < i and rep > 0:
                    soma  += A[i][j]*x[1][j]
                else:
                    soma  += A[i][j]*x[0][j]
            x[1][i] = ((B[i] - soma)/A[i][i]) + x[0][i]
        #verificar convergencia
        print(x)
        vetor = x[1]-x[0]
        dr = np.max(np.abs(vetor))/(np.max(np.abs(x[1])))
        print(dr)
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1
        
        
            



#Gauss_Jacobi()
Gauss_Seidel()