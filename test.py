a = [1,2,3]
b = [4,5,6]
c = [a,b]

d = []
for i in range(len(c)):
    dlinha = []
    for j in range(len(c[0])):
        if i == j:
            dlinha.append(1)
        else:
            dlinha.append(0)
    d.append(dlinha)

print(c)
print(d)