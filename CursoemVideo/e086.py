matriz = [[], [], []]
for altura in range(0, 3):
    for largura in range(0, 3):
        matriz[altura].append(int(input(f'Digite um valor para a posição [{altura}, {largura}]: ')))
for altura in range(0, 3):
    for largura in range(0, 3):
        print(f'[{matriz[altura][largura]:^5}]', end='')
    print()
