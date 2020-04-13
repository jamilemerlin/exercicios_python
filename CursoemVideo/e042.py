reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    if reta1 == reta2 != reta3 or reta1 == reta3 != reta2 or reta2 == reta3 != reta1:
        print('Com essas medidas podemos formar um: TRINÂNGULO ISÓCELES!')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('Com essas medidas podemos formar um: TRINÂNGULO ESCALENO')
    elif reta1 == reta2 and reta1 == reta3 and reta2 == reta3:
        print(f'Com essas medidas podemos formar um: TRINÂNGULO EQUILÁTERO!')
else:
    print('Com essas medidas não é possível formar um triângulo!')