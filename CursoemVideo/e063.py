print('Sequencia de Fibonacci')
print('=-*-'*10)
entrada = int(input('Quantos termos você quer ver: '))
inicio = 0
somador = 1
print(f'{inicio} -> {somador} -> ', end='')
contador = 3
while contador <= entrada:
    soma = inicio + somador
    print(f'{soma} -> ', end='')
    inicio = somador
    somador = soma
    contador += 1
print('Fim')

'''entrada = int(input('Digite um número inteiro: '))
contador = 0
somador = 1
for contador in range(0, entrada):
    print(f'{contador} ->', end='')
    soma = contador + somador
    somador = contador
    contador = soma'''