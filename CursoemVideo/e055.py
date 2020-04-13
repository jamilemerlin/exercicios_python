maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o {c}ª peso: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso
print(f'O menor peso é: {menor:.1f}kg e o maior peso é {maior:.1f}kg')
