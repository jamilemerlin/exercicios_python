nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'\033[4;32;40m APROVADO \033[m'
          f'\ncom média {media}')
elif media < 5.0:
    print(f'\033[4;31;40m REPROVADO \033[m'
          f'\ncom média {media}')
else:
    print(f'\033[4;33;40m RECUPERAÇÃO \033[m'
          f'\ncom média {media}')
