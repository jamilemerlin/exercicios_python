def leiaInt(mensagem):
    valido = False
    inteiro = 0
    while True:
        entrada = str(input(mensagem))
        if entrada.isnumeric():
            inteiro = int(entrada)
            valido = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if valido:
            break
    return inteiro


entrada = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {entrada}.')
