
print('\033[32;40m=-\033[m'*20)
print('\033[32;40m    SIMULAÇAO DE EMPRÉSTIMO BANCÁRIO    \033[m')
print('\033[32;40m=-\033[m'*20)
valorcasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você deseja quitar? '))
maxparcela = salario * 30 / 100
meses = anos * 12
valorparcela = valorcasa / meses
if valorparcela > maxparcela:
    print(f'Infelizmente, seu empréstimo não foi aprovado!'
          f'\nPois o valor da parcela é de R${valorparcela:.2f} e ultrapassa o limite da sua renda mensal!')
else:
    print(f'Seu empréstimo foi aprovado!'
          f'\nPara quitar o imóvel escolhido em {anos} anos,'
          f'\nvocê pagará {meses} parcelas de R${valorparcela:.2f}')
