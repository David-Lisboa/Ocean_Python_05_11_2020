# Dicionários são semelhantes às listas, porém, podemos dar nomes aos índices

dicionario = {
    'nome_indice': 'valor'
}
print(dicionario)

item = dicionario['nome_indice']
print(item)
paulo = {
    'nome': 'Paulo',
    'sobrenome': 'Salavatore',
    'idade': 26
}

Giovana = {
    'nome': 'Giovana',
    'sobrenome': 'Souza',
    'idade': 26,
    'altura': 1.63
}


def exibir_pessoa(pessoa):
    print(f"{pessoa['nome']} {pessoa['sobrenome']}")
    print(f"Idade: {pessoa['idade']}")

    if 'cor_cabelo' in pessoa:
        print(f"Cor do Cabelo: {pessoa['cor_cabelo']}")

    if 'altura' in pessoa:
        print(f"Altura: {pessoa['altura']}m")

    print()


exibir_pessoa(paulo)
exibir_pessoa(Giovana)

pessoas = [
    {
        'nome': 'Paulo',
        'sobrenome': 'Salvatore',
        'idade': 26,
        'altura': 1.65
    },
    {
        'nome': 'Giovanna',
        'sobrenome': 'Souza',
        'idade': 23,
        'cor_cabelo': 'Loiro',
        'altura': 1.63
    },
    {
        'nome': 'Luiz',
        'sobrenome': 'Silva',
        'idade': 28,
        'cor_cabelo': 'Castanho',
        'altura': 1.71
    }
]


def exibir_pessoa(pessoa):
    print(f"{pessoa['nome']} {pessoa['sobrenome']}")
    print(f"Idade: {pessoa['idade']}")

    if 'cor_cabelo' in pessoa:
        print(f"Cor do Cabelo: {pessoa['cor_cabelo']}")

    if 'altura' in pessoa:
        print(f"Altura: {pessoa['altura']}m")

    print()

    # for pessoa in pessoas:


exibir_pessoa(pessoas[2])

dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
    'chave4': 'valor4',
    'chave5': 'valor5'
}

# print(dicionario)
# print(dicionario.keys())

# Outra forma de pegar chaves
for key in dicionario.keys():
    print(dicionario[key])

# Chaves e índices numéricos
for indice, chave in enumerate(dicionario):
    print(chaindiceve, chave)

# Apenas chaves:
for chave in dicionario:
    print(chave)

# Se quiserem estudar

config = {
    'f': {
        'c': lambda f: 5 * (f - 32) / 9
    },
    'c': {
        'f': lambda c: (9 * c / 5) + 32,
        'k': lambda c: c + 273.15
    }
}


def converter_temperatura(de, para, valor):
    if de in config and para in config[de]:
        return config[de][para](valor)
    else:
        print("Tipo não suportado.")


print(converter_temperatura('c', 'f', 100))
print(converter_temperatura('f', 'c', 212))
print(converter_temperatura('c', 'k', 0))
