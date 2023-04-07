from tkinter import *
import Metodos


Janela = Tk()

index = IntVar()
frame1 = Frame(master=Janela)
frame2 = Frame(master=Janela)
opc = []

resultado = ''

def displayResult():
    global resultado
    x = Metodos.metodos[index.get()]()
    res = 'Método de: ' + Metodos.nomes[index.get()]
    res += '\nSolução do sistema:\n'
    for i, s in enumerate(x):
        print(f"x.{i+1} = {s}") 
        res += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    resultado = Label(text=res)
    resultado.pack()


def Tela2():
    i = index.get()
    if i in range(0,4):
        Info.config(text = "Separe as colunas por vírgula")
        LabelInput1.config(text = "Matriz A")
        LabelInput2.config(text = "Matriz B")
        if i in range(2,4):
            pLabel.pack()
            pEntry.pack()
    elif  i == 4:
        print('ok')
    else:
        pass
    frame1.pack_forget()
    frame2.pack()

def Tela1():
    frame1.pack()
    





for i, nome in enumerate(Metodos.nomes):
    opc.append(Radiobutton(frame1,
                variable=index,
                value = i,
                text = nome,
                command = Tela2))
    opc[i].pack()

Janela.geometry("500x500")
Janela.title('Calculadora de Sistemas de Equações Lineares e Interpolação')

Info = Label(frame2)
Info.pack()

LabelInput1 = Label(frame2)
LabelInput1.pack()
InputA = Text(frame2,height= '6', font=('Arial', 15))
InputA.pack()
LabelInput2  = Label(frame2)
LabelInput2.pack()
InputB = Text(frame2,height='6',font=('Arial', 15))
InputB.pack()

env = Button(frame2, text='Enviar Dados')


pLabel = Label(frame2,
                text ='Precisão')

pEntry = Entry(
    frame2,
    font=("Arial", 15)
)

ret = Button(frame2,text='retornar')



Tela1()

Janela.mainloop()
