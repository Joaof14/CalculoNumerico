import numpy as np

A = np.array([[10,2,1],[1,5,1],[2,3,10]])
B = np.array([7,-8,6])




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
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1
    print("Solução do sistema da matriz:")
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
        




#Gauss_Jacobi()
#Gauss_Seidel()
