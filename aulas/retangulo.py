largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
linha = 0
while linha < altura:
    contador = 1
    while contador <= largura:
        print("#", end="")
        contador += 1
    linha += 1
    print()
