import numpy as np

A = np.array([[1,2,3],[3,4,5],[7,-8,9]])
i = 1
print(A[:,i])
j = np.argmax(np.abs(A[:,i]))
print(j)
A[[i,j]] = A[[j,i]]
print(A)


