def atribuiCoordenadas(coor):
    global pts_x, pts_y
    pts_x = []
    pts_y = []
    for par in pares:
        pts_x.append(par.split(',')[0])
        pts_y.append(par.split(',')[1])

    pts_x = np.array(pts_x, dtype=float)
    pts_y = np.array(pts_y, dtype=float)
    #Interpol(pts_x,pts_y)
    InterpLg(pts_x,pts_y,5)
    InterpNt(pts_x,pts_y,5)
    pass

def Interpol():
    d = len(pts_x)
    mA = []
    for i in range(d):
        linha = []
        for j in range(d):
            calc = pts_x[i] ** j
            linha.append(calc)
        mA.append(linha)
    mB = pts_y
    print(mA)
    print(mB)

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
    z = 'O polinômio é: \nP(x) = ' + str(pxn) + '\nP(' +str(pt) + ') = ' + str(r)
    return z
    