entrada = 0
lista = []
while True:
    entrada = int(input('Digite um número inteiro: '))
    continuar = str(input('Deseja continuar? [S/N] -> ')).lower().strip()
    if entrada not in lista:
        lista.append(entrada)
    if continuar == 'n':
        break
lista.sort()
print(f'Os valores digitados foram:'
      f'\n{lista}')
