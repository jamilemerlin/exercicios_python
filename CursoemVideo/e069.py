homens = 0
mulheres = 0
maiordeidade = 0
while True:
    print('-' * 20)
    print('CADASTRE UMA PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = ''
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Sexo: [F/M] ')).upper().strip()
    if idade > 18:
        maiordeidade += 1
    if sexo == 'M':
        homens +=1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    usuario = ''
    while usuario != 'S' and usuario != 'N':
        print('-' * 20)
        usuario = str(input('Você deseja continuar?'
                        '\nSIM [S]'
                        '\nNÃO [N]')).upper().strip()
    if usuario == 'N':
        break
print(f'A - {maiordeidade} pessoas tem mais de 18 anos.')
print(f'B - {homens} homens foram cadastrados.')
print(f'C - {mulheres} mulheres tem menos de 20 anos.')
