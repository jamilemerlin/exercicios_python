def ehprimo(y):
    contador = 2
    if y == 1:
        return False
    elif y == 2:
        return True
    while contador < y:
        if y % contador == 0:
            return False
        contador += 1
    return True


def n_primos(x):
    inicial = x
    result = 0
    while inicial >= 1:
        if ehprimo(inicial):
            result += 1
        inicial -= 1
    return result


a = int(input("Digite um número: "))
resultado = n_primos(a)
print(resultado)
