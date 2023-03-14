# Método da retrosubstituição:
def retrosub(matriz_equacao):

    n = len(matriz_equacao)
    y = n*[0]
    
    for i in range(n-1, -1, -1):
        soma = 0

        for j in range(i+1, n):
            soma += matriz_equacao[i][j]* y[j]
        y[i] = (matriz_equacao[i][n-1] - soma) / matriz_equacao[i][i]   # Fórmula da matriz;

    return y

matriz = [
    [-1, 1, 8, 1],
    [-2, 5, 2, -3],
    [3, -2, -1, 1],
    [1, 1, 1, 4]]
type(matriz)

# Resolução do sistema da matriz:
matriz_solucao = retrosub(matriz)

# Apresentação da solução:
print("Solução do sistema da matriz:")
for i, y in enumerate(matriz_solucao):
    print(f"x.{i+1} = {y}")
