'''Programa simula um funcionamento de um parque de estacionamento. A classe estacionamento recebe um inteiro 
que determina a lotacao do parque e devolve um objecto com os seguintes metodos: entra(), corresponde a 
entrada de um carro; sai(), corresponde a saıda de um carro; lugares() indica o numero de lugares livres no estacionamento
'''

class Estacionamento:

    def __init__(self, lugares) :
        self.lugares = lugares
    
    def entra(self):
        self.lugares = self.lugares - 1

    def sai(self):
        self.lugares = self.lugares + 1

    def lugar(self):
        return self.lugares

ist = Estacionamento(20)

ist.entra()
ist.entra()
print(ist.lugar())
ist.entra()
ist.entra()
ist.sai()
ist.sai()
print(ist.lugar())
