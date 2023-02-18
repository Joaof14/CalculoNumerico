from tkinter import *

metodos = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")

def chamarMetodo():
    if metodo.get() == metodos[0]:
        Bis()
    elif metodo.get() == metodos[1]:
        FalsaPos()
    elif metodo.get() == metodos[2]:
        PontoFixo()
    elif metodo.get() == metodos[3]:
        Secante()
    elif metodo.get() == metodos[4]:
        Newton()
    else:
        print("método não selecionado")
def Bis():
    print("método da bissecção")
def FalsaPos():
    print("método da bissecção")
def PontoFixo():
    print("método da bissecção")
def Secante():
    print("método da bissecção")
def Newton():
    print("método da bissecção")
window = Tk()

metodo = StringVar()

for i in range(len(metodos)):
    opc = Radiobutton(  window,
                        text=metodos[i],
                        variable=metodo,
                        value=metodos[i],
                        command=chamarMetodo)
    opc.pack()

window.mainloop()