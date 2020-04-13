from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
escolha = 0
while escolha != 5:
    escolha = int(input('     MENU'
                        '\n     [1] somar'
                        '\n     [2] multiplicar'
                        '\n     [3] maior'
                        '\n     [4] novos números'
                        '\n     [5] sair do programa'
                        '\n >>>> Escolha : '))
    if escolha == 1:
        total = valor1 + valor2
        print(f'A soma: {valor1} + {valor2} é igual a {total}.')
        print('=-*-'*10
        sleep(2)
    elif escolha == 2:
        total = valor1 * valor2
        print(f'A multiplicação: {valor1} X {valor2} é igual a {total}.')
        print('=-*-' * 10)
        sleep(2)
    elif escolha == 3:
        if valor1 > valor2:
            print(f'{valor1} é maior que {valor2}.')
            print('=-*-' * 10)
            sleep(2)
        elif valor1 == valor2:
            print(f'{valor1} é igual a {valor2}')
            print('=-*-' * 10)
            sleep(2)
        else:
            print(f'{valor2} é maior que {valor1}.')
            print('=-*-' * 10)
            sleep(2)
    elif escolha == 4:
        print('Informe novos números: ')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif escolha == 5:
        print('=-*-' * 10)
        print('Saindo da aplicação.')
    else:
        print('Opção inválida, tente novamente!')
        print('=-*-' * 10)
print('fim')