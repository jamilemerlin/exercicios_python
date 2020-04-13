'''ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    if ano % 100 == 0 and ano % 400 != 0:
        print(f'{ano} não é bissexto!')
    else:
        print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto!')'''
# a solucção a cima é minha.

# a solução a baixo é do professor.
from datetime import date

ano = int(input('Digite um ano ou zero para o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{ano} é bissexto!')
else:
    print(f'{ano} não é bissexto!')
