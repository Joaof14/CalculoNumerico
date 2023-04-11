import numpy as np
from sympy import  expand, Symbol

xS = Symbol('x')

A = np.array([[3,5,9,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]], dtype = float)
B = np.array([7,1,6,8], dtype = float)



A = np.array([[3,2,4],[1,1,2],[4,3,-2]],dtype=float)
B = np.array([1,2,3], dtype= float)




A = np.array([[10,2,1],[1,5,1],[2,3,10]], dtype = float)
B = np.array([7,-8,6], dtype=float)



x = np.zeros(B.size, dtype=float)
m = []
output = ''
f = open("Resol.txt", 'w')
f.write("Matriz A|B: \n")
f.close()
nomes = ("Eliminação de Gauss", "Fatoração LU", "Gauss-Jacobi", "Gauss-Seidel")
def pivoteamento(i):
    global output
    for j in range(i+1,len(A)):
        A[[i,j]] = A[[j,i]]
        B[[i,j]] = B[[j,i]]
        if A[i][i] != 0:
            break

def escalonamento(i,pivo,atb):

    global output

    for j in range(i + 1,len(A)):
        #define multiplicador da linha
        m.append(A[j][i] / pivo)

        #atualiza elementos da linha j com operações elementares entre 
        #ela, multiplicador e elementos da linha anteriormente definidos
        A[j] =  np.round(A[j] - m[-1]*A[i], 3)

        if atb == True:
            #atualiza vetor b para manter equivalência do sistema linear
            B[j] = np.round(B[j] - m[-1]*B[i], 3)

        #outputs
        output += '\nfator m: ' + str(float(m[-1])) + '\n'
        output += 'Linha ' + str(j+1) + ' = ' + 'Linha ' + str(j+1) + ' - ' + str(float(m[-1])) + '*' + 'Linha ' + str(i+1) + '\n'
    output += '\n'

def retrosub(C,D, ts):
    global output
    n = len(C)
    y = n*[0]
    if ts == True:
        for i in range(n-1, -1, -1):
            soma = 0
            for j in range(i+1, n):
                soma += C[i][j]* y[j]
            y[i] = (D[i] - soma) / C[i][i]   # Fórmula da matriz;
        print("Solução do sistema da matriz:")
        output = '\nSolução do sistema:\n'
        for i, s in enumerate(y):
            print(f"x.{i+1} = {s}") 
            output += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    else:
        n = len(C)
        y = n*[0]
        for i in range(n):
            soma = 0
            for j in range(i-1,-1,-1):
                soma += C[i][j]* y[j]
            y[i] = (D[i] - soma) / C[i][i]
        print("Solução Parcial")
        output = '\nValores da matriz y:\n'
        for i, s in enumerate(y):
            print(f"y.{i+1} = {s}")
            output += 'y.' + str(i+1) + ' = ' + str(s) + '\n'
    outputtxt()
    return y   



def outputMatrizesAB(mb):
    global A
    for i in range(len(A)):
        outputM = ''
        for j in range(len(A[i])):
            outputM += str(A[i][j]) + ' '
        if mb:
            outputM += '|' + str(B[i])
        outputM += '\n'
        with open('Resol.txt', 'a') as f:
            f.write(outputM)

def outputtxt():
    global output
    with open('Resol.txt', 'a') as f:
        f.write(output)
    output = ''

def EliminGauss():
    global A
    global B
    global output
    print("Método de Eliminação de Gauss")
    for i in range(len(A)-1):
        output = ''
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]

        output += '\nEscalonamento na Matriz Ampliada AB\n'
        output += 'pivo: ' + str(pivo) 

        escalonamento(i,pivo,True)
        outputtxt()
        outputMatrizesAB(mb = True)

    print("Matriz A")   
    retrosub(A,B, True)

#metodo de fatoração LU
def FatorLu():
    global A
    global B
    global output
    print("Método do fator LU")
    for i in range(len(A)-1):
        output = ''
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]

        output += '\nEscalonamento na Matriz A\n'
        output += 'pivo: ' + str(pivo)
        
        escalonamento(i,pivo,False)
        outputtxt()
        outputMatrizesAB(mb = False)

    L = np.zeros(np.shape(A))
    u = A
    k = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                L[i][j]=(1.000)
            elif i < j:
                L[i][j]=(0.000)
            else:
                L[i][j]=(np.round(m[k], 3))
                k+=1
    
    #output de teste
    output = "\nMatriz L:\n"
    for i in range(len(L)):
        for j in range(len(L[i])):
            output += str(L[i][j]) + ' '
        output += '\n'
    output += "\nMatriz U:\n"
    outputtxt()
    outputMatrizesAB(mb = False)



    #retrosubstuição ao contrário
    y = retrosub(L,B,False)
    #retrosubstuição normal
    retrosub(u,y,True)


def Gauss_Jacobi():
    global output
    xk = np.zeros((2,B.size))
    rep = 0
    p = 0.05
    print('Método de Gauss-Jacobi')
    #aplicar substuição
    while rep < 100:
        for i in range(B.size):
            soma = 0
            #output = 'xk.'+ str[i] + ' = ' + str(B[i])
    
            for j in range(B.size):
                if i != j:
                    soma  += A[i][j]*xk[0][j]
                    #output += ' - ' + str(A[i][j]) + '*' + str(xk[0][j])
            xk[1][i] = ((B[i] - soma)/A[i][i])
            if rep >0:
                output += 'x(k-1).' + str(i+1) + ' = ' + str(xk[0][i]) 
                output+= '  x(k).' + str(i+1) + ' = ' + str(xk[1][i])+'\n'

        #verificar convergencia 
        
        if rep > 0:

            vetor = xk[1]-xk[0]
            dr = np.max(np.abs(vetor))/(np.max(np.abs(xk[1])))
            output += 'dr = ' + str(dr) + '  precisão: ' + str(p) + '\n\n'

            if dr < p:
                break
            else:
                xk = np.flip(xk,axis = 0)
        rep += 1
        outputtxt()
    for i, s in enumerate(xk[1]):
        print(f"x.{i+1} = {s}") 
    



def Gauss_Seidel():
    global output
    global x
    rep = 0
    p = 0.05
    xk = np.zeros((2,B.size))
    print('método de gaus-seidel')
    #aplicar substuição
    while rep < 100:
        for i in range(B.size):
            soma = 0

            for j in range(B.size):
                if j < i and rep > 0:
                    soma  += A[i][j]*xk[1][j]
                elif j > i and rep > 0:
                    soma  += A[i][j]*xk[0][j]
            xk[1][i] = ((B[i] - soma)/A[i][i])
            if rep > 0:
                output += 'x(k-1).' + str(i+1) + ' = ' + str(xk[0][i]) 
                output+= '  x(k).' + str(i+1) + ' = ' + str(xk[1][i])+'\n'

        #verificar convergencia
        if rep > 0:
            vetor = xk[1]-xk[0]
            dr = np.max(np.abs(vetor))/(np.max(np.abs(xk[1])))
            output += 'dr = ' + str(dr) + '  precisão: ' + str(p) + '\n\n'
            if dr < p:
                break
            else:
                xk = np.flip(xk,axis = 0)
        rep += 1
        outputtxt()
    for i, s in enumerate(xk[1]):
        print(f"x.{i+1} = {s}") 


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

def InterpLg(xz,yz, pt):
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
    print(pxn)
    print(r)
    

def InterpNt(xz,yz,pt):
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
    print(expand(pxn))
    print(r)

#
Gauss_Jacobi()
Gauss_Seidel()

