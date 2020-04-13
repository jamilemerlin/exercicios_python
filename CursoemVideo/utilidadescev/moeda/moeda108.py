def aumentar(valor=0, aumento=0):
    porcentagem = valor + ((aumento * valor) / 100)
    return porcentagem


def diminuir(valor=0, reducao=0):
    porcentagem = valor - ((reducao * valor) / 100)
    return porcentagem


def dobro(valor=0):
    dobro = valor * 2
    return dobro


def metade(valor=0):
    divisao = valor / 2
    return divisao

def real(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
