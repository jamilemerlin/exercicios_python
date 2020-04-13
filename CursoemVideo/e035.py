reta1 = float(input('Digite a medida da primeira reta: '))
reta2 = float(input('Digite a medida da segunda reta: '))
reta3 = float(input('Digite a medida da terceira reta: '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('As medidas aplicadas podem formar um triângulo!')
else:
    print('Não podem formar um triângulo!')