print('=' * 40)
print('{:^40}'.format('CAIXA ELETRÔNICO'))
print('=' * 40)
valorsacado = int(input('Qual valor você deseja sacar? R$ '))
while True:
    divisao = valorsacado // 50
    resto = valorsacado % 50
    if divisao != 0:
        print(f'Total de {divisao:.0f} cédulas de R$50,00')
    divisao1 = resto // 20
    resto1 = resto % 20
    if divisao1 != 0:
        print(f'Total de {divisao1:.0f} cédulas de R$20,00')
    divisao2 = resto1 // 10
    resto2 = resto1 % 10
    if divisao2 != 0:
        print(f'Total de {divisao2:.0f} cédulas de R$10,00')
    divisao3 = resto2 // 1
    resto3 = resto2 % 1
    if divisao3 != 0:
        print(f'Total de {divisao3:.0f} cédulas de R$1,00')
        break
print('=' * 40)
print('FIM DA OPERAÇÃO! Tenha um bom dia!')
