n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisaointeira = n1 // n2
esponenciacao = n1 ** n2
print('A soma é{}, o produto é {}, e a divisão é {:.3f}'.format(soma, multiplicacao, divisao))
print('Divisão inteira {} e potência {}'.format(divisaointeira, esponenciacao))