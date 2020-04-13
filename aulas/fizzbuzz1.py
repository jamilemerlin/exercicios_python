numero = int(input("Digite um número:"))

resultado = (numero % 3 == 0) and (numero % 5 == 0)

if resultado == 0:
    print(numero)

else:
    print("FizzBuzz")
