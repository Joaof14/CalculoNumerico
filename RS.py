#A = [[3,2,4],[0,2,2],[0,0,-2]]
#A = [[3,5,9,4],[0,0,1,5],[0,3,2,3],[0,9,7,4]]
#B = [1,2,3]
#B = [7,1,6,8]
A = [[-2,0,0],[2,2,0],[4,2,3]]
B = [3,2,1]


# Método da retrosubstituição:
def retrosub():
    global A
    global B
    n = len(A)
    y = n*[0]
    
    for i in range(n-1, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma += A[i][j]* y[j]
        y[i] = (B[i] - soma) / A[i][i]   # Fórmula da matriz;

    return y

def retrosubI():
    global A
    global B
    n = len(A)
    y = n*[0]
    
    for i in range(n):
        soma = 0
        for j in range(i-1,0,-1):
            soma += A[i][j]* y[j]
        y[i] = (B[i] - soma) / A[i][i]   # Fórmula da matriz;

    return y
# Resolução do sistema da matriz:
matriz_solucao = retrosubI()

# Apresentação da solução:
print("Solução do sistema da matriz:")
for i, y in enumerate(matriz_solucao):
    print(f"x.{i+1} = {y}")
