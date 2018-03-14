import sys

sys.path.append('classes')

from classes.veiculo import Veiculo
from classes.moto import Moto
from classes.carro import Carro


'''
Projeto apenas para estudo da Linguagem Python
'''


##Teste polimorfismo
civic = Carro(4, "vermelho", "fiat", "sedan")
tenere = Moto(2, 'Azul', "Yamaha", "Trail")

lista_veiculos = []
lista_veiculos.append(civic)
lista_veiculos.insert(1, tenere)

for veiculo in lista_veiculos:
    veiculo.freiar()
    ##Exemplo de algo como um toString
    print(str(veiculo))

    ##Conversao para dicionario
    print(veiculo.__dict__)


##Teste do tryCatch 


    if type(veiculo) is Moto :
        try:
            veiculo.empinar()
        except Exception as e:
            raise e





