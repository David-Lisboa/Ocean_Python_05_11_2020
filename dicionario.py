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
