import numpy as np
import sympy as sp
xS = sp.Symbol('x')

pares= np.array(['-1,4','0,1','2,-1'])
x = []
y = []
for par in pares:
    x.append(par.split(',')[0])
    y.append(par.split(',')[1])

x = np.array(x, dtype=float)
y = np.array(y, dtype=float)
print(x)
print(y)

def Interpol(inpA, inpB):
    d = len(inpA)
    mA = []
    for i in range(d):
        linha = []
        for j in range(d):
            calc = inpA[i] ** j
            linha.append(calc)
        mA.append(linha)
    mB = inpB
    print(mA)
    print(mB)

#Interpol(x,y)

def InterpLg(xz,yz):
    d = len(xz)
    pxn = 0
    lx = []
    for j in range(d):
        lxk = 1
        for k in range(d):
            if k != j:
                lxk *= (xS - xz[k])/(xz[j] - xz[k])
        lx.append(lxk)
        pxn += lxk*yz[j]
    print(sp.expand(pxn))


def InterpNt(xz,yz):
    d1 = len(xz)
    o = np.zeros((d1,d1))
    o[0] += yz
    for i in range(1,d1):
        for j in range(d1-i):
            o[i][j] = (o[i-1][j+1] - o[i-1][j])/(xz[j+1] - xz[j])
    d = o[:,0]
    print(o)
#InterpLg(x,y)  
InterpNt(x,y)
