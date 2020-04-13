soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
print(f'A soma de todos os números ímpares multiplos de 3 entre 1 e 500 é: {soma}')
