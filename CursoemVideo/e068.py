from random import randint
print('=-*'* 10)
print('JOGO DO PAR OU IMPAR')
print('=-*'* 10)
vence = 0
while True:
    jogada = str(input('Escolha PAR [P] OU IMPAR [I]: ')).upper().strip()
    jogador = int(input('Escolha um número: '))
    pc = randint(0, 10)
    parimpar = (jogador + pc) / 2
    print(f'Você jogou {jogador} e o computador jogou {pc}.')
    print('Deu par' if parimpar % 2 == 0 else 'Deu impar')
    if parimpar % 2 == 0:
        if jogada == 'P':
            print('Você venceu!'
                  '\nVamos jogar novamente...')
            vence += 1
        else:
            print('Você perdeu!')
            break
    else:
        if jogada == 'I':
            print('Você venceu!'
                  '\nVamos jogar novamente...')
            vence += 1
        else:
            print('Você perdeu!')
            break
print(f'Você ganhou {vence} vezes!')
