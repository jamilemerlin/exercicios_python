entrada = float(input('Digite a quantidade de metros: '))
centimetros = entrada * 100
milimetros = entrada * 1000
print(f'{entrada} metros equivalem a:\n\033[4;31;40m{centimetros} centímetros\033[m \n\033[4;33;40m{milimetros} milímetros!\033[m')
