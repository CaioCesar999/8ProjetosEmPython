# Simulador de Dado
#Simular um dado que gera um valor de 1 até 6
import random
import PySimpleGUI as sg

class SimuladorDeDado:
    valor_minimo = 1
    valor_maximo = 6
    mensagem = 'Você gostaria de gerar um novo valor para o  dado?'
    
    def __int__(self):
        self.valor_minimo
        self.valor_maximo
        self.mensagem
        
        
        
    def Iniciar(self):
        #Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('sim'),sg.Button('não')]
        ]
        
        #criar janela
        self.janela = sg.Window('Simulador de Dado', layout= self.layout)
        #ler os valores da tela
        self.eventos, self.valores = self.janela.Read() 
        #resposta = input(self.mensagem)
        #Fazer alguma coisa com os valores
    
        try:
            if self.eventos == 'sim' or self.eventos == 's':
                self.GerarValorDoDado()
            elif self.eventos == 'não' or self.eventos == 'n':
                print('Agradecemos sua participação!')
            else:
                print('Favor digitar sim ou não')        
        except:
            print("Ocorreu um erro ao receber a sua resposta")     
                
    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
