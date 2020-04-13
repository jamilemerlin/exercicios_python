numeros = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}ª valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares foram: {numeros[0]}')
print(f'Os números impares foram: {numeros[1]}')
