valorlista = []
for contador in range(0, 5):
    valorlista.append(int(input(f'Digite um número para a posição {contador}: ')))
print(f'Os números digitados são: {valorlista}')
ordenada = valorlista[:]
ordenada.sort()
menor = ordenada[0]
maior = ordenada[-1]
print(f'O menor número foi {menor} e está na posição ', end='')
for indice, valor in enumerate(valorlista):
    if valor == menor:
        print(f'{indice}...', end='')
print()
print(f'O maior número foi {maior} e está na posição ', end='')
for indice, valor in enumerate(valorlista):
    if valor == maior:
        print(f'{indice}...', end='')
print()
