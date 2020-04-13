from math import hypot

entrada1 = float(input('Digite o comprimento do cateto oposto: '))
entrada2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(entrada1, entrada2)
print(f'A hipotenusa para os catetos {entrada1:.2f} e {entrada2:.2f} é {hipotenusa:.2f}')