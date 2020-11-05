for indice in range(2):
    elemento_da_lista = int(input("elemento:"))

    if elemento_da_lista % 2 == 0:
        print(f"elemento {elemento_da_lista} é par")
    else:
        print(f"elemento {elemento_da_lista} é par")

# 2 forma
lista_de_pares = []
lista_de_inpares = []

for indice in range(2):
    elemento_da_lista = int(input("elemento:"))

    if elemento_da_lista % 2 == 0:
        lista_de_pares.append(elemento_da_lista)
    else:
        lista_de_inpares.append(elemento_da_lista)
print("lista par",lista_de_pares)
print("lista inpares",lista_de_inpares)
