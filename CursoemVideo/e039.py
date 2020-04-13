from datetime import date
anonascimento = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year
calc = ano - anonascimento
if calc > 18:
    passou = calc - 18
    print(f'O tempo para alistamento já passou fazem {passou} anos!')
elif calc == 18:
    print(f'Você completou {calc}! Está na hora de fazer o alistamento!')
else:
    falta = 18 - calc
    print(f'Ainda faltam {falta} anos para você poder fazer o alistamento!')
