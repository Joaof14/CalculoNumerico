from tkinter import *
from Calc import CalcZeroF

#cria objeto para calcular
FunCalc = CalcZeroF()

#função para chamar a classe com parametros para seus atributos
def Controle():
    #atribui valores aos atributos do objeto
    FunCalc.Atribui(f=fEntry.get(), a=aEntry.get(), b=bEntry.get(),p=pEntry.get())

    #checa o método a ser utilzado
    if metodo.get() == FunCalc.nomes[0]:
        FunCalc.Bis()
    elif metodo.get() == FunCalc.nomes[1]:
        FunCalc.FalsaPos()
    elif metodo.get() == FunCalc.nomes[2]:
        FunCalc.PontoFixo(ChuteI=chuteIEntry.get(), fIter=fIEntry.get())
    elif metodo.get() == FunCalc.nomes[3]:
        FunCalc.Secante()
    elif metodo.get() == FunCalc.nomes[4]:
        FunCalc.Newton(ChuteI=chuteIEntry.get(), fIter=fIEntry.get())
    else:
        print("método não selecionado")

def grafico():
    #chama grafico
    FunCalc.grafico(a=aEntry.get(), b=bEntry.get(),f=fEntry.get())

window = Tk() #instanciando a classe Tk para criar uma janela

window.geometry("480x480")
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
graf = Button(window,
              text='Gráfico',
              command=grafico)
graf.pack()
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

fILabel = Label( window,
                text ='função de iteração para metodo do ponto fixo') #cria label e indica o que nele deve estar escrito
fILabel.pack() #insere label na janela
fIEntry = Entry(
    window,
    font=("Arial", 15), #cria prompt de entrada
)
fIEntry.pack()

chuteILabel = Label( window,
                text ='chute inicial para metodo do ponto fixo') #cria label e indica o que nele deve estar escrito
chuteILabel.pack() #insere label na janela
chuteIEntry = Entry(
    window,
    font=("Arial", 15), #cria prompt de entrada
)
chuteIEntry.pack()


window.mainloop() #faz janela aparecer
