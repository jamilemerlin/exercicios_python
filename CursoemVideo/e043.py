peso = float(input('Insira seu peso em quilogramas: '))
altura = float(input('Insira sua altura em metros: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f} e é considerado abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.2f} e é considerado ideal.')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.2f} e é considerado sobrepeso.')
elif imc >= 30 and imc < 40:
    print(f'Seu IMC é de {imc:.2f} e é considerado obesidade.')
else:
    print(f'Seu IMC é de {imc:.2f} e é considerado obesidade mórbida.')
