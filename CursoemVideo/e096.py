def area(largura, comprimento):
    areatotal = largura * comprimento
    print(f'A área de um terreno {largura}X{comprimento} é de {areatotal}m².')


print('    Controle de Terrenos')
print('-'*28)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
