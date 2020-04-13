first = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = first
contador = 1
total = 0
escolha = 10
while escolha != 0:
    total += escolha
    while contador <= total:
        print(f'{termo}', end=' -> ')
        contador += 1
        termo += razao
    print('PAUSA')
    escolha = int(input('Quantos termos a mais você que ver? '))
print(f'Ao total foram apresentados {total} números para essa PA.')