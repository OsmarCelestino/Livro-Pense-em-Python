def numero_primo  (numero):
    n = 0
    contador = 2
    while contador <= numero:
        if(numero % contador == 0):
            n = n + 1
        contador = contador + 1
    if(n == 1):
        return n
    else:
        return 0
n = 0
while n != 1:
   numero = int(input("Digite um numero pra saber se ele é primo: "))
   n = numero_primo(numero)
   if(n != 1):
       print("O numero {} não é primo!!!".format(numero))
print("O numero {} é primo!!!".format(numero))