from tkinter import *
import Metodos

opc = []

Janela = Tk()

def mostrarMetodos():
    mA.config(state='disabled')
    mB.config(state='disabled')
    Info.pack_forget()

    for i in range(len(Metodos.nomes)):
        opc.append(Radiobutton(  Janela,
                            text=Metodos.nomes[i],
                            command=Metodos.metodos[i],
                            indicatoron=0,
                            bg="gray"))
        opc[i].pack()
    pLabel.pack()
    pEntry.pack()
    ret.pack()

def retornar():
    for i in range(len(Metodos.nomes)):
        opc[i].pack_forget()
    ret.pack_forget()
    pEntry.pack_forget()
    pLabel.pack_forget()
    mAl.pack()
    mA.config(state='normal')
    mBl.pack()
    mB.config(state='normal')
    env.pack_forget()
    env.pack()
    


Janela.geometry("500x500")
Janela.title('Calculadora de Sistemas de EQuações Lineares')

Info = Label(text="Separe as colunas por vírgula!", bg = 'green')
Info.pack()

mAl = Label(Janela, text='Matriz dos coeficientes A')
mAl.pack()
mA = Text(height='8', font=('Arial', 15))
mA.pack()

mBl = Label(Janela, text='Matriz B dos resultados')
mBl.pack()
mB = Text(height='4', font=('Arial', 15))
mB.pack()

env = Button(text='Enviar Dados', command=mostrarMetodos)
env.pack()

pLabel = Label( Janela,
                text ='precisão (Necessária somente em)')

pEntry = Entry(
    Janela,
    font=("Arial", 15)
)

ret = Button(text='retornar', command=retornar)




Janela.mainloop()