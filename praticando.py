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
            o[i][j] = (o[i-1][j+1] - o[i-1][j])/(xz[j+i] - xz[j])
    d = o[:,0]
    print(o)
#InterpLg(x,y)  
InterpNt(x,y)
objtv = int(input("Digite 1 para input de Matriz \nDigite 2 para input de Par ordenado\n"))
if objtv == 1:
    outputMatrizesAB(mb = True)
    metodos = (EliminGauss, FatorLu, Gauss_Jacobi, Gauss_Seidel)
    func = int(input("método que você quer \n"))
    output = '\nMétodo de ' + nomes[func] + '\n'
    outputtxt()
    metodos[func]()
else:
    pares= np.array(['-1,2','0,1','1,2','3,82', '2,17'])
    xl = []
    yl = []
    for par in pares:
        xl.append(par.split(',')[0])
        yl.append(par.split(',')[1])

    xl = np.array(xl, dtype=float)
    yl = np.array(yl, dtype=float)
    #Interpol(xl,yl)
    InterpLg(xl,yl,5)
    InterpNt(xl,yl,5)