lista = []
while True:
    entrada = int(input('Digite um número: '))
    lista.append(entrada)
    continua = str(input('Deseja continuar? [S/N] -> ')).upper().strip()
    if continua == 'N':
        break
if 5 in lista:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
print(f'Foram digitados {len(lista)} números')
lista.sort(reverse=True)
print(f'A lista decrescente é: {lista}')
