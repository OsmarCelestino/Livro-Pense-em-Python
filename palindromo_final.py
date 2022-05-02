def sequencia_inversa(sequencia):
    return sequencia[::-1]
def palindromo(sequencia, sequencia_inversa):
    if(sequencia == sequencia_inversa):
        return True
    else:
        return False
def soma (primeira, segunda):
    primeira = int(primeira)
    segunda = int(segunda)
    string = primeira + segunda
    string = str(string)
    return string
pal = False
sequencia = input("Digite uma sequencia de números para ver se ela é um palindromo: ")
while pal == False:
    sequencia_invertida = sequencia_inversa(sequencia)
    pal = palindromo(sequencia, sequencia_invertida)
    print(sequencia)
    if pal == True:
        print("A sequencia {} é um palindromo".format(sequencia))
        break
    else:
        sequencia = soma(sequencia, sequencia_invertida)
