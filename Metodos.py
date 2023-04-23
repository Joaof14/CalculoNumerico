import numpy as np
#A = np.array([[3,2,4],[1,1,2],[4,3,-2]],dtype=float)
#A = np.array([[3,5,9,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]], dtype = float)
#B = np.array([1,2,3], dtype= float)
#B = np.array([7,1,6,8], dtype = float)
from sympy import  expand, Symbol
from sympy.plotting import plot
xS = Symbol('x')

#A = np.array([[10,2,1],[1,5,1],[2,3,10]], dtype = float)
#B = np.array([7,-8,6], dtype=float)

np.seterr(all = 'warn')


nomesSL = ("Eliminação de Gauss", "Fatoração LU", "Gauss-Jacobi", "Gauss-Seidel")
nomesItp = ("Interpolação por Sistema linear", "Interpolação de Lagrange", "Interpolação de Newton")

def atribuiMatriz(Inpa,Inpb, pr = '0.0000000001'):
    global A,B, output, m,p
    A = []
    B = []
    m = []
    output = ''
    if type(Inpa) == str:
        a = Inpa.strip().split('\n')
        b = Inpb.strip().split('\n')
        for i in range(len(b)):
            A.append(a[i].split(','))
            B.append(b[i])
        A = np.array(A, dtype=float)
        B = np.array(B, dtype=float)
    elif type(Inpa) == list:
        A = np.array(Inpa)
        B = np.array(Inpb)
    else:
        A = np.zeros((3,3))
        B = np.zeros(3)
    da = np.shape(A)
    db = np.shape(B)
    if da[0] != db:
        IndexError
    f = open("Resol.txt", 'w')
    f.write("Matriz A|B: \n")
    p = float(pr)
    f.close()
    outputMatrizesAB(mb = True)



def pivoteamento(i):
    global output
    j = np.argmax(np.abs(A[:,i]))
    A[[i,j]] = A[[j,i]]

def escalonamento(i,pivo,atb = True):
    global output

    for j in range(i + 1,len(A)):
        #define multiplicador da linha
        m.append(A[j][i] / pivo)

        #atualiza elementos da linha j com operações elementares entre 
        #ela, multiplicador e elementos da linha anteriormente definidos
        A[j] =  A[j] - m[-1]*A[i]

        if atb == True:
            #atualiza vetor b para manter equivalência do sistema linear
            B[j] = B[j] - m[-1]*B[i]

        #outputs
        output += '\nfator m: ' + str(float(m[-1])) + '\n'
        output += 'Linha ' + str(j+1) + ' = ' + 'Linha ' + str(j+1) + ' - ' + str(float(m[-1])) + '*' + 'Linha ' + str(i+1) + '\n'
    output += '\n'

def retrosub(C,D, ts):
    global output
    n = len(C)
    C = np.array(C, dtype=float)
    D = np.array(D, dtype=float)
    y = np.zeros(n)
    if ts == True:
        for i in range(n-1, -1, -1):
            soma = 0
            for j in range(i+1, n):
                soma += C[i][j]* y[j]
            y[i] = (D[i] - soma) / C[i][i]   # Fórmula da matriz;
        output = '\nSolução do sistema:\n'
        for i, s in enumerate(y):
            output += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    else:
        for i in range(n):
            soma = 0
            for j in range(i-1,-1,-1):
                soma += C[i][j]* y[j]
            y[i] = (D[i] - soma) / C[i][i]
        output = '\nValores da matriz y:\n'
        for i, s in enumerate(y):
            output += 'y.' + str(i+1) + ' = ' + str(s) + '\n'
    outputtxt()
    return y   


def outputMatrizesAB(mb):
    global A
    for i in range(len(A)):
        outputM = ''
        for j in range(len(A[i])):
            outputM += str(np.round(A[i][j], 4)) + ' '
        if mb:
            outputM += '|' + str(np.round(B[i],4))
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
    output += '\n\nMétodo de Eliminação de Gauss\n\n'
    outputtxt()
    for i in range(len(A)-1):
        output = ''
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if abs(pivo) <= 0.0000000000000001:
            pivoteamento(i)
            pivo = A[i][i]

        output += '\nEscalonamento na Matriz Ampliada AB\n'
        output += 'pivo: ' + str(pivo) 

        escalonamento(i,pivo,True)
        outputtxt()
        outputMatrizesAB(mb = True)
 
    z = retrosub(A,B, True)  
    return z

#metodo de fatoração LU
def FatorLu():
    global A
    global B
    global output
    output += '\n\nMétodo de Fatoração LU\n\n'
    outputtxt()
    for i in range(len(A)-1):
        output = ''
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]

        output += '\nEscalonamento na Matriz A\n'
        output += 'pivo: ' + str(pivo)
        
        escalonamento(i,pivo,False)
        outputtxt()
        outputMatrizesAB(mb = False)

    L = np.zeros(np.shape(A))
    u = np.copy(A)
    k = 0
    for i in range(len(A)):
        for j in range(len(A)):
            if i == j:
                L[i][j]=(1.000)
            elif i < j:
                L[i][j]=(0.000)
            else:
                L[i][j]=m[k]
                k+=1
    
    #output de teste
    output = "\nMatriz L:\n"
    for i in range(len(L)):
        for j in range(len(L[i])):
            output += str(np.round(L[i][j],4)) + ' '
        output += '\n'
    output += "\nMatriz U:\n"
    outputtxt()
    outputMatrizesAB(mb = False)


    #retrosubstuição ao contrário
    y = retrosub(L,B,False)
    z = retrosub(u,y,True)
    
    #retrosubstuição normal
    return z


def Gauss_Jacobi():
    global output
    xk = np.zeros((2,B.size))
    rep = 0
    output += '\n\nMétodo de Gauss-Jacobi\n\n'
    repmax = 100
    #Verifica critério das linhas e das colunas
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

    if clmax > 1 and ccmax > 1:
        output += '\n Sistema não oedece aos critérios de convergência suficientes\nlogo a convergência não é uma certeza \n'
        repmax = 40

    #aplicar substuição
    while rep < repmax:
        output+='\niteração: ' + str(rep) +'\n'
        for i in range(B.size):
            soma = 0
            
            if A[i][i] == 0:
                ZeroDivisionError
                output += '\n\n ERRO DE DIVISÃO POR ZERO, PROGRAMA INTERROMPIDO \n\n'
                break    
            for j in range(B.size):
                if i != j:
                    soma  += A[i][j]*xk[0][j]
                    
            
            xk[1][i] = ((B[i] - soma)/A[i][i])
            if rep >0:
                output += 'x(k-1).' + str(i+1) + ' = ' + str(xk[0][i]) 
                output+= '  x(k).' + str(i+1) + ' = ' + str(xk[1][i])+'\n'

        #verificar parada
        
        if rep > 0:

            vetor = xk[1]-xk[0]
            dr = np.max(np.abs(vetor))/(np.max(np.abs(xk[1])))
            output += 'dr = ' + str(dr) + '  precisão: ' + str(p) + '\n\n'

            if dr < p:
                break
            else:
                xk = np.flip(xk,axis = 0)
        rep += 1
    if rep == repmax and dr>p:
        output += '\nMétodo não convergiu\n'
        z = 'Método não convergiu'
    else:
        z = xk[1]
        output += '\nSolução do sistema: \n'
        for i, s in enumerate(z):
            output += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    outputtxt()
    return z



def Gauss_Seidel():
    global output
    rep = 0
    xk = np.zeros((2,B.size))
    output += '\n\nMétodo de Gauss-Seidel\n\n'
    repmax = 100
    #verifica criterio das linha e de Sassenfeld
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
    numsassenfeld = np.max(sassenfeld)

    if numsassenfeld > 1 and ccmax > 1:
        repmax=40
        output += '\nSistema não obedece aos critérios de convergência suficientes \nlogo a convergência não é uma certeza \n'
        

    #aplicar substuição
    while rep < repmax:
        output+='\niteração: ' + str(rep) +'\n'
        for i in range(B.size):
            soma = 0
            if A[i][i] == 0:
                ZeroDivisionError
                output += '\n\n ERRO DE DIVISÃO POR ZERO, PROGRAMA INTERROMPIDO \n\n'
                break
            for j in range(B.size):
                if j < i and rep > 0:
                    soma  += A[i][j]*xk[1][j]
                elif j > i and rep > 0:
                    soma  += A[i][j]*xk[0][j]
            xk[1][i] = ((B[i] - soma)/A[i][i])
            if rep > 0:
                output += 'x(k-1).' + str(i+1) + ' = ' + str(xk[0][i]) 
                output+= '  x(k).' + str(i+1) + ' = ' + str(xk[1][i])+'\n'

        #verificar parada
        if rep > 0:
            vetor = xk[1]-xk[0]
            dr = np.max(np.abs(vetor))/(np.max(np.abs(xk[1])))
            output += 'dr = ' + str(dr) + '  precisão: ' + str(p) + '\n\n'
            if dr < p:
                break
            else:
                xk = np.flip(xk,axis = 0)
        rep += 1
    if rep == repmax and dr>p:
        output += '\nMétodo não convergiu\n'
        z = 'Método não convergiu'
    else:
        z = xk[1]
        output += '\nSolução do sistema: \n'
        for i, s in enumerate(z):
            output += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    outputtxt()
    return z





def atribuiCordenadas(inpA, ponto):
    global pts_x, pts_y, pt
    pares = inpA.strip().split('\n')
    pt = float(ponto)
    pts_x = []
    pts_y = []
    for par in pares:
        if len(par.split(',')) != 2:
            IndexError
            pts_x = []
            pts_y = []
            break
        pts_x.append(par.split(',')[0])
        pts_y.append(par.split(',')[1])
    pts_x = np.array(pts_x, dtype=float)
    pts_y = np.array(pts_y, dtype=float)
    

def Interpol():
    d = len(pts_x)
    mA = []
    pxn = 0 
    r = 0
    for i in range(d):
        linha = []
        for j in range(d):
            calc = pts_x[i] ** j
            linha.append(calc)
        mA.append(linha)
    mB = pts_y
    atribuiMatriz(mA, mB)
    vetor = metodos[0]()
    for i in range(len(vetor)):
        pxn += vetor[i]*xS**i
        r += vetor[i]*pt**i
    pxn = str(pxn)
    pxn = expand(pxn)
    z = 'O polinômio é: \nP(x) = ' + str(pxn) + '\nP(' +str(pt) + ') = ' + str(r)
    plot(pxn, (xS, np.min(pts_x), np.max(pts_x)), title = str(pxn))
    return z


def InterpLg():
    d = len(pts_x)
    pxn = 0
    r = 0
    for j in range(d):
        lxk = 1
        rk = 1
        for k in range(d):
            if k != j:
                rk *= (pt - pts_x[k])/(pts_x[j] - pts_x[k])
                lxk *= (xS - pts_x[k])/(pts_x[j] - pts_x[k])
        r += rk*pts_y[j]
        pxn += lxk*pts_y[j]
    pxn = str(pxn)
    pxn = expand(pxn)
    plot(pxn, (xS, np.min(pts_x), np.max(pts_x)), title = str(pxn))
    z = 'O polinômio é: \nP(x) = ' + str(pxn) + '\nP(' +str(pt) + ') = ' + str(r)
    return z


def InterpNt():
    d1 = len(pts_x)
    o = np.zeros((d1,d1))
    o[0] += pts_y
    for i in range(1,d1):
        for j in range(d1-i):
            o[i][j] = (o[i-1][j+1] - o[i-1][j])/(pts_x[j+i] - pts_x[j])
    d = o[:,0]
    pxn = d[0]
    r = d[0]
    for i in range(1,d1):
        aux = 1
        rax = 1
        for j in range(i):
            aux*=(xS-pts_x[j])
            rax*=(pt-pts_x[j])
        pxn += d[i]*aux
        r += d[i]*rax
    pxn = str(pxn)
    pxn = expand(pxn)
    plot(pxn, (xS, np.min(pts_x), np.max(pts_x)), title = str(pxn))
    
    z = 'O polinômio é: \nP(x) = ' + str(pxn) + '\nP(' +str(pt) + ') = ' + str(r)
    return z
    

metodos = (EliminGauss, FatorLu, Gauss_Jacobi, Gauss_Seidel,Interpol,InterpLg,InterpNt)