from tkinter import *
import Metodos




def Controle():
    pass

Janela = Tk()

Janela.geometry("500x500")
Janela.title('Calculadora de Sistemas de EQuações Lineares')

Info = Label(text="Separe as colunas por vírgula!", bg = 'green')
Info.pack()

mAl = Label(Janela, text='Matriz dos coeficientes A')
mAl.pack()
mA = Text(height='20')
mA.pack()

mBl = Label(Janela, text='Matriz B dos resultados')
mBl.pack()
mB = Text(height='8')
mB.pack()

env = Button(text='Enviar Dados')

for i in range(len(Metodos.nomes)):
    opc = Radiobutton(  Janela,
                        text=Metodos.nomes[i],
                        command=Metodos.metodos[i],
                        indicatoron=0,
                        bg="gray")
    #opc.pack()

Janela.mainloop()