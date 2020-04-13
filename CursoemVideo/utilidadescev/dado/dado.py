def leiadinheiro(valor):
    valido = False
    while not valido:
        entrada = input(valor)
        entrada = str(entrada)
        entrada = entrada.replace(',', '.').strip()
        if entrada.isalpha():
            print('\033[0;31mERRO! Digite um número válido.\033[m')
            valido = True
            entrada = float(entrada)
        else:
            valido = True
            entrada = float(entrada)
        if valido:
            return entrada


def leiaInt(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar esse valor.')
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            return entrada


def leiafloat(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar esse valor.')
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        else:
            return entrada