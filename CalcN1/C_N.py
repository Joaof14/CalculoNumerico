from tkinter import *
from Calc import CalcZeroF


FunCalc = CalcZeroF() #cria objeto para calcular

window = Tk() #instanciando a classe Tk para criar uma janela
resultadoDisplay = Label(
        window, 
        font=("Arial", 15),
        text=""
    )
#função para chamar a classe com parametros para seus atributos
def displayResult():
    global resultadoDisplay
    resultadoDisplay.pack_forget()
    resultadoDisplay = Label(
        window, 
        font=("Arial", 15),
        text=FunCalc.resultado
    )
    resultadoDisplay.pack()
    
def Controle():
    #atribui valores aos atributos do objeto
    try: 
        FunCalc.Atribui(f=fEntry.get(), a=aEntry.get(), b=bEntry.get(),p=pEntry.get())
    except: 
        FunCalc.resultado = "verifique se preencheu tudo corretamente!"
        return 0
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
        FunCalc.Newton(ChuteI=chuteIEntry.get())
    else:
        print("método não selecionado")

    displayResult()
    
def grafico():
    #chama grafico
    FunCalc.grafico(a=aEntry.get(), b=bEntry.get(),f=fEntry.get())
    displayResult()

#atributos da janela
window.geometry("540x540")
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
                text ='chute inicial para metodo do ponto fixo ou Newton') #cria label e indica o que nele deve estar escrito
chuteILabel.pack() #insere label na janela
chuteIEntry = Entry(
    window,
    font=("Arial", 15), #cria prompt de entrada
)
chuteIEntry.pack()

resultado = Label(window,
                  text="Resultado",
                  font=("Arial", 15))
resultado.pack()

resultadoDisplay.pack()
window.mainloop() #faz janela aparecer
