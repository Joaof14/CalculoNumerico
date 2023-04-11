import numpy as np

A = np.array([[1,2,3],[3,4,5],[7,-8,9]])
i = 1
print(A[:,i])
j = np.argmax(np.abs(A[:,i]))
print(j)
A[[i,j]] = A[[j,i]]
print(A)



if objtv == 1:
    outputMatrizesAB(mb = True)
    metodos = (EliminGauss, FatorLu, Gauss_Jacobi, Gauss_Seidel)
    func = int(input("método que você quer \n"))
    output = '\nMétodo de ' + nomes[func] + '\n'
    outputtxt()
    metodos[func]()
else:
    objtv = int(input("Digite 1 para input de Matriz \nDigite 2 para input de Par ordenado\n"))

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