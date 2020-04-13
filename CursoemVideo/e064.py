entrada = 0
contador = 0
soma = 0
while entrada != 999:
    entrada = int(input('Digite um número inteiro para somar: '))
    if entrada != 999:
        soma += entrada
        contador += 1
print(f'Foram digitados {contador} números e a soma desses números é {soma}')
