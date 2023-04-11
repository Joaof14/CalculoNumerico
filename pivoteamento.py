import numpy as np

A = np.array([[1,2,3],[3,4,5],[7,-8,9]])
i = 1
print(A[:,i])
j = np.argmax(np.abs(A[:,i]))
print(j)
A[[i,j]] = A[[j,i]]
print(A)



A = np.array([[10,2,1],[1,5,1],[2,3,10]], dtype = float)
B = np.array([7,-8,6], dtype=float)