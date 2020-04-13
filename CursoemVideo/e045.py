from random import choice
from time import sleep
print('\033[7;30mVAMOS JOGAR JOKENPO?\033[m')
escolha = int(input('Digite 1 para SIM'
                    '\nDigite 2 para NÃO'
                    '\n-> '))
if escolha == 1:
    jogador = str(input('Qual é a sua jogada? '))
    print('Vou pensar na minha jogada...')
    sleep(1)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    pc = choice(['pedra', 'papel', 'tesoura'])
    print('-='*15)
    print(f'Eu escolhi {pc}')
    print(f'Você escolheu {jogador}')
    print('-='*15)
    if pc == jogador:
        print(f'\033[34;40mEstamos empatados!\033[m')

    elif pc == 'tesoura' and jogador == 'papel':
        print(f'\033[36;40mEu ganhei!\033[m')

    elif jogador == 'tesoura' and pc == 'pedra':
        print(f'\033[36;40mEu ganhei!\033[m')

    elif jogador == 'pedra' and pc == 'papel':
        print(f'\033[36;40mEu ganhei!\033[m')

    elif pc == 'tesoura' and jogador == 'pedra':
        print(f'\033[31;40mParabéns você ganhou!\033[m')

    elif jogador == 'tesoura' and pc == 'papel':
        print(f'\033[31;40mParabéns você ganhou!\033[m')

    elif jogador == 'papel' and pc == 'pedra':
        print(f'\033[31;40mParabéns você ganhou!\033[m')
else:
    print('Que pena, quem sabe jogamos na próxima!')
