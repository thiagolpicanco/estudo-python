
#Inicia Lista Comum
lista = [1,2,3,4,5]

#Copia elemento por elemento para a nova lista
lista2 = [x for x in lista]

#Copia todos os elementos que forem pares
lista_pares = [x for x in lista if x%2==0]

#Copia elementos ao quadrado da lista
lista_quadrado = [x**2 for x in lista]

print(lista)
print(lista2)
print(lista_pares)
print(lista_quadrado)


#Gerando lista dinamicamente de 1 a 10
listax = list(range(0, 11))
print(listax)

lista_letras = [letra for letra in "Testando teste"]
    
for item in zip(listax, lista_letras):
    print(item) 


