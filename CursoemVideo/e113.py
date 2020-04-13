def leiaInt(mensagem):
    while True:
        try:
            entrada = int(input(mensagem))
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar esse valor.')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        else:
            return entrada


def leiafloat(mensagem):
    while True:
        try:
            entrada = float(input(mensagem))
        except (KeyboardInterrupt):
            print('O usuário preferiu não informar esse valor.')
            return 0
        except:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        else:
            return entrada


inteiro = leiaInt('Digite um número inteiro: ')
real = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')
