numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite mais um número: '))
if numero1 == numero2:
    print(f'Os número digitados foram {numero1} e {numero2} e eles são IGUAIS.')
elif numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}.')
else:
    print(f'O número {numero2} é maior que o número {numero1}.')
