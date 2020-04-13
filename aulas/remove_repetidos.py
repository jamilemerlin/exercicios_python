def remove_repetidos(lista):
    for numero in range(len(lista)):
        f = list(set(lista))
        fim = sorted(f)
    return fim


li = []
l = 1
while l > 0:
    l = int(input("Digite um número: "))
    if l == 0:
        break
    li.append(l)
print(remove_repetidos(li))
