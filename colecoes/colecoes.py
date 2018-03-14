
##Teste
def output(texto, colecao):
    print(texto + str(colecao))



'''
Alguns teste 
com lista'''

lista = ['teste1', 'teste2', 'teste3', 'teste1']

output('lista inicial', lista)
##acrescentar novo item na lista
lista.append('teste4')
output('lista com append', lista)

##tamanho da lista
print('tamanho lista %d'%len(lista))

##contar quantidade de ocorrencias do mesmo item na lista
print('a palavra teste1 esta presente %d vezes na lista'%lista.count('teste1'))


##inclui os dados de outra lista dentro da mesma
lista2 = ['teste100']
lista.extend(lista2)
output("adicionado dados de outra lista dentro da lista inicial", lista)


##Retornado o indice de um item
print('imprimindo o indice do item teste2: %d'% lista.index('teste2'))


##inverte a lista
lista.reverse()
output("lista invertida", lista)


##Remove ultimo elemneto como pilha
lista.pop()
output("ultimo removido", lista)

##Remove elemento especifico
lista.remove('teste1')
output("removido elemento teste1", lista)

##Ordena a lista
lista.sort()
output("ordenando lista", lista)


##Foreach
print("foreach")
for item in lista:
    print(item)

##Range
print("Range indice")
for i in range(len(lista)):
    print('elemento com range: '+ lista[i])


##Range depois segundo ate o quarto elemento
print('range')
for i in range(2,4):
    print(lista[i])
    




'''Tupla - algo como uma lista imutavel(mais performatico) '''
tupla = ('teste1', 'teste2', 'teste3')
tupla2 = tuple(tupla)


'''Dicionario - (Map)'''
print('--------------Iniciando Dicionario ------------------------')
dicionario = {'nome': 'teste1', 'idade': 23}
output('Dicionario iniciado: ', dicionario)

print("Buscando a chave nome")
print(dicionario.get('nome'))


print("Printando chaves")
for item in dicionario.keys():
    print(item)


#Conjunto - (Set)
print('--------------Iniciando Dicionario ------------------------')
conjunto = {'teste1', 'teste2'}
output("Conjunto iniciado: ", conjunto)

##Adicionado Item
conjunto.add('teste3')
output("adicionado teste3", conjunto)

##Tentando adicionar item repetido
conjunto.add('teste3')
output("teste repeticao item teste3", conjunto)
