#import numpy as np

A = [[10,2,1],[1,5,1],[2,3,10]]
B = [7,-8,6]
print(A[0] - A[1])
print(A)
print(B)

def Substituição():
    pass

def Gauss_Jacobi():
    x = [[0,0,0]]
    iter = 0
    while iter < 100:
        xk = []
        for i in range(len(B)):
            soma = 0
            for j in range(len(B)):
                soma += A[i][j]*x[0][j]
            xk.append(B[i] - soma)
            pass
        x[1]= xk
    #verificação de convergencia
        

