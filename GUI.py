from tkinter import *
import Metodos


Janela = Tk()

index = IntVar()
index_s = IntVar()
frameSL_primaria = Frame(master=Janela)
frameSL_secundaria = Frame(master=Janela)
frameITP = Frame(master=Janela)
frameTela2 = Frame(master=Janela)
opc = []
opc2 = []

resultado = Label(Janela)

def displayResult():
    global resultado
    resultado.config(text='')
    if index.get() < 4:
        if index.get() > 1:
            Metodos.atribuiMatriz(InputA.get("1.0", "end"), InputB.get("1.0", "end"), pr = pEntry.get())
        else:
            Metodos.atribuiMatriz(InputA.get("1.0", "end"), InputB.get("1.0", "end"))
        res = 'Método de: ' + Metodos.nomesItp[index.get()]
        res += '\nSolução do sistema:\n'
        x = Metodos.metodos[index.get()]()
        for i, s in enumerate(x):
            print(f"x.{i+1} = {s}") 
            res += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    else:
        res = 'Método de: ' + Metodos.nomesSL[index.get()]
        if index.get == 4:
            pass
        
    resultado.config(text=res)
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

    ret.pack()
    frameTela2.pack()

def Tela1():
    resultado.pack_forget()
    frameSL_secundaria.pack_forget()
    frameTela2.pack_forget()
    frameSL_primaria.pack()
    frameITP.pack()
    



label_sl_secundario = Label(frameSL_secundaria, text = 'escolha como realizar a resolução\n do sistema para a interpolação!\n O método de eliminação de gauss\n será considerado padrão')
label_sl_secundario.pack()

label_tela_1 = Label(frameSL_primaria, 
                     text = "escolha o que quer realizar",
                      font = ("Arial", 15))
label_tela_1.pack()


for i, nome in enumerate(Metodos.nomesSL):
    opc.append(Radiobutton(frameSL_primaria,
                variable=index,
                value = i,
                text = nome,
                command = Tela2,
                indicatoron=False))
    opc[i].pack()
    opc2.append(Radiobutton(frameSL_secundaria,
                variable=index_s,
                value = i,
                text = nome))
    opc2[i].pack()


for i, nome in enumerate(Metodos.nomesItp):
    opc.append(Radiobutton(frameITP,
                variable=index,
                value = i+4,
                text = nome,
                command = Tela2,
                indicatoron=False))
    opc[i+4].pack()




Janela.geometry("500x600")
Janela.title('Calculadora de Sistemas de Equações Lineares e Interpolação')

Info = Label(frameTela2)
Info.pack()

LabelInput1 = Label(frameTela2)
LabelInput1.pack()
InputA = Text(frameTela2,height= '6', font=('Arial', 15))
InputA.pack()
LabelInput2  = Label(frameTela2)
LabelInput2.pack()
InputB = Text(frameTela2,height='6',font=('Arial', 15))
InputB.pack()



pLabel = Label(frameTela2,
                text ='Precisão')

pEntry = Entry(
    frameTela2,
    font=("Arial", 15)
)

ret = Button(frameTela2,text='retornar', command=Tela1)

calcular = Button(master=frameTela2, command = displayResult, text = 'calcular')
calcular.pack()

Tela1()

Janela.mainloop()
