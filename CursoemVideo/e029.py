velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    print('Você ultrapassou a velocidade permitida e isso gerou uma multa!')
    multa = (velocidade - 80) * 7
    print(f'Sua multa é de R${multa:.2f}!')
print('Tenha um bom dia, dirija com segurança!')
