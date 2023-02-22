from tkinter import *
from sympy import expand, Symbol, Subs
xS = Symbol('x')
class CalcZeroF():
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    f = None
    a = None
    b = None
    p = None
    fa = None
    fb = None
    cond = True
    def calc(self, x):
        fx = self.f.subs(xS, x)
        if self.fa*self.fb <= 0:
            if abs(fx) < self.p:
                print("a raíz da função é: ", x)
                self.cond = False
            elif self.fa == 0:
                print("a raíz da função é: ", self.a)
            elif self.fb == 0:
                print("a raíz da função é: ", self.b)
            else:
                if abs(self.fa)>abs(self.fb):
                    self.a = x
                else:
                    self.b = x
                    print("")     
        else:
            if self.a > self.b:
                self.a -= 1
            elif self.a<self.b:
                self.b -=1
            else:
                print("sem raízes no intervalo")
                self.cond = False
        return self.cond
    def Bis(self):
        print('')
        while self.cond:
            x = (self.a + self.b)/2
            print("a: ",self.a,"b: ",self.b,"x: ", x)
            self.calc(self,x)
        self.cond = True        
    def FalsaPos(self):
        print("método da falsa posição")
        while True:
            x = ((self.a*self.fb)-(self.b*self.a))/(self.b-self.a)
            print("a: ",self.a,"b: ",self.b,"x: ", x)
            self.calc(self,x)
        self.cond = True
    def PontoFixo():
        print("método do ponto fixo")
    def Secante():
        print("método da secante")
    def Newton():
        print("método de newton")
window = Tk()
fLabel = Label( window,
                text ='função')
fLabel.pack()
fEntry = Entry(
    window,
    font=("Arial", 15),
)
fEntry.pack()
aLabel = Label( window,
                text ='início do intervalo')
aLabel.pack()
aEntry = Entry(
    window,
    font=("Arial", 15)
)
aEntry.pack()
bLabel = Label( window,
                text ='final do intervalo')
bLabel.pack()
bEntry = Entry(
    window,
    font=("Arial", 15)
)
bEntry.pack()
pLabel = Label( window,
                text ='precisão')
pLabel.pack()
pEntry = Entry(
    window,
    font=("Arial", 15)
)
pEntry.pack()
metodo = StringVar()
def chamaMetodo():
    #atualiza atributos do metodo
    CalcZeroF.f = expand(fEntry.get())
    CalcZeroF.a = float(aEntry.get())
    CalcZeroF.b = float(bEntry.get())
    CalcZeroF.p = float(pEntry.get())
    CalcZeroF.fa = CalcZeroF.f.subs(xS, CalcZeroF.a)
    CalcZeroF.fb = CalcZeroF.f.subs(xS, CalcZeroF.b)
    #checa o método a ser utilzado
    if metodo.get() == CalcZeroF.nomes[0]:
        CalcZeroF.Bis(self=CalcZeroF)
    elif metodo.get() == CalcZeroF.nomes[1]:
        CalcZeroF.FalsaPos(self=CalcZeroF)
    elif metodo.get() == CalcZeroF.nomes[2]:
        CalcZeroF.PontoFixo()
    elif metodo.get() == CalcZeroF.nomes[3]:
        CalcZeroF.Secante()
    elif metodo.get() == CalcZeroF.nomes[4]:
        CalcZeroF.Newton()
    else:
        print("método não selecionado")
for i in range(len(CalcZeroF.nomes)):
    opc = Radiobutton(  window,
                        text=CalcZeroF.nomes[i],
                        variable=metodo,
                        value=CalcZeroF.nomes[i],
                        command=chamaMetodo,
                        indicatoron=0,
                        bg="gray")
    opc.pack()
window.mainloop()
