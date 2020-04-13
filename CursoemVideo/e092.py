#calculo aposentadoria
from datetime import date
calulo_aposentadoria = dict()
calulo_aposentadoria['nome'] = str(input('Digite seu nome: '))
ano_nascimento = int(input('Digite seu ano de nascimento: '))
ano_hoje = date.today().year
idade = ano_hoje - ano_nascimento
calulo_aposentadoria['idade'] = idade
ctps = int(input('Digite o número da sua CTPS: '))
if ctps != 0:
    calulo_aposentadoria['ano_contratacao'] = int(input('Digite o ano da sua contratação: '))
    calulo_aposentadoria['salario'] = float(input('Digite seu salário: R$ '))
    calulo_aposentadoria['idade_aposentadoria'] = (idade - (ano_hoje - ano_contratacao)) + 35
if ctps == 0:
    calulo_aposentadoria['ctps'] = 0
print('-*' *15)
for key, value in calulo_aposentadoria.items():
    print(f' - {key} tem o dado {value}.')
