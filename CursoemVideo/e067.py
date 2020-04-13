contador = 1
while True:
    print('=-*-' * 11)
    entrada = int(input('Digite um número para saber sua tabuada: '))
    print('=-*-' * 11)
    if entrada < 0:
        break
    while contador <= 10:
        multi = entrada * contador
        print(f'{entrada} X {contador:>2} = {multi:>2}')
        contador += 1
    contador = 1
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')

# solução professor:
''' 
while True:
    n = int(input('Quer ver a tabada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:>2} = {n * c:>2}')
    print('-' * 30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')'''
