def sed(str_sub, str_p, original, destino):
    original = open(original, 'r', encoding="UTF-8")
    final = open(destino, 'w', encoding= "UTF-8")
    for line in original:
        line = line.replace(str_p, str_sub)
        final.write(line)
    print(final)

    original.close()
    final.close()
    return final

original = 'livro_guttenberg.txt'
destino = 'arquivo_exercicios.txt'
str_sub = 'casa'
str_p = 'hoje'
arquivo_final = sed(str_sub, str_p, original, destino)


