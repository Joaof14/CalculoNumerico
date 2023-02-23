from sympy import expand, Symbol, Subs
xS = Symbol('x') #declarando que o caractere x no input será tratado 
#como um símbolo e será armazenado na variavel xS

#criando classe para calculo de zero função com seus metodos
class CalcZeroF():

    #declarando variáveis
    nomes = ("Bissecção", "Falsa Posição", "Ponto Fixo", "Secante", "Newton")
    cond = True
    #função para verificar metodo chamado
    def verificaMetodo(self, f,a,b,p, metodo):
        self.f = expand(f)
        self.a = float(a)
        self.b = float(b)
        self.p = float(p)
        self.fa = self.f.subs(xS, a)
        self.fb = self.f.subs(xS, b)
        #checa o método a ser utilzado
        if metodo == self.nomes[0]:
            self.Bis(self=CalcZeroF)
        elif metodo == self.nomes[1]:
            self.FalsaPos(self=CalcZeroF)
        elif metodo == self.nomes[2]:
            self.PontoFixo()
        elif metodo == self.nomes[3]:
            self.Secante()
        elif metodo == self.nomes[4]:
            self.Newton()
        else:
            print("método não selecionado")

    #função para calculo geral
    def calc(self, x):
        fx = self.f.subs(xS, x)
        if self.fa*self.fb <= 0:
            if abs(fx) < self.p:
                print("a raíz da função é: ", x)
                self.cond = False
            elif self.fa == 0:
                print("a raíz da função é: ", self.a)
                self.cond = False
            elif self.fb == 0:
                print("a raíz da função é: ", self.b)
                self.cond = False
            else:
                if abs(self.fa)>abs(self.fb):
                    self.a = x
                else:
                    self.b = x
                    print("")     
        else:
            print("não há garantia de raíz no local")
            self.cond=False
        return self.cond

    #método da bissecção, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def Bis(self):
        while self.cond:
            x = (self.a + self.b)/2
            print("a: ",self.a,"b: ",self.b,"x: ", x)
            self.cond = self.calc(self,x)
    #método da falsa posição, com seu respectivo x, chamando o cálculo geral enquanto resultado for válido
    def FalsaPos(self):
        print("método da falsa posição")
        while True:
            x = ((self.a*self.fb)-(self.b*self.a))/(self.b-self.a)
            print("a: ",self.a,"b: ",self.b,"x: ", x)
            self.cond = self.calc(self,x)
       

    #método do ponto fixo, com seu respectivo x
    def PontoFixo():
        print("método do ponto fixo")

    #método da secante, com seu respectivo x
    def Secante():
        print("método da secante")

    #método de newton, com seu respectivo x
    def Newton():
        print("método de newton")