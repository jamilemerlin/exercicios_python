from utilidadescev.moeda import moeda108

entrada = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda108.real(entrada)} é {moeda108.real(moeda108.metade(entrada))}')
print(f'O dobro de {moeda108.real(entrada)} é {moeda108.real(moeda108.dobro(entrada))}')
print(f'Aumentando 10%, temos {moeda108.real(moeda108.aumentar(entrada, 10))}')
print(f'Reduzindo 13%, temos {moeda108.real(moeda108.diminuir(entrada, 13))}')
