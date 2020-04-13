def fatorialfuncao(entrada):
    contador = entrada
    fator = 1
    while contador > 0:
        fator = fator * contador
        contador = contador - 1
    return fator
