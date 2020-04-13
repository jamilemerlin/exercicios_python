from math import factorial
numero = int(input('Digite um número inteiro para saber seu fatorial: '))
contador = 1
total = 1
while contador <= numero:
    total = total * contador
    contador += 1
print(f'O {numero}! é {total}')

'''numero = int(input('Digite um número inteiro para saber seu fatorial: '))
fatorial = factorial(numero)
print(f' O fatorial de {numero} é {fatorial}')'''

'''numero = int(input('Digite um número inteiro para saber seu fatorial: '))
multi = 1
for c in range(1, numero + 1):
    multi = multi * c
print(f'O fatorial de {numero} é {multi}')'''