totalgasto = 0
produtomaisbarato = 0
maisbarato = ''
maiscaro = 0
totalprodutos = 0
while True:
    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Preço: R$ '))
    totalprodutos += 1
    totalgasto += preco
    if preco > 1000:
        maiscaro += 1
    if totalprodutos == 1:
        maisbarato = nome
        produtomaisbarato = preco
    elif preco < produtomaisbarato:
        maisbarato = nome
        produtomaisbarato = preco
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'O total dos gastos foi: R${totalgasto:.2f}.')
print(f'{maiscaro} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi {maisbarato}.')
