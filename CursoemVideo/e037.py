numero = int(input('Digite um número inteiro: '))
base = int(input('Qual será a base de conversão?'
                 '\n1 para binário'
                 '\n2 para octal'
                 '\n3 para hexadecimal'
                 '\nDigite o número escolhido: '))
if base == 1:
    binario = bin(numero)
    print(f'O binário do número {numero} é: {binario[2:]}')
elif base == 2:
    octal = oct(numero)
    print(f'O octal do número {numero} é: {octal[2:]}')
elif base == 3:
    hexadecimal = hex(numero)
    print(f'O hexadecimal do número {numero} é: {hexadecimal[2:]}')
else:
    print('Essa opção não é válida!')

