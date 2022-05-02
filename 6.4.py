def veri_power(a,b):
    resto = a % b
    div = a / b
    if resto == 0:
        resto = div % b
        if resto == 0:
            return True
        else:
            return False
    else:
        return False
a = int(input('Digite um numero Inteiro como valor de a: '))
b = int(input('Digite um numero Inteiro como valor de b: '))
print(veri_power(a,b))
