produto = float(input('Digite o valor do produto: R$ '))
condicaodepagamento = int(input('Modo de pagamento:'
                                '\n1 - à vista (dinheiro ou cheque)'
                                '\n2 - à vista (cartão)'
                                '\n3 - parcelado (máximo 2x)'
                                '\n4 - parcelado (3x ou mais)'
                                '\nDigite a opção de pagamento:'))
if condicaodepagamento == 1:
    desconto = produto - (produto * 10 / 100)
    print(f'Nesta modalidade de pagamento há um desconto de 10% o valor a ser pago é de R${desconto:.2f}')
elif condicaodepagamento == 2:
    desconto = produto - (produto * 5 / 100)
    print(f'Nesta modalidade de pagamento há um desconto de 5% o valor a ser pago é de R${desconto:.2f}')
elif condicaodepagamento == 3:
    print(f'Nesta modalidade de pagamento não há desconto o valor a ser pago é de R${produto:.2f}')
else:
    desconto = produto + (produto * 20 / 100)
    print(f'Nesta modalidade de pagamento há um acréscimo de 20% o valor a ser pago é de R${desconto:.2f}')