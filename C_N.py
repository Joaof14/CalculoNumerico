from tkinter import *
from sympy import expand, Symbol, Subs
xS = Symbol('x')
class Metodos():
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    f = None
    a = None
    b = None
    p = None
    
    def Bis():
        print('')
        while True:
            cond = (Metodos.f.subs(xS,Metodos.a))*(Metodos.f.subs(xS,Metodos.b))
            print(cond)
            x = (Metodos.a+Metodos.b)/2
            print("loop; a: ",Metodos.a, "b: ",Metodos.b, "x: ",x)
            if cond <= 0: #possui raiz entre a e b
                if (abs(Metodos.f.subs(xS,Metodos.a)) <= Metodos.p):
                    print("a raíz da função é: ", Metodos.a)
                elif (abs(Metodos.f.subs(xS,Metodos.a))) <= Metodos.p:
                    print("a raíz da função é: ", Metodos.b)
                else:    
                    if abs(Metodos.a) > abs(Metodos.b):
                        Metodos.a = x
                    else:
                        Metodos.b = x
            else:
                print("não há zero na função")
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
    Metodos.f = expand(fEntry.get())
    Metodos.a = int(aEntry.get())
    Metodos.b = int(bEntry.get())
    Metodos.p = int(pEntry.get())
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
