first = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = first +(10 - 1) * razao
cont = []
for c in range(first, decimo + razao, razao):
    # cont.append(c)
    print(f'{c}', end=' -> ')
print('ACABOU')