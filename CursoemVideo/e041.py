from datetime import date
print('\033[7;30m=\033[m'*50)
print('\033[7;30mCONFEDERAÇÃO NACIONAL DE NATAÇÃO\033[m'.center(60))
print('\033[7;30m=\033[m'*50)
ano = int(input('Qual o ano de nascimento do atleta? '))
atual = date.today().year
idade = atual - ano
if idade > 20:
    print(f'O atleta tem {idade} anos e está classificado como: MASTER!')
elif idade == 20:
    print(f'O atleta tem {idade} anos e está classificado como: SÊNIOR!')
elif idade > 14:
    print(f'O atleta tem {idade} anos e está classificado como: JUNIOR!')
elif idade > 9:
    print(f'O atleta tem {idade} anos e está classificado como: INFANTIL!')
else:
    print(f'O atleta tem {idade} anos e está classificado como: MIRIM!')