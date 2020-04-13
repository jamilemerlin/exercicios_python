def aumentar(valor=0, aumento=0, formatar=False):
    porcentagem = valor + ((aumento * valor) / 100)
    if formatar == False:
        return porcentagem
    else:
        return real(porcentagem)



def diminuir(valor=0, reducao=0, formatar=False):
    porcentagem = valor - ((reducao * valor) / 100)
    if formatar == False:
        return porcentagem
    else:
        return real(porcentagem)


def dobro(valor=0, formatar=False):
    dobro = valor * 2
    if formatar == False:
        return dobro
    else:
        return real(dobro)


def metade(valor=0, formatar = False):
    divisao = valor / 2
    if formatar == False:
        return divisao
    else:
        return real(divisao)

def real(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(valor=0, aumento=0, reducao=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: {real(valor):>13}') # poderia usar tabulação \t para alinhar o valor
    print(f'Metade do preço: {metade(valor, True):>13}')
    print(f'Dobro do preço: {dobro(valor, True):>14}')
    print(f'{aumento}% de aumento: {aumentar(valor, aumento, True):>14}')
    print(f'{reducao}% de redução: {diminuir(valor, reducao, True):>14}')
    print('-' * 30)
