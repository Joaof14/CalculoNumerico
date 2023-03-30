import numpy as np

pares= np.array(['1,2','1,2','1,2'])
x = []
y = []
for par in pares:
    x.append(par.split(',')[0])
    y.append(par.split(',')[1])

x = np.array(x, dtype=float)
y = np.array(y, dtype=float)
print(x)
print(y)

