largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
linha = 1
while linha <= altura:
    if linha == 1 or linha == altura:
        borda = True
    else:
        borda = False
    contador = 1
    while contador <= largura:
        if borda:
            print("#", end="")
        elif contador == 1 or contador == largura:
            print("#", end="")
        else:
            print(" ", end="")
        contador += 1
    linha += 1
    print()
