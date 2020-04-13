numero = int(input('Digite um número entra 0 e 9999: '))
uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10
print(f'Unidade {uni}'
      f'\nDezena {dez:>2}'
      f'\nCentena {cen}'
      f'\nMilhar {mil:>2}')