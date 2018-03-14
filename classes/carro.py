from veiculo import Veiculo

class Carro(Veiculo):


    def __init__(self, qtd_rodas, cor, marca, modelo):
        super(Carro, self).__init__(qtd_rodas, cor, marca)
        self.modelo = modelo

    def abastecer(self):
        print("abastecendo o carro")

    def freiar(self):
        print("Freio do carro")

        