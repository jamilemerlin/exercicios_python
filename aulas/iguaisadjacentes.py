numeroinicial = int(input("Digite um número: "))
numero = 0
inicial = numeroinicial
digito = int(input("Digite o número a ser pesquisado: "))
while numeroinicial > 0:
    resto = numeroinicial % 10
    dividendo = numeroinicial // 10
    numeroinicial = dividendo
    if digito == resto:
        numero = numero + 1

if numero == 1:
    print(numeroinicial, "nao tem digitos iguais adjacentes")
else:
    print(numeroinicial, "tem dois digitos", digito, "adjacentes)
