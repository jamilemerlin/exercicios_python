jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
numero_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
partidas = list()
for partida in range(0, numero_de_partidas):
    partidas.append(int(input(f'Quantos gols na partida {partida}? ')))
    jogador['gols'] = partidas[:]
jogador['total_de_gols'] = sum(partidas)
print('* -'*15)
print(jogador)
print('* -'*15)
for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}.')
print('* -'*15)
print(f'O jogador {jogador["nome"]} jogou {numero_de_partidas}.')
for item, value in enumerate(jogador['gols']):
    print(f' -> Na partida {item} ele fez {value} gols.')
print(f'Fez no total {jogador["total_de_gols"]} gols.')

