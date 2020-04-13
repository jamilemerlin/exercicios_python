import math

a = int(input("Informe A: "))
b = int(input("Informe B: "))
c = int(input("Informe C: "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)

    if x1 == x2:
        print("a raiz desta equação é", x1)

    if x1 < x2:
        print("as raízes da equação são", x1, "e", x2)

    if x1 > x2:
        print("as raízes da equação são", x2, "e", x1)
