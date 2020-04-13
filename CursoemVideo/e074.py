from random import randint
numero = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
ordenado = sorted(numero)
print(f'os números sorteados foram: {numero}')
print(f'{ordenado[0]} é o menor número.')
print(f'{ordenado[-1]} é o maior número.')
