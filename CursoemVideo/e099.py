from time import sleep
def maior(*numeros):
    print('Analisando os valores passados...')
    contagem = maior = 0
    for valor in numeros:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.2)
        if contagem == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contagem += 1
    print(f'Foram informados {contagem} valores ao todo.')
    print(f'O maior número é: {maior}')
    print('-=' * 20)


maior(2, 5, 7, 3, 9)
maior(6, 9, 55, 22, 30)
maior(1, 2)
maior(0)
maior(6)
maior()