def middle(lista):
    lista.pop(0)
    lista.pop()
    return lista
lista = [1,2,3,4,5]
print(middle(lista))