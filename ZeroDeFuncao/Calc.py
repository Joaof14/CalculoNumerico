from sympy import expand, Symbol, Subs, diff
from sympy.plotting import plot
xS = Symbol('x') #declarando que o caractere x no input será tratado 
#como um símbolo e será armazenado na variavel xS

#variável self.linha que será atualizada para inserir no arquivo de texto

#criando classe para calculo de zero função com seus metodos
class CalcZeroF():

    #declarando variáveis
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    gr = None
    #função para verificar metodo chamado
    def Atribui(self, f,a,b,p):
        self.i = 0
        self.f = expand(f)
        self.a = float(a)
        self.b = float(b)
        self.p = float(expand(p))
        self.cond = True
        self.fa = self.f.subs(xS, self.a)
        self.fb = self.f.subs(xS, self.b)
        self.file = open("resolução.txt","w")
        self.linha = ""
        self.resultado = ''
        self.file.close()
        self.aI = self.a
        self.bI = self.b
        
    #função para gráfico
    def grafico(self, a,b,f):
        self.resultado = ""
        try: 
            f = expand(f)
            self.aI = float(a)
            self.bI = float(b)
            self.gr = plot(f,(xS,self.aI,self.bI))
        except:
            try:
                self.resultado ="se tiver preenchido o intervalo, verifique se está correto"
                f = expand(f)
                self.gr = plot(f,(xS, -30.0, 30.0))
                self.gr.save('gráfico.png')
            except:
                self.resultado +="\nverifique se preencheu a função corretamente"
        
        
        

    #função para calculo geral
    def calc(self):
        #update nas iterações

        self.i  += 1
        #verificações na função
        if self.fa*self.fb >= 0:
            self.resultado = 'iteração: ' + str(self.i) + '\n'
            if self.fa == 0:
                self.resultado  += "\na raíz da função é a = " + str(self.a)
                self.cond = False
            elif self.fb == 0:
                self.resultado += "\na raíz da função é b = " + str(self.b) 
                self.cond = False
            else:
                self.resultado += "não há garantia de raíz no local"
                self.cond=False
            
        else:
            self.fx = float(self.f.subs(xS, self.x))
            self.outputtxt()
            if abs(self.fx) < self.p:
                self.resultado = " \na raíz da função é: " + str(self.x)
                self.cond = False
            elif self.fa*self.fx > 0:
                self.linha += "Temos que f(a)* f(x) é positivo, logo, pelo teorema de bolzano \n"
                self.linha += "sabemos que não existe raízes entre eles, enquanto que f(a)*f(b) é negativo \n"
                self.linha += "portanto existe pelo menos uma raíz entre eles, com isso a recebe x \n \n"
                self.a = self.x
                self.fa = float(self.f.subs(xS, self.a))
            else:
                self.linha += "Temos que f(a)* f(x) é positivo, logo, pelo teorema de bolzano \n"
                self.linha += "sabemos que não existe raízes entre eles, enquanto que f(a)*f(b) é negativo \n"
                self.linha += "portanto existe pelo menos uma raíz entre eles, com isso a recebe x \n \n"
                self.b = self.x
                self.fb = float(self.f.subs(xS, self.b))
        return self.cond

    #método da bissecção, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def Bis(self):
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método da bissecção \n \n"
            self.x = (self.a + self.b)/2
            self.cond = self.calc()
        self.outputtxt()

    #método da falsa posição, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def FalsaPos(self):
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método da falsa posição \n \n"
            self.x = float(((self.a*self.fb)-(self.b*self.fa))/(self.fb-self.fa))
            self.cond = self.calc()
        self.outputtxt()

    #método do ponto fixo, com seu respectivo x
    def PontoFixo(self, ChuteI, fIter):
        try:
            self.x = float(ChuteI)
            fIter = expand(fIter)
        except:
            self.resultado = "cuidado ao inserir os valores!"
            return 0
        self.i = -1
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método do ponto fixo\n \n"
            self.linha += "função de iteração: " + str(fIter) + "\n"
            if self.i >= 0:   
                self.x = fIter.subs(xS,self.x)
            try:
                self.cond = self.calc()
                self.verificaConvergencia()
            except:
                self.resultado = "método não convergiu"
                self.cond = False
            
        self.verificaResultado()

 #método de newton, com seu respectivo x
    def Newton(self, ChuteI):
        try:
            self.x = float(ChuteI)
        except: 
            self.resultado = "cuidado ao inserir os valores!"
            return 0
        flinha = diff(self.f, xS)
        self.i = -1
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método de Newton \n \n"
            if self.i >= 0:
                self.x = float(self.x - (self.f.subs(xS,self.x)/flinha.subs(xS,self.x)))
            try:
                self.cond = self.calc()
                self.verificaConvergencia()
            except:
                self.resultado = "método não convergiu"
                self.cond = False
        self.verificaResultado()

    #método da secante, com seu respectivo x
    def Secante(self):
        x = []
        fx = []
        x.append(self.a)
        fx.append(self.fa)
        x.append(self.b)
        fx.append(self.fb)
        self.i = -1
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método da secante \n \n"
            if self.i > 0:
                xk = float(x[self.i]-((self.fx* (x[self.i]-x[self.i-1]))/(fx[self.i]-fx[self.i - 1])))
                try:
                    x.append(xk)
                    self.x = xk
                    self.cond = self.calc()
                    fx.append(self.fx)
                    self.verificaConvergencia()
                except:
                    self.resultado = "método não convergiu"
                    self.cond = False
            else:
                self.i += 1
                self.fx = float(fx[self.i])
                self.x = float(x[self.i])
                self.outputtxt()
        self.verificaResultado()




    def verificaConvergencia(self):
        if (self.bI > self.aI) and (self.x > self.bI + 3 or self.x < self.aI - 3):
            self.resultado = "x se afastou demais do intervalo"
            self.cond = False
        elif (self.bI < self.aI) and (self.x > self.aI + 3 or self.x < self.bI - 3):
            self.resultado = "x se afastou demais do intervalo"
            self.cond = False

    def verificaResultado(self):
        if self.fx < self.p and not (
            (self.x <= self.aI and self.x >= self.bI) or (self.x >= self.aI and self.x <= self.bI)):
            self.resultado = "x = " + str(self.x)
            self.resultado += "\nraíz encontrada mas não está no intervalo"
        self.outputtxt()

    def outputtxt(self):
        self.file = open('resolução.txt', 'a')
        if self.resultado == '' and self.i <= 50:
            self.linha += "função estudada: " + str(self.f) + '\n\n'
            self.linha += 'iteração: ' + str(self.i) + '\n' 
            self.linha += "a: "+ str(self.a) + "    fa: "+ str(self.fa) + "\n"
            self.linha += "b: " + str(self.b) + "   fb: " + str(self.fb) + "\n"
            self.linha += "x: "+ str(self.x) + "    fx: " + str(self.fx) + "\n\n"
        elif self.resultado == '' and self.i > 50:
            self.resultado = "a calculadora alcançou seu limite de iterações\n" + "x: " + str(self.x)
        else:
            self.linha = self.resultado
        self.file.write(self.linha)
        self.file.close()
        self.linha = ''