entrada = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = entrada / 3.27
print(f'Com \033[4;32;40mR${entrada:.2f}\033[m você pode comprar \033[4;31;40mUS${dolar:.2f}\033[m dolares!')
