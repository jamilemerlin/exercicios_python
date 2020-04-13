nome = str(input('Digite seu nome: ')).strip()
padrao = nome.title()
if 'Silva'in padrao:
    print(f'Existe o nome Silva em {padrao}')
else:
    print(f'Não existe o nome Silva em {padrao}')