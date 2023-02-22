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
    def Bis(self):
        print('')
        while True:
            x = (self.a + self.b)/2
            fx = self.f.subs(xS, x)
            print("a: ",self.a,"b: ",self.b,"x: ", x)
            if self.fa*self.fb < 0:
                if abs(fx) < self.p:
                    print("a raíz da função é: ", x)
                    break
                else:
                    if abs(self.fa)>abs(self.fb):
                        self.a = x
                    else:
                        self.b = x
                    print("")
            elif self.fa*self.fb == 0:
                if self.fa == 0:
                    print("a raíz da função é: ", self.a)
                else:
                    print("a raíz da função é: ", self.b)
                break
            else:
                print("sem raízes no intervalo")
                break
    def FalsaPos():
        print("método da falsa posição")
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
    CalcZeroF.a = int(aEntry.get())
    CalcZeroF.b = int(bEntry.get())
    CalcZeroF.p = float(pEntry.get())
    CalcZeroF.fa = CalcZeroF.f.subs(xS, CalcZeroF.a)
    CalcZeroF.fb = CalcZeroF.f.subs(xS, CalcZeroF.b)
    #checa o método a ser utilzado
    if metodo.get() == CalcZeroF.nomes[0]:
        CalcZeroF.Bis(self=CalcZeroF)
    elif metodo.get() == CalcZeroF.nomes[1]:
        CalcZeroF.FalsaPos()
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
