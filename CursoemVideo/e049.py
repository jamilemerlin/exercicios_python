numero = int(input('Digite um número para ver sua tabuada: '))
print(f'A tabuáda de {numero} é:')
for c in range(1, 11):
    mult = numero * c
    print(f'{numero} X {c:>2} = {mult:>2}')