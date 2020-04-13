entrada = str(input('Digite uma expressão matemática com parêntesis: '))
if entrada.count(')') != entrada.count('('):
        print(f'A expressão {entrada} NÃO está formada da maneira correta.')
else:
    abre = []
    fecha = []
    for indice, valor in enumerate(entrada):
        if valor == '(':
            abre.append(indice)
        if valor == ')':
            fecha.append(indice)
    certo = True
    for indice in range(0, len(abre)):
        abrevalor = abre[indice]
        fechavalor = fecha[indice]
        if abrevalor > fechavalor:
            certo = False
            break
    if certo:
        print(f'A expressão {entrada} está formatada na ordem correta.')
    else:
        print(f'A expressão {entrada} NÃO está formada da maneira correta.')
