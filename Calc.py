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
        self.iter = 0
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
        self.linha += 'iteração: ' + str(self.iter) + '\n' 
        self.iter  += 1
        self.linha += "a: "+ str(self.a) + "    fa: "+ str(self.fa) + "\n"
        self.linha += "b: " + str(self.b) + "   fb: " + str(self.fb) + "\n"
        self.fx = self.f.subs(xS, x)
        self.outputtxt()
        self.linha += "x: "+ str(x) + "    fx: " + str(self.fx) + "\n"
        if self.fa*self.fb <= 0:
            if abs(self.fx) < self.p:
                self.linha+= " \na raíz da função é: " + str(x)
                self.cond = False
            elif self.fa == 0:
                self.linha += "\na raíz da função é: " + str(self.a)
                self.cond = False
            elif self.fb == 0:
                self.linha += "\na raíz da função é: " + str(self.b) 
                self.cond = False
            else:
                if self.fa*self.fx > 0:
                    self.linha += "Temos que f(a)* f(x) é positivo, logo, pelo teorema de bolzano \n"
                    self.linha += "sabemos que não existe raízes entre eles, enquanto que f(a)*f(b) é negativo \n"
                    self.linha += "portanto existe pelo menos uma raíz entre eles, com isso a recebe x \n \n"
                    self.a = x
                else:
                    self.linha += "Temos que f(a)* f(x) é positivo, logo, pelo teorema de bolzano \n"
                    self.linha += "sabemos que não existe raízes entre eles, enquanto que f(a)*f(b) é negativo \n"
                    self.linha += "portanto existe pelo menos uma raíz entre eles, com isso a recebe x \n \n"
                    self.b = x  
        else:
            self.linha+= "não há garantia de raíz no local"
            self.cond=False
        self.outputtxt()
        return self.cond

    #método da bissecção, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def Bis(self):
        self.linha = self.linha + "método da bissecção \n \n"
        while self.cond and self.iter <= 50:
            self.fa = self.f.subs(xS, self.a) #descobrimos f(a) e fb substituindo a e b em f(x)
            self.fb = self.f.subs(xS, self.b) #para isso, é usado a função a subs
            x = (self.a + self.b)/2
            self.cond = self.calc(x)

    #método da falsa posição, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def FalsaPos(self):
        self.linha = self.linha + "método da bissecção \n \n"
        while self.cond and self.iter <= 50:
            self.fa = self.f.subs(xS, self.a) 
            self.fb = self.f.subs(xS, self.b)
            x = ((self.a*self.fb)-(self.b*self.fa))/(self.fb-self.fa)
            self.cond = self.calc(x)

    #método do ponto fixo, com seu respectivo x
    def PontoFixo(self, ChuteI, fIter):
        x = float(ChuteI)
        fIter = expand(fIter)
        while self.cond and self.iter <= 50:
            if self.iter != 0:
                x = fIter.subs(xS,x)
            self.fa = self.f.subs(xS, self.a) 
            self.fb = self.f.subs(xS, self.b)
            self.cond = self.calc(x)

        print("método do ponto fixo")

    #método da secante, com seu respectivo x
    def Secante():
        print("método da secante")

    #método de newton, com seu respectivo x
    def Newton():
        print("método de newton")

    def outputtxt(self):
        self.file = open('resolução.txt', 'a')
        self.file.write(self.linha)
        self.file.close()
        self.linha = ''