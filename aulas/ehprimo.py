entrada = int(input("Digite um número inteiro: "))
contador = 2

while contador < entrada:
    if (entrada % contador) == 0:
        print("não primo")
        exit()
    contador = contador + 1

print("primo")
