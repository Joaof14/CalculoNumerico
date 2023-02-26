if self.i >= 2:
    fx.append(self.fx)
    xk = x[self.i-1]-((self.fx* (x[self.i-1]-x[self.i-2]))/(fx[self.i-1]-fx[self.i - 2]))
    print(xk)
    x.append(xk)
elif self.i == 0: 
    x.append(self.a)
    x.append(self.b)