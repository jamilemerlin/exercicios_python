def ehprimo(k):
    contador = 2
    if k == 1:
        return False
    while contador < k:
        if k % contador == 0:
            return False
        contador = contador + 1
    return True


def maior_primo(k):
    inicial = 0
    contador = 2
    while inicial <= k:
        if ehprimo(k):
            return k
        k = k - 1
