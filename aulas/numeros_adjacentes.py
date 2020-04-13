entrada = int(input("Digite um número inteiro: "))
total = 0
while entrada > 0:
    resto = entrada % 10
    dividendo = entrada // 10
    entrada = dividendo
    total = total + resto
print(total)
