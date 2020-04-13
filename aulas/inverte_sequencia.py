entrada = 1
l = []
while entrada > 0:
    entrada = int(input("Digite um número: "))
    if entrada != 0:
        l.append(entrada)
    else:
        break
for numero in reversed(l):
    print(numero)

