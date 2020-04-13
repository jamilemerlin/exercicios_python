entrada1 = int(input('POr quantos dias o carro foi alugado? '))
entrada2 = float(input('Quantos quilometros foram rodados? '))
# valordiaria = entrada1 * 60
# valorkm = entrada2 * 0.15
# total = valordiaria + valorkm
total = (entrada1 * 60) + (entrada2 * 0.15)
print(f'O tatal a pagar é de R${total:.2f}')