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
