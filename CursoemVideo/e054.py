from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    anonascimento = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    anoatual = date.today().year
    idade = anoatual - anonascimento
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print(f'{maior} pessoas são maior de idade.')
print(f'{menor} pessoas são menor de idade.')
