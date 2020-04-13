from random import randint
from time import sleep
from operator import itemgetter # de um espaco vertical (uma linha em branco) entre os imports e o restante do codigo

#partida = list() # acho que voce nao precisa guardar a partida pq soh vai existir uma partida por execucao do programa
jogadores = dict() # coloca o nome da variavel no plural para lembrar que pode ter mais que 1 jogador nessa variavel

print('   JOGO DE DADOS')
print('-*' *12)

for c in range(1, 5): # recomendo usar a letra "j" para lembrar que eh o numero do jogador
    chave = 'Jogador ' + str(c)
    jogadores[chave] = randint(1, 6) # aqui a chave 'Jogador' nunca muda. Ela deve ser 'Jogador1', 'Jogador2', ...
    print(f'O jogador {c} tirou {jogadores[chave]}') # aqui a chave tbm nao muda.
    sleep(0.7)
    #partida.append(jogador.copy()) # voce nao vai precisar disso pq cada os valores vao ser unicos em cada chave
    # partida = [ { 'Jogador': 4 }, { 'Jogador': 3 }, ... ]

print('-*' *12) # deixe uma linha em branco quando mudar de identacao
print(' Ranking dos jogadores:')

partidaOrdenada = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

for k, v in enumerate(partidaOrdenada):
    print(f'{k + 1}ª lugar: {v[0]} com {v[1]}')
    sleep(0.5)
