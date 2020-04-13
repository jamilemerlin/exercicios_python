from time import sleep
def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if inicio < fim:
        p = inicio
        while p <= fim:
            print(f'{p}', end=' ', flush=True)
            p += passo
            sleep(0.3)
        print('Fim')
        print('')
    else:
        p = inicio
        while p >= fim:
            print(f'{p}', end=' ', flush=True)
            p -= passo
            sleep(0.3)
        print('Fim')
        print('')


inicio_a = 1
fim_a = 10
passo_a = 1
contador(inicio_a, fim_a, passo_a)

inicio_b = 10
fim_b = 0
passo_b = 2
contador(inicio_b, fim_b, passo_b)

print('-=' * 20)
inicio_c = int(input('Digite o início da contagem: '))
fim_c = int(input('Digite o fim da contagem: '))
passo_c = int(input('Digite o passo da contagem: '))
contador(inicio_c, fim_c, passo_c)
