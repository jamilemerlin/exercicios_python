def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome = str(input('Nome do jogador: '))
gol = str(input('Quantidade de gols: '))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nome.strip() == '':
    ficha(gols=gol)
else:
    ficha(nome, gol)
