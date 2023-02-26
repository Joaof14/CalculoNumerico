from sympy import expand, Symbol, Subs
from sympy.plotting import plot
xS = Symbol('x') #declarando que o caractere x no input será tratado 
#como um símbolo e será armazenado na variavel xS

#variável self.linha que será atualizada para inserir no arquivo de texto

#criando classe para calculo de zero função com seus metodos
class CalcZeroF():

    #declarando variáveis
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    #função para verificar metodo chamado
    def Atribui(self, f,a,b,p):
        self.f = expand(f)
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.cond = True
        self.linha = ""
        self.i = 0
        self.fa = self.f.subs(xS, self.a) 
        self.fb = self.f.subs(xS, self.b)
        self.file = open("resolução.txt","w")
        self.file.close()
        
    #função para gráfico
    def grafico(self, f,a,b):
        try:
            self.gr = plot(self.f,(xS,a,b),show = False)
        except:
            print("something wrong")

    #função para calculo geral
    def calc(self, x):
        self.fx = self.f.subs(xS, self.x)
        self.outputtxt()
        self.i  += 1
        
        if self.fa*self.fb <= 0:
            if abs(self.fx) < self.p:
                self.linha = " \na raíz da função é: " + str(self.x)
                self.cond = False
            elif self.fa == 0:
                self.linha  = "\na raíz da função é: " + str(self.a)
                self.cond = False
            elif self.fb == 0:
                self.RESU = "\na raíz da função é: " + str(self.b) 
                self.cond = False
            else:
                if self.fa*self.fx > 0:
                    self.linha += "Temos que f(a)* f(x) é positivo, logo, pelo teorema de bolzano \n"
                    self.linha += "sabemos que não existe raízes entre eles, enquanto que f(a)*f(b) é negativo \n"
                    self.linha += "portanto existe pelo menos uma raíz entre eles, com isso a recebe x \n \n"
                    self.a = self.x
                    self.fa = self.f.subs(xS, self.a) 
            
                else:
                    self.linha += "Temos que f(a)* f(x) é positivo, logo, pelo teorema de bolzano \n"
                    self.linha += "sabemos que não existe raízes entre eles, enquanto que f(a)*f(b) é negativo \n"
                    self.linha += "portanto existe pelo menos uma raíz entre eles, com isso a recebe x \n \n"
                    self.b = self.x
                    self.fb = self.f.subs(xS, self.b)
        else:
            self.linha+= "não há garantia de raíz no local"
            self.cond=False
        return self.cond

    #método da bissecção, com seu respectivo self.x, chamando o cálculo geral enquanto resultado for válido
    def Bis(self):
        self.linha = self.linha + "método da bissecção \n \n"
        self.x = (self.a + self.b)/2
        self.cond = self.calc(self.x)

    #método da falsa posição, com seu respectivo self.x, chamando o cálculo geral enquanto resultado for válido
    def FalsaPos(self):
        self.linha = self.linha + "método da bissecção \n \n"
        self.x = ((self.a*self.fb)-(self.b*self.fa))/(self.fb-self.fa)
        self.cond = self.calc(self.x)

    #método do ponto fiself.xo, com seu respectivo self.x
    def PontoFixo(self, ChuteI, fIter):
        self.x = float(ChuteI)
        fIter = expand(fIter)
        if self.i != 0:
            self.x = fIter.subs(xS,self.x)
        self.cond = self.calc(self.x)

        print("método do ponto fixo")

 #método de newton, com seu respectivo self.x
    def Newton(self, ChuteI,fIter):
        self.x = float(ChuteI)
        fIter = expand(fIter)
        while self.cond and self.i <= 50:
            if self.i != 0:
                self.x = fIter.subs(xS,self.x)
            self.cond = self.calc(self.x)
        


    #método da secante, com seu respectivo self.x
    def Secante(self):
        self.x = []
        fx = []
        while self.cond and self.i <= 50:
            if self.i >= 2:
                fx.append(self.fx)
                xk = self.x[self.i-1]-((self.fx* (self.x[self.i-1]-self.x[self.i-2]))/(fx[self.i-1]-fx[self.i - 2]))
                print(xk)
                self.x.append(xk)
            elif self.i == 0: 
                self.x.append(self.a)
                fx.append(self.fa)
                self.x.append(self.b)
                fx.append(self.fb)
            print(fx[self.i])
            self.cond = self.calc(self.x[self.i])
        print(self.x)
    print("método da secante")
    


    def outputtxt(self):
        self.file = open('resolução.txt', 'a')
        self.linha += 'iteração: ' + str(self.i) + '\n' 
        self.linha += "a: "+ str(self.a) + "    fa: "+ str(self.fa) + "\n"
        self.linha += "b: " + str(self.b) + "   fb: " + str(self.fb) + "\n"
        self.linha += "x: "+ str(self.x) + "    fx: " + str(self.fx) + "\n"
        self.file.write(self.linha)
        self.file.close()
        self.linha = ''