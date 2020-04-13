entrada = (int(input('Digite o primeiro número: ')),
           int(input('Digite o segundo número: ')),
           int(input('Digite o terceiro número: ')),
           int(input('Digite o quarto número: ')))
print(f'Você digitou os números: {entrada}')
print(f'O valor 9 apareceu {entrada.count(9)} vezes.')
if 3 in entrada:
    print(f'o valor 3 foi digitado a primeira vez na posição {entrada.index(3)+1}.')
else:
    print(f'O valor 3 não apareceu nenhuma vez.')
print('Os números pares digitados foram:', end='')
for n in entrada:
    if n % 2 == 0:
        print(n, end='')
