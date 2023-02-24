from tkinter import *
from Calc import CalcZeroF


#função para chamar a classe com parametros para seus atributos
def Controle():
    #cria objeto para calcular
    FunCalc = CalcZeroF()
    #atribui valores aos atributos do objeto
    FunCalc.Atribui(f=fEntry.get(), a=aEntry.get(), b=bEntry.get(),p=pEntry.get())
    #chama grafico
    FunCalc.grafico(f=fEntry.get(), a=aEntry.get(), b=bEntry.get())
    #checa o método a ser utilzado
    if metodo.get() == FunCalc.nomes[0]:
        FunCalc.Bis()
    elif metodo.get() == FunCalc.nomes[1]:
        FunCalc.FalsaPos()
    elif metodo.get() == FunCalc.nomes[2]:
        FunCalc.PontoFixo()
    elif metodo.get() == FunCalc.nomes[3]:
        FunCalc.Secante()
    elif metodo.get() == FunCalc.nomes[4]:
        FunCalc.Newton()
    else:
        print("método não selecionado")
    FunCalc.gr.show()
window = Tk() #instanciando a classe Tk para criar uma janela

fLabel = Label( window,
                text ='função') #cria label e indica o que nele deve estar escrito
fLabel.pack() #insere label na janela

fEntry = Entry(
    window,
    font=("Arial", 15), #cria prompt de entrada
)
fEntry.pack()

aLabel = Label( 
        window,
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

#cria botões de seleção para escolher método de cálculo
for i in range(len(CalcZeroF.nomes)):
    opc = Radiobutton(  window,
                        text=CalcZeroF.nomes[i],
                        variable=metodo,
                        value=CalcZeroF.nomes[i],
                        command=Controle,
                        indicatoron=0,
                        bg="gray")
    opc.pack()

window.mainloop() #faz janela aparecer
