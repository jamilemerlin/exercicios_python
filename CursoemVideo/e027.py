nome = str(input('Digite seu nome: ')).strip().title()
divide = nome.split()
print(f'O primeiro nome de {nome} é: {divide[0]}'
      f'\ne último nome é: {divide[-1]}')
