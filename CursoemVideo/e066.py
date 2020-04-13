entrada = 0
soma = 0
quantidade = 0
while entrada != 999:
    entrada = int(input('Digite um número inteiro (999 para parar): '))
    if entrada == 999:
        break
    soma += entrada
    quantidade += 1
print(f'Você digitou {quantidade} números e a soma total é {soma}.')