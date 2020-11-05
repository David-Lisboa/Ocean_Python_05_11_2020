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

# Acessar intervalos da lista

lista = [10, 30, 5, 4, 9, 12, 300]

# Começa no índice 0 e vai até o índice 2
print(lista[0:2])

# Comparando com horário do relógio:
# O curso do Ocean é das 13 às 16h
# das 13 às 16
# 13:16
# No python, o segundo número não é incluído
# Portanto, se a aula vai das 13h às 16h,
# a declaração seria 13:17, pois ele para antes do 17h

# Vai do segundo até o terceiro
print(lista[1:3])
#         0, 1,  2, 3, 4,  5,   6
lista = [10, 30, 5, 7, 9, 12, 300]  # Total 7 elementos
# Vai do quinto até o sétimo
print(lista[7 - 3:7])

#         0, 1,  2, 3, 4,  5,   6,  7,  8
lista = [10, 30, 5, 7]  # Total 9 elementos
# Quero pegar sempre os três últimos
print(lista[len(lista) - 3:len(lista)])

#         0, 1,  2, 3, 4,  5,   6,  7,  8
lista = [10, 30, 5, 7]  # Total 9 elementos
# Quero pegar sempre os três últimos
print(lista[-3:])

print(lista[0:3])  # começa no indice 0 e vai ate o indice 3-1

# quero pegar sempre os 3 ultimo
print(lista[-3:])

# for:

animais = ['gato', 'rato', 'cachorro', 'papagaio', 'morcego']

for animal in animais:
    print(animal)

# Uma string nada mais é que uma cadeia de caracteres
# Ou seja, pode ser considerada com uma lista de caracteres

nome = "Paulo Salvatore"

primeira_letra = nome[0]

print(primeira_letra)

ultima_letra = nome[-1]

print(ultima_letra)

primeiro_nome = nome[0:5]
print(primeiro_nome)

# Declaro a lista
animais = ['morcego', 'papagaio', 'leão']
print(animais)

# Adiciono um elemento no final
animais.append('girafa')
print(animais)

# Substituo o primeiro elemento (ou qualquer um, acessando pelo índice)
animais[0] = 'cachorro'
print(animais)

# Inserindo um elemento em algum índice específico (sem substituir)
animais.insert(1, 'gato')
print(animais)

# Onde está a girafa?
# Obtendo o índice de um elemento pelo valor dele
indice_girafa = animais.index('girafa')
print("O elemento 'girafa' está no índice", indice_girafa)

# Como eu removo um elemento pelo valor?
animais.remove('leão')
print(animais)

# Como eu removo um elemento pelo índice?
del animais[1]
print(animais)

# Como eu removo o último elemento da lista?
animais.pop()
print(animais)

# Também posso passar um índice para que pop remova-o da lista
animais.pop(0)
print(animais)

# Quantidade de itens na lista
quantidade_elementos = len(animais)
print("A lista possui", quantidade_elementos, "elemento(s)")

# Qual a diferença entre o pop e o del?
# O pop retorna o valor que foi removido

# Pop vs Del

animais = ['morcego', 'papagaio', 'leão']
print(animais)

indice = 1

# Quero obter o 'papagaio', mas automaticamente já removê-lo da lista, posso usar o pop

animal = animais.pop(indice)

print(animal)
print(animais)

# Como seria o mesmo código anterior usando o del?

# Pop vs Del

animais = ['morcego', 'papagaio', 'leão']
print(animais)

indice = 1

# Quero obter o 'papagaio', mas automaticamente já removê-lo da lista, posso usar o pop

animal = animais[indice]
del animais[indice]

print(animal)
print(animais)

# For: Vai varrer TODA a lista
# Também é possível usar o for para executar um determinado número de vezes

animais = ['gato', 'cachorro', 'papagaio', 'girafa', 'morcego']

print(animais[0])
print(animais[1])
print(animais[2])
print(animais[3])

print('\n')

# Posso substituir os prints por um for, que irá rodar um print para cada animal da lista

for animal in animais:
    # Em cada execução, teremos um valor diferente na variável animal
    print(animal)

qdt_lista = int(input("valor:"))
numeros = []

for indice in range(quantidade_de_elemetos):
    numeros.append(int(input("valor")))
print("lista:", numeros)

# Para fazer um for que rode um determinado número de vezes, sem necessariamente varrer uma lista
# utilizamos o range

# range(3) -> [0, 1, 2]
# range(5) -> [0, 1, 2, 3, 4]

# Range é um tipo de variável customizado, mas que também pode ser "varrido" pelo for
# A melhor palavra para substituir esse "varrendo" o for, é o "iterable" ou simplesmente "iterável"
# Quando eu falo que uma informação é "interável", significa que eu posso percorrer por todos os elementos
# dessa informação, utilizando técnicas como "for", acesso via índice, etc

print(range(5), type(range(5)))

# Eu também posso converter o range(5) para uma lista

lista_numeros = list(range(5))
print(lista_numeros, type(lista_numeros))

for indice in range(5):
    print(indice)

tupla = (5, 4, 9)

print(tupla, type(tupla))

# Tupla vs Lista

lista = [5, 4, 9]
lista[0] = 99
print(lista)
print(lista[0])

# Na tupla, não podemos mudar os valores dela
tupla = (5, 4, 9)
print(tupla)
print(tupla[0])

# Apesar de parecer que uma tupla precisa de parênteses, na verdade ela não precisa

tupla = 4, 9, 2, 3
print(tupla, type(tupla))

tupla_um_elemento = 5,
print(tupla_um_elemento, type(tupla_um_elemento))


# Só necessário colocar os parênteses quando estou criando uma tupla dentro de uma chamada de função

# Por exemplo: exibir_numeros((5, 3)) -> Nesse caso, (5, 3) é uma tupla. Se eu passar sem os parênteses, o python
# entenderá que 5 e 3 são argumentos da função

def teste1(numeros):
    print(numeros, numeros[0])


teste1((5, 2))


def teste2(numero1, numero2):
    print(numero1, numero2)


teste2(5, 2)

# Quero manipular a tupla, como faço? Simples, converte pra lista e trabalha normalmente

tupla = 5, 9, 1, 3

print(tupla, type(tupla))

lista_convertida = list(tupla)
print(lista_convertida, type(lista_convertida))
lista_convertida.append(5)
print(lista_convertida, type(lista_convertida))

# Desconstrução de tuplas

tupla_animais = 'gato', 'papagaio', 'cachorro'

print(tupla_animais, type(tupla_animais))

animal1, animal2, animal3 = tupla_animais

print(animal1, animal2, animal3)

tupla = 125.5, 'C'

temperatura, tipo = tupla
print(f'{temperatura}º{tipo}')


# Utilizando a desconstrução de tuplas em uma função

def converter_temperatura():
    temperatura_convertida = 50.5
    tipo_temperatura = 'C'
    return temperatura_convertida, tipo_temperatura


temp, tipo = converter_temperatura()

print(temp, tipo)


def pegar_tupla_numeros():
    numeros = range(100)

    return tuple(numeros)


tupla_numeros = pegar_tupla_numeros()

print(tupla_numeros, type(tupla_numeros))
