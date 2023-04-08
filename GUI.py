from tkinter import *
import Metodos


Janela = Tk()

index = IntVar()
frameSL_primaria = Frame(master=Janela)
frameSL_secundaria = Frame(master=Janela)
frameITP = Frame(master=Janela)
frameInp = Frame(master=Janela)
opc = []
opc2 = []

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
    else:
        Info.config(text = "Separe as coordenadas por vírgula, colocando cada par em uma linha diferente")
        LabelInput1.config(text = "Coordendas x,y")
        LabelInput2.config(text = "valor de x que se deseja obter o y")
        if  i == 4:
            frameSL_secundaria.pack()
            print('ok')
        else:
            pass
    frameSL_primaria.pack_forget()
    frameITP.pack_forget()

    
    frameInp.pack()

def Tela1():
    frameSL_secundaria.pack_forget()
    frameInp.pack_forget()
    frameSL_primaria.pack()
    frameITP.pack()
    





for i, nome in enumerate(Metodos.nomesSL):
    opc.append(Radiobutton(frameSL_primaria,
                variable=index,
                value = i,
                text = nome,
                command = Tela2))
    opc[i].pack()
    opc2.append(Radiobutton(frameSL_secundaria,
                variable=index,
                value = i,
                text = nome))
    opc2[i].pack()


for i, nome in enumerate(Metodos.nomesItp):
    opc.append(Radiobutton(frameITP,
                variable=index,
                value = i+4,
                text = nome,
                command = Tela2))
    opc[i+4].pack()

Janela.geometry("500x500")
Janela.title('Calculadora de Sistemas de Equações Lineares e Interpolação')

Info = Label(frameInp)
Info.pack()

LabelInput1 = Label(frameInp)
LabelInput1.pack()
InputA = Text(frameInp,height= '6', font=('Arial', 15))
InputA.pack()
LabelInput2  = Label(frameInp)
LabelInput2.pack()
InputB = Text(frameInp,height='6',font=('Arial', 15))
InputB.pack()

env = Button(frameInp, text='Enviar Dados')


pLabel = Label(frameInp,
                text ='Precisão')

pEntry = Entry(
    frameInp,
    font=("Arial", 15)
)

ret = Button(frameInp,text='retornar')



Tela1()

Janela.mainloop()
