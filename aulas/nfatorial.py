entrada = int(input("Digite o valor de n: "))
contador = entrada
fator = 1

while contador > 0:
    fator = fator * contador
    contador = contador - 1
print(fator)
