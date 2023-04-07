import numpy as np

A = np.array([[1,2,3],[3,4,5],[7,-8,9]])
i = 1
print(A[:,i])
j = np.argmax(np.abs(A[:,i]))
print(j)
A[[i,j]] = A[[j,i]]
print(A)


j = np.argmax(np.abs(A[:,i])) 
A[[i,j]] = A[[j,i]]
B[[i,j]] = B[[j,i]]
global output
j = np.argmax(np.abs(A[:,i])) 
A[[i,j]] = A[[j,i]]
if atb == True:
    B[[i,j]] = B[[j,i]]