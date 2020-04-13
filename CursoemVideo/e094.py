dados_pessoas = dict()
pessoas_cadastradas = list()
soma_idades = 0
while True:
    dados_pessoas.clear()
    dados_pessoas['nome'] = str(input('Nome: '))
    while True:
        dados_pessoas['sexo'] = str(input('Sexo: [F/M] ')).upper()
        if dados_pessoas['sexo'] in 'FM':
            break
        print('Erro! Por favor digite apenas S ou N.')
    dados_pessoas['idade'] = int(input('Idade: '))
    soma_idades += dados_pessoas['idade']
    pessoas_cadastradas.append(dados_pessoas.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('Erro! Por favor digite apenas S ou N.')
    if continuar == 'N':
        break
print('- *' * 15)
print(f'A - Ao todo cadastramos {len(pessoas_cadastradas)} pessoas.')
media_idades = soma_idades / len(pessoas_cadastradas)
print(f'B - A média das idades cadastradas é {media_idades:.2f} anos.')
print('C - As mulheres cadastradas foram: ', end='')
for pessoa in pessoas_cadastradas:
    if pessoa['sexo'] == 'F':
        print(f'{pessoa["nome"] }', end=' ')
print()
print('D - As pessoas com idade acima da média são: ', end='')
for pessoa in pessoas_cadastradas:
    if pessoa['idade'] >= media_idades:
        print(f'{pessoa["nome"]}', end=' ')




