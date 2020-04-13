nome = str(input('Digite seu nome completo: ')).strip()
letrasmaiusculas = nome.upper()
letrasminusculas = nome.lower()
separacao = nome.split()
juncao = ''.join(nome)
totalletras = len(juncao)
totalprimeionome = len(separacao[0])
print(f'Seu nome em letras maiúsculas é: {letrasmaiusculas}'
      f'\nSeu nome em letras minúsculas é: {letrasminusculas}'
      f'\nSeu nome tem: {totalletras} letras'
      f'\nSeu primeiro nome tem: {totalprimeionome} letras')
