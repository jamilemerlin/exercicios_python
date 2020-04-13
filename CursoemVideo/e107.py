from utilidadescev.moeda import moeda

entrada = float(input('Digite o preço: R$ '))
print(f'A metade de R${entrada} é R${moeda.metade(entrada)}')
print(f'O dobro de R${entrada} é R${moeda.dobro(entrada)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(entrada, 10)}')
print(f'Reduzindo 13%, temos R${moeda.diminuir(entrada, 13)}')
