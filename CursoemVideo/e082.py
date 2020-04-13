lista = []
while True:
    entrada = int(input('Digite um número: '))
    lista.append(entrada)
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
lista2 = []
lista3 = []
for num in lista:
    if num % 2 == 0:
        lista2.append(num)
    else:
        lista3.append(num)
print(f'1ª Lista: {lista}')
print(f'2ª Lista com pares: {lista2}')
print(f'3ª Lista com impares: {lista3}')
