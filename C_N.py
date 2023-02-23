from tkinter import *
from Calc import CalcZeroF

window = Tk()
fLabel = Label( window,
                text ='função')
fLabel.pack()
fEntry = Entry(
    window,
    font=("Arial", 15),
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

#função para chamar a classe com parametros para seus atributos
def chamaClasse():
    #atualiza variáveis que serão parametros para atributos da classe
    fun = fEntry.get()
    aI = aEntry.get()
    bI = bEntry.get()
    pr = pEntry.get()
    metd = metodo.get()

    CalcZeroF.verificaMetodo(self = CalcZeroF, f=fun, a=aI, b=bI,p=pr,metodo=metd)

for i in range(len(CalcZeroF.nomes)):
    opc = Radiobutton(  window,
                        text=CalcZeroF.nomes[i],
                        variable=metodo,
                        value=CalcZeroF.nomes[i],
                        command=chamaClasse,
                        indicatoron=0,
                        bg="gray")
    opc.pack()
window.mainloop()
