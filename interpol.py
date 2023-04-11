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
print('pontos x: ')
print(x)
print('pontos y: ')
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

def InterpLg(xz,yz, pt):
    print("Interpolação de Lagrange")
    d = len(xz)
    pxn = 0
    r = 0
    for j in range(d):
        lxk = 1
        rk = 1
        for k in range(d):
            if k != j:
                rk *= (pt - xz[k])/(xz[j] - xz[k])
                lxk *= (xS - xz[k])/(xz[j] - xz[k])
        r += rk*yz[j]
        pxn += lxk*yz[j]
    print(sp.expand(pxn))
    print(f'P({pt}) = {r}')


def InterpNt(xz,yz, pt):
    print("Interpolação de Newton")
    d1 = len(xz)
    o = np.zeros((d1,d1))
    o[0] += yz
    for i in range(1,d1):
        for j in range(d1-i):
            o[i][j] = (o[i-1][j+1] - o[i-1][j])/(xz[j+i] - xz[j])
    d = o[:,0]
    pxn = d[0]
    r = d[0]
    for i in range(1,d1):
        aux = 1
        rax = 1
        for j in range(i):
            aux*=(xS-xz[j])
            rax*=(pt-xz[j])
        pxn += d[i]*aux
        r += d[i]*rax
    print(sp.expand(pxn))
    print(f'P({pt}) = {r}')

InterpLg(x,y,5)  
InterpNt(x,y,5)
