#Chute um numero
#Criar um algoritmo que gera um valor aleatório e eu tenho que tentar adivinhasr que numero é através de 
#dicas como "chute um valor mais alto" ou "chute um valor mais baixo"
import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        
    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto')
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:    
                    self.tentar_novamente = False
                    print("Parabéns você acertou")
        except:
            print('Favor digitar apenas número!')
            self.Iniciar()
                
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero: ')
        
        
    def GerarNumeroAleatorio(self):
         self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)


chute = ChuteONumero()
chute.Iniciar()