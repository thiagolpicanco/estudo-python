from veiculo import Veiculo

import sys
sys.path.append('../')

from excessoes.ForaLei import ForaLeiException 

class Moto(Veiculo):


    def __init__(self, qtdRodas, cor, marca, categoria):
        super(Moto, self).__init__(qtdRodas, cor, marca)
        self.categoria = categoria

    def abastecer(self):
        print("abastecendo a moto")

    def freiar(self):
        print("Freio moto")

    def empinar(self):
        raise ForaLeiException("Proibido empinar")

    def __str__(self):
        return "Moto da categoria: %s ,de cor %s, da marca %s" %(self.categoria, self.cor, self.marca)