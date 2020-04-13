def soma_elementos(li):
    soma = 0
    for numero in range(len(li)):
        soma += li[numero]
    return soma


lista = []
l = 1
while l > 0:
    l = int(input("digite a lista de números inteiros:"))
    if l == 0:
        break
    lista.append(l)
print(soma_elementos(lista))
