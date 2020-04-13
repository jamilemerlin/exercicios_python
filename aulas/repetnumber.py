n = int(input("Digite um número: "))
x0 = 0
resto = n % 10
n = n // 10
while n > 0 and != x0:
    resto2 = n % 10
    n = n // 10
    if resto == resto2:
        x0 = 1
        resto = resto2
        n = n // 10
if x0:
    print("sim")
else:
    print("não")
