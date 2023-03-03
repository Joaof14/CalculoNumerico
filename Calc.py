from sympy import expand, Symbol, Subs, diff
from sympy.plotting import plot
xS = Symbol('x') #declarando que o caractere x no input será tratado 
#como um símbolo e será armazenado na variavel xS

#variável self.linha que será atualizada para inserir no arquivo de texto

#criando classe para calculo de zero função com seus metodos
class CalcZeroF():

    #declarando variáveis
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    linha = ""
    i = 0
    file = open("resolução.txt","w")
    resultado = ''
    file.close()
    
    #função para verificar metodo chamado
    def Atribui(self, f,a,b,p):
        self.f = expand(f)
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.cond = True
        self.fa = self.f.subs(xS, self.a)
        self.fb = self.f.subs(xS, self.b)
        
    #função para gráfico
    def grafico(self, a,b,f):
        try: 
            f = expand(f)
            try:
                self.a = float(a)
                self.b = float(b)
                self.gr = plot(f,(xS,self.a,self.b))
            except:
                self.gr = plot(f,(xS, -30, 30))
            self.gr.save('gráfico.png')
        except:
            print("verifique se preencheu a função corretamente")
        

    #função para calculo geral
    def calc(self, x):
        self.x = float(x)
        self.fx = float(self.f.subs(xS, self.x))
        self.outputtxt()
        self.i  += 1
        
        if self.fa*self.fb <= 0:
            if abs(self.fx) < self.p:
                self.resultado = " \na raíz da função é: " + str(self.x)
                self.cond = False
            elif self.fa == 0:
                self.resultado  = "\na raíz da função é: " + str(self.a)
                self.cond = False
            elif self.fb == 0:
                self.resultado = "\na raíz da função é: " + str(self.b) 
                self.cond = False
            else:
                if self.fa*self.fx > 0:
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
        else:
            self.resultado = "não há garantia de raíz no local"
            self.cond=False
        return self.cond

    #método da bissecção, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def Bis(self):
        self.i = 1
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método da bissecção \n \n"
            x = (self.a + self.b)/2
            self.cond = self.calc(x)

    #método da falsa posição, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def FalsaPos(self):
        self.i = 1
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método da falsa posição \n \n"
            x = ((self.a*self.fb)-(self.b*self.fa))/(self.fb-self.fa)
            self.cond = self.calc(x)

    #método do ponto fixo, com seu respectivo x
    def PontoFixo(self, ChuteI, fIter):
        x = float(ChuteI)
        fIter = expand(fIter)
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método do ponto fixo\n \n"
            if self.i != 0:
                x = fIter.subs(xS,x)
            self.cond = self.calc(x)


 #método de newton, com seu respectivo x
    def Newton(self, ChuteI,fIter):
        x = float(ChuteI)
        flinha = diff(self.f, xS)
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método de Newton \n \n"
            if self.i != 0:
                x = float(x - (self.f.subs(xS,x)/flinha.subs(xS,x)))
            self.cond = self.calc(x)
        


    #método da secante, com seu respectivo x
    def Secante(self):
        x = []
        fx = []
        x.append(self.a)
        fx.append(self.fa)
        x.append(self.b)
        fx.append(self.fb)
        while self.cond and self.i <= 50:
            self.linha = self.linha + "método da secante \n \n"
            if self.i >= 2:
                xk = float(x[self.i-1]-((self.fx* (x[self.i-1]-x[self.i-2]))/(fx[self.i-1]-fx[self.i - 2])))
                x.append(xk)
                self.cond = self.calc(x[self.i])
                fx.append(self.fx)
            else:
                self.fx = float(fx[self.i])
                self.x = float(x[self.i])
                self.outputtxt()
                self.i += 1
            
    


    def verificaResultado(self, a, b):
        a = float(a) 
        b = float(b)
        if not ((self.x <= a and self.x >= b) or (self.x >= a and self.x <= b)):
            self.resultado = "raíz encontrada mas não está no intervalo"
        self.outputtxt()

    def outputtxt(self):
        self.file = open('resolução.txt', 'a')
        if self.resultado == '':
            self.linha += str(self.f) + '\n\n'
            self.linha += 'iteração: ' + str(self.i) + '\n' 
            self.linha += "a: "+ str(self.a) + "    fa: "+ str(self.fa) + "\n"
            self.linha += "b: " + str(self.b) + "   fb: " + str(self.fb) + "\n"
            self.linha += "x: "+ str(self.x) + "    fx: " + str(self.fx) + "\n\n"
        else:
            self.linha = self.resultado
        self.file.write(self.linha)
        self.file.close()
        self.linha = ''