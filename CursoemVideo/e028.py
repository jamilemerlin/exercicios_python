from random import randint
escolha = randint(0, 5)
usuario = int(input('Qual número entra 0 e 5 o computador escolheu? '))
if usuario == escolha:
    print(f'Parabéns! Você acertou o computador escolheu o número {usuario}!!!')
else:
    print(f'Não foi dessa vez... O computador escolheu {escolha}')
