def maior_elemento(entrada):
    for numero in range(len(entrada)):
        f = list(set(entrada))
        fim = sorted(f)
    return fim[-1]


lista = []
l = 1
while l > 0:
    l = int(input("Digite um número: "))
    if l == 0:
        break
    lista.append(l)
print(maior_elemento(lista))

