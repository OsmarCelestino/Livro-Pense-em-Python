print('Teorema de Fernat')
def check_fernat(a,b,c,n):
    a = a ** n
    b = b ** n
    c = c ** n
    soma = a + b
    if soma == c:
     return print('Holy smokes, Fernat was wrong!')
    else:
        return print('No that dosen´t work' )

a = float(input('Digite um valor  pra a'))
b = float(input('Digite um valor pra b'))
c = float(input('Digite um valor pra c'))
n = float(input('Digite um valor pra n'))
while n < 2:
    print('N tem que ser maior que 2')
    a = float(input('Digite um valor  pra a'))
    b = float(input('Digite um valor pra b'))
    c = float(input('Digite um valor pra c'))
    n = float(input('Digite um valor pra n'))
resultado = check_fernat(a,b,c,n)