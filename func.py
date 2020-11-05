# Operador ternário no Python

idade = 15

maior_idade = idade >= 18

documento = 'cnh' if maior_idade else 'rg'
print(documento)

# lista

lista = [10, 30, 5, 4, 9, 12]
print(lista, type(lista))  # exibir lista e o tipo da lista
print(lista[0], type(lista[0]))  # exibir elemento na posição '0' e o tipo do elemento

quantidade_de_elemetos = len(lista)
ultimo_indice = quantidade_de_elemetos - 1

print(quantidade_de_elemetos, ultimo_indice)

ultimo_elemto = lista[ultimo_indice]

print(ultimo_elemto)

print(lista[0:3]) # começa no indice 0 e vai ate o indice 3-1

# quero pegar sempre os 3 ultimo
print(lista[-3:])

# for:

animais = ['gato', 'rato', 'cachorro', 'papagaio', 'morcego']

for animal in animais:
    print(animal)


qdt_lista = int(input("valor:"))
numeros=[]

for indice in range(quantidade_de_elemetos):
    numeros.append(int(input("valor")))
print("lista:", numeros)