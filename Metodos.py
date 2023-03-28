import numpy as np

#A = np.array([[3,2,4],[1,1,2],[4,3,-2]],dtype=float)
A = np.array([[3,5,9,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]])
#B = np.array([1,2,3], dtype= float)
B = np.array([7,1,6,8])

#A = np.array([[10,2,1],[1,5,1],[2,3,10]])
#B = np.array([7,-8,6])

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
        output += 'fator m: ' + str(float(m[-1])) + '\n'
        output += 'Linha ' + str(j) + ' = ' + 'Linha ' + str(j) + ' - ' + str(float(m[-1])) + '*' + 'Linha ' + str(i) + '\n'
    


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
        for i, s in enumerate(y):
            print(f"x.{i+1} = {s}") 
    else:
        n = len(C)
        y = n*[0]
        for i in range(n):
            soma = 0
            for j in range(i-1,-1,-1):
                soma += C[i][j]* y[j]
            y[i] = (D[i] - soma) / C[i][i]
        print("Solução Parcial")
        for i, s in enumerate(y):
            print(f"y.{i+1} = {s}")
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
    for i in range(len(A)):
        output = ''
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]

        output += 'Escalonamento na Matriz Ampliada AB\n'
        output += 'pivo: ' + str(pivo) + '\n'

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
    for i in range(len(A)):
        output = ''
        #define pivo e linha para utilizar com multiplicador operações
        pivo = A[i][i]
        if pivo == 0:
            pivoteamento(i)
            pivo = A[i][i]

        output += 'Escalonamento na Matriz A\n'
        output += 'pivo: ' + str(pivo) + '\n'
        
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
    output = "Matriz L:\n"
    for i in range(len(L)):
        for j in range(len(L[i])):
            output += str(L[i][j]) + ' '
        output += '\n'
    output += "Matriz U:\n"
    outputtxt()
    outputMatrizesAB(mb = False)



    #retrosubstuição ao contrário
    y = retrosub(L,B,False)
    #retrosubstuição normal
    retrosub(u,y,True)



def Gauss_Jacobi():
    global output
    x = np.zeros((2,B.size))
    rep = 0
    p = 0.05

    #aplicar substuição
    while rep < 100:
        for i in range(B.size):
            soma = 0
            for j in range(B.size):
                soma  += A[i][j]*x[0][j]
            x[1][i] = ((B[i] - soma)/A[i][i]) + x[0][i]

        #verificar convergencia 
        vetor = x[1]-x[0]
        dr = np.max(np.abs(vetor))/(np.max(np.abs(x[1])))
        print(dr)
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1
    for i, s in enumerate(x[1]):
        print(f"x.{i+1} = {s}") 




def Gauss_Seidel():
    global output
    rep = 0
    p = 0.05
    x = np.zeros((2,B.size))

    #aplicar substuição
    while rep < 100:
        for i in range(B.size):
            soma = 0
            for j in range(B.size):
                if j < i and rep > 0:
                    soma  += A[i][j]*x[1][j]
                else:
                    soma  += A[i][j]*x[0][j]
            x[1][i] = ((B[i] - soma)/A[i][i]) + x[0][i]

        #verificar convergencia
        vetor = x[1]-x[0]
        dr = np.max(np.abs(vetor))/(np.max(np.abs(x[1])))
        print(dr)
        if dr < p and rep > 0:
            break
        else:
            x = np.flip(x,axis = 0)
        rep += 1
    for i, s in enumerate(x[1]):
        print(f"x.{i+1} = {s}") 


outputMatrizesAB(mb = True)

metodos = (EliminGauss, FatorLu, Gauss_Jacobi, Gauss_Seidel)
func = int(input("método que você quer \n"))
metodos[func]()


