def is_palindrome(palavra):
    palavra_separada = palavra
    palavra_revertida = palavra[::-1]
    if palavra_separada == palavra_revertida:
        return print('A palavra é um palindromo')
    else:
        return print('A palavra não é um palindromo')
palavra = str(input('Digite uma palavra para verificar se ela é um palindromo'))
is_palindrome(palavra)
