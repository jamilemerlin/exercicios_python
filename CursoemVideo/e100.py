from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for contador in range(0, 5):
        valor = randint(1, 10)
        lista.append(valor)
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)


def somarpar(lista):
    soma = 0
    for valor in lista:
        resto = valor % 2
        if resto == 0:
            soma += valor
    print(f'A soma dos números pares da lista {lista} é: {soma}')


numeros = list()
sorteia(numeros)
print('')
somarpar(numeros)
