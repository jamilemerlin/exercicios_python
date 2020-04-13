entrada = str(input('Digite seu sexo: [F/M] - ')).upper()
while entrada != 'F' and entrada != 'M':
    entrada = str(input('Dado inválido.Digite seu sexo: [F/M] - ')).upper()
print(f'Well done! Sexo {entrada} registrado!')
