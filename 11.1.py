arquivo = open('10.1.txt', "r")
lista = []
for linha in arquivo:
    linha = linha.strip()
    lista.append((linha))
lista_separada = lista[0]
lista = lista_separada.split()
dicio = dict(lista)

