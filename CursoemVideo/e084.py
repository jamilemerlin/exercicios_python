total = []
temptotal = []
maior = menor = 0
while True:
    temptotal.append(str(input('Seu nome: ')))
    temptotal.append(float(input('Seu peso: ')))
    if len(total) == 0:
        maior = menor = temptotal[1]
    else:
        if temptotal[1] < menor:
            menor = temptotal[1]
        if temptotal[1] > maior:
            maior = temptotal[1]
    total.append(temptotal[:])
    temptotal.clear()
    continuar = str(input('Deseja continuar? [S/N] --> ')).upper().strip()
    if continuar == 'N':
        break
print(f'Foram cadastradas {len(total)} pessoas.')
print(f'As pessoas mais pesadas são: ', end='')
for p in total:
    if p[1] == maior:
        print(f'{p[0]}, ', end='')
print()
print(f'As pessoas mais leves são: ', end='')
for p in total:
    if p[1] == menor:
        print(f'{p[0]}, ', end='')
print()
