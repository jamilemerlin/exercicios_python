dados = dict()
dados['Nome'] = str(input('Qual o nome do aluno? '))
dados['Média'] = float(input('Qual a média do aluno? '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
else:
    dados['Situação'] = 'Reprovado'
print(f'O aluno {dados["Nome"]} teve média {dados["Média"]} e está {dados["Situação"]}')
for k, v in dados.items():
    print(f'{k} é igual a {v}.')
