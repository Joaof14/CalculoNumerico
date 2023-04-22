import numpy as np

A = np.array([[10,2,1],[1,5,1],[2,3,10]])
B = np.array([7,-8,6])

A = [[0, -0.2,-0.2],[-0.75, 0, -0.25],[-0.5, -0.5, 0]]
A = np.array([[2,-0.2,-0.1],[-0.2,-1,-0.2],[-0.2,-0.3,3]], dtype=float)

cl = np.zeros(B.size, dtype=float)

for i in range (B.size):
    cl[i] = np.sum(np.abs(A[i]))
print(cl)
clmax = np.max(cl)

cc = np.zeros(B.size, dtype=float)

for i in range (B.size):
    cc[i] = np.sum(np.abs(A[:,i]))
print(cc)
ccmax = np.max(cc)

sassenfeld = np.ones(shape=B.size, dtype=float)
for i in range(B.size):
    aux = 0
    for j in range(B.size):
        aux += np.abs(A[i][j])*sassenfeld[j]
    sassenfeld[i] = aux


print(clmax)
print(ccmax)
numsassenfeld = np.max(sassenfeld)
print(numsassenfeld)









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
        


