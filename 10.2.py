def cumsum(lista):
    lista_somada = sum(lista)
    nova_lista = lista
    nova_lista.pop()
    nova_lista.append(lista_somada)
    return nova_lista
lista = [1,2,3]
print(cumsum(lista))