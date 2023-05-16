import numpy as np

def atribuiMatriz(Inpa,Inpb):
    global A,B, output, m, Acopia, Bcopia
    m = []
    output = ''
    A = np.array(Inpa)
    B = np.array(Inpb)
    f = open("Resolução_Sistema_Linear.txt", 'w')
    f.write("Matriz A|B: \n")
    f.close()
    outputMatrizesAB(mb = True)
    Acopia = np.copy(A)
    Bcopia = np.copy(B)



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
        with open('Resolução_Sistema_Linear.txt', 'a') as f:
            f.write(outputM)

def outputtxt():
    global output
    with open('Resolução_Sistema_Linear.txt', 'a') as f:
        f.write(output)
    output = ''

def verifica(solu):
    #verifica resíduos
    global output
    solu = np.array(solu, dtype = float)
    residuos = np.zeros(len(A))
    output += '\nResíduo=B-B~\n'
    for i in range(len(A)):
        somatorio = 0
        for j in range(len(A)):
            somatorio += solu[j]*Acopia[i][j]
        residuos[i] = Bcopia[i] - somatorio
        output += '\nResíduo.'+ str(i+1) +'=' + str(residuos[i])
    outputtxt()

def EliminGauss():
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
        #escalona a matriz
        escalonamento(i,pivo,True)
        outputtxt()
        outputMatrizesAB(mb = True)
    z = retrosub(A,B, True)
    verifica(z)
    return z