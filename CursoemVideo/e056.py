media = 0
maioridadem = 0
nomevelho = ''
totalmulheres = 0
for pessoa in range(1, 5):
    print(f'-------{pessoa}ª PESSOA -------')
    nome = str(input('Digite seu nome: '))
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo: [F/M]')).strip().upper()
    media += idade
    if pessoa == 1 and sexo == 'M':
        maioridadem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadem:
        maioridadem = idade
        nomevelho = nome
    if sexo == 'F' and idade <= 20:
        totalmulheres += 1
print(f'A idade média desse grupo é de: {media / 4:.1f} anos!')
print(f'O mais velho é: {nomevelho} ele tem {maioridadem}')
print(f'{totalmulheres} mulheres tem menos de 20 anos.')
