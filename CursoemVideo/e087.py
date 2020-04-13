matriz = [[], [], []]
totalcoluna = totalpares = 0
maior = 0
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um número para a posição [{linha}, {coluna}]: ')))
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            totalpares += matriz[linha][coluna]
    print()
print(f'A soma dos valores pares é {totalpares}')
for linha in range(0, 3):
    totalcoluna += matriz[linha][2]
print(f'A soma dos valores da terceira coluna é {totalcoluna}')
for coluna in range(0, 3):
    if matriz[1][coluna] > maior:
        maior = matriz[1][coluna]
print(f'O maior valor da segunda linha é {maior}')
