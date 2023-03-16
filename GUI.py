from tkinter import *
import Metodos

def Controle():
    if metodo.get() == Metodos.nomes[0]:
        Metodos.EliminGauss()
    elif metodo.get() == Metodos.nomes[1]:
        Metodos.FatorLu()
    else:
        pass

Janela = Tk()

Janela.geometry("360x360")

metodo = StringVar()
for i in range(len(Metodos.nomes)):
    opc = Radiobutton(  Janela,
                        text=Metodos.nomes[i],
                        variable=metodo,
                        value=Metodos.nomes[i],
                        command=Controle,
                        indicatoron=0,
                        bg="gray")
    opc.pack()

Janela.mainloop()