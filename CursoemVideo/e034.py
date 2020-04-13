salario = float(input('Digite seu salário: R$'))
if salario > 1250.00:
    reajuste1 = (salario * 10 / 100) + salario
    print(f'Você terá um aumento de 10% e seu salário será: R${reajuste1:.2f}')
else:
    reajuste2 = (salario * 15 / 100) + salario
    print(f'Você terá um aumento de 15% e seu salário será: R${reajuste2:.2f}')