def eh_hipotenusa(hi):
    ca = 1
    while ca <= hi:
        co = 1
        while co <= hi:
            if (hi * hi) == (ca * ca) + (co * co):
                return hi
            co += 1
        ca += 1
    return 0


def soma_hipotenusas(n):
    hi = 1
    soma = 0
    while hi <= n:
        soma += eh_hipotenusa(hi)
        hi += 1
    return soma


comeca = int(input("Digite um número inteiro: "))
print(soma_hipotenusas(comeca))

