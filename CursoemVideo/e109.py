from utilidadescev.moeda import moeda109

entrada = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda109.real(entrada)} é {moeda109.metade(entrada, True)}')
print(f'O dobro de {moeda109.real(entrada)} é {moeda109.dobro(entrada, True)}')
print(f'Aumentando 10%, temos {moeda109.aumentar(entrada, 10, True)}')
print(f'Reduzindo 13%, temos {moeda109.diminuir(entrada, 13, True)}')
