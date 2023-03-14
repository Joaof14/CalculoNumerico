def retrosub(C,D, ts):
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