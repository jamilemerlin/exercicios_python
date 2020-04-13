entrada = float(input('Digite o valor do produto: '))
desconto = (5 * entrada) / 100
novovalor = entrada - desconto
print(f'Este produto com 5% de desconto fica {novovalor:.2f} reais')