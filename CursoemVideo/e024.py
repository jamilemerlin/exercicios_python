cidade = str(input('Digite o nome da sua cidade: ')).strip()
padrao = cidade.upper()
separacao = padrao.split()
revisao = 'SANTO' in separacao[0]
if revisao is True:
    print(f'Sim, a cidade {padrao} começa com SANTO')
else:
    print(f'Não, a cidade {padrao} não começa com SANTO')