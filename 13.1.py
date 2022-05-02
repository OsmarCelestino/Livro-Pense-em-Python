import string
arquivo =  open("arquivo_exercicios.txt", "r", encoding="UTF-8")
texto = arquivo.read()
texto = texto.replace(" ", "")
texto = texto.upper()
texto = texto.translate(str.maketrans('', '', string.punctuation))
print(texto)