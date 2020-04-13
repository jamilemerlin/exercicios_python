first = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = first
contador = 1
while contador <= 10:
    print(f'{termo}', end=' -> ')
    contador += 1
    termo += razao
print('ACABOU')