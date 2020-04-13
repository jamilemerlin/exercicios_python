entrada = float(input('Digite o valor do salário: R$ '))
aumento = (15 * entrada) / 100
novosalario = entrada + aumento
print(f'O salário R${entrada:.2f} com o aumento de 15% passará a ser R${novosalario:.2f}')