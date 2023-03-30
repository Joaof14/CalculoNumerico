from tkinter import *
import Metodos

opc = []

Janela = Tk()

resultado = ''
def mostrarMetodos():
    global resultado
    try:
        Metodos.atribui(mA.get("1.0", "end"), mB.get("1.0", "end"))
        print(Metodos.A)
    except:
        print('Verifique se preencheu corretamente e corrija caso necessário clicando em retorna!')
    finally:
        mA.config(state='disabled')
        mB.config(state='disabled')
        Info.pack_forget()

        for i in range(len(Metodos.nomes)):
            opc.append(Radiobutton( Janela,
                                text=Metodos.nomes[i],
                                command = lambda: displayResult(i),
                                indicatoron=0,
                                state = 'normal'))
            opc[i].pack()
        pLabel.pack()
        pEntry.pack()
        ret.pack()
        if resultado != '':
            resultado.pack_forget()

def retornar():
    global resultado
    for i in range(len(Metodos.nomes)):
        opc[i].pack_forget()
    pEntry.pack_forget()
    pLabel.pack_forget()
    mA.config(state='normal')
    mB.config(state='normal')
    ret.pack_forget()
    
def displayResult(i):
    global resultado
    
    x = Metodos.metodos[i]()
    res = 'Solução do sistema:\n'
    for i, s in enumerate(x):
        print(f"x.{i+1} = {s}") 
        res += 'x.' + str(i+1) + ' = ' + str(s) + '\n'
    resultado = Label(text=res)
    resultado.pack()
    retornar()


Janela.geometry("500x500")
Janela.title('Calculadora de Sistemas de EQuações Lineares')

Info = Label(text="Separe as colunas por vírgula!", bg = 'green')
Info.pack()

mAl = Label(Janela, text='Matriz dos coeficientes A')
mAl.pack()
mA = Text(height= '6', font=('Arial', 15))
mA.pack()

mBl = Label(Janela, text='Matriz B dos resultados')
mBl.pack()
mB = Text(height='6',font=('Arial', 15))
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