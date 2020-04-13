coluna = 1
linha = 1
while linha <= 10:
    while coluna <= 10:
        print(coluna * linha, end="\t")
        coluna = coluna + 1
    linha = linha + 1
    print()
    coluna = 1
