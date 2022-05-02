import string
def ler_arquivo(nome_arquivo):
    palavras = dict()
    arquivo = open(nome_arquivo, encoding="utf8")
    for line in arquivo:
        processar_linhas(line, palavras)
    return palavras

def processar_linhas(line, palavras):
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        palavras[word] = palavras.get(word, 0) + 1
def total_palavras(hist):
    return sum(hist.values())
def palavras_diferentes(hist):
    return len(hist)
def palavras_comuns(hist):
    t = []
    for key, value in hist.items():
        t.append((value, key)) 
    t.sort(reverse=True)
    return t
hist = ler_arquivo('livro_guttenberg.txt')
print(hist)
print("Total de palavras do livro: {}".format(total_palavras(hist)))
print("Numero de diferentes palavras: {}".format(palavras_diferentes(hist)))
print(hist)
t = palavras_comuns(hist)
print("As 20 palavras mais comuns ")
for freq, palavra in t[:20]:
    print(palavra, freq, sep='\t')


