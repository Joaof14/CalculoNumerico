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
    font=("Arial", 15)
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

for i in range(len(metodos)):
    opc = Radiobutton(  window,
                        text=metodos[i],
                        variable=metodo,
                        value=metodos[i],
                        command=chamarMetodo,
                        indicatoron=0,
                        bg="gray")
    opc.pack()

window.mainloop()