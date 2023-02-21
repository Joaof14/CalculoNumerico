from tkinter import *
from sympy import expand, Symbol, Subs

class Metodos():
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    f = None
    a = None
    b = None
    p = None
    def Bis():
        print("método da bissecção")
        print(Metodos.f)
    def FalsaPos():
        print("método da falsa posição")
        print(Metodos.b)
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
xS = Symbol('x')
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
    Metodos.f = fEntry.get()
    Metodos.a = aEntry.get()
    Metodos.b = bEntry.get()
    Metodos.p = pEntry.get()
    #checa o método a ser utilzado
    if metodo.get() == Metodos.nomes[0]:
        Metodos.Bis()
    elif metodo.get() == Metodos.nomes[1]:
        Metodos.FalsaPos()
    elif metodo.get() == Metodos.nomes[2]:
        Metodos.PontoFixo()
    elif metodo.get() == Metodos.nomes[3]:
        Metodos.Secante()
    elif metodo.get() == Metodos.nomes[4]:
        Metodos.Newton()
    else:
        print("método não selecionado")
for i in range(len(Metodos.nomes)):
    opc = Radiobutton(  window,
                        text=Metodos.nomes[i],
                        variable=metodo,
                        value=Metodos.nomes[i],
                        command=chamaMetodo,
                        indicatoron=0,
                        bg="gray")
    opc.pack()
window.mainloop()
