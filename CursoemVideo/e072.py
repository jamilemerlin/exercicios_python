while True:
    numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
              'onze', 'doze', 'treze', 'quatorze', 'quinze',
              'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    entrada = int(input('Digite um número entre 0 e 20 para ser lido por extenso: '))
    if entrada < 0 or entrada > 20:
        entrada = print('Número inválido. ', end= '')
    else:
        print(numero[entrada])
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        print('Saindo da aplicação.')
        break
