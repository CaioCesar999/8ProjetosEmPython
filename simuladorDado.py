# Simulador de Dado
#Simular um dado que gera um valor de 1 até 6
import random
import PySimpleGUI

class SimuladorDeDado:
    valor_minimo = 1
    valor_maximo = 6
    mensagem = 'Você gostaria de gerar um novo valor para o  dado?'
    
    def __int__(self):
        self.valor_minimo
        self.valor_maximo
        self.mensagem

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
            if resposta == 'sim' or resposta == 's':
                self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')        
        except:
            print("Ocorreu um erro ao receber a sua resposta")     
            
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()