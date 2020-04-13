from random import randint
escolha = randint(0, 10)
usuario = -1
tentativa = 0
print('Vou pensar em um número, tente adivinhar qual é esse número!')
usuario = int(input('Qual seu chute? '))
while usuario != escolha:
    if usuario < escolha:
        print('Mais...Tente de novo! ')
    elif usuario > escolha:
        print('Menos... Tente de novo! ')
    usuario = int(input('Qual seu chute? '))
    tentativa += 1
if usuario == escolha:
    print(f'Parabéns! Você acertou o computador escolheu o número {usuario} e você precisou de {tentativa +1} tentativas!!!')
