entrada = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(entrada)))
print('É um número?', entrada.isnumeric())
print('É alfabético?', entrada.isalpha())
print('É alfanúmerico?', entrada.isalnum())
print('Está em maiúsculas?', entrada.isupper())
print('Está em minúsculas?', entrada.islower())
print('Está capitalizada?', entrada.iscapt())
print('Só tem espaços?', entrada.isspace())

# capitalizada é quando começa com maiúscula e termina com minúscula.
# existe vários comandos do mesmo seguimento.