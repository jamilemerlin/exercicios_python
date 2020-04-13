jogador = dict()
resultado_time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    numero_de_partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas = list()
    for partida in range(0, numero_de_partidas):
        partidas.append(int(input(f'Quantos gols na partida {partida}? ')))
    jogador['gols'] = partidas[:]
    jogador['total_de_gols'] = sum(partidas)
    resultado_time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar? [S/N] ')).upper()
        if continuar in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if continuar == 'N':
        break
print('-' * 50)
print('cod', end='  ')
for item in jogador.keys():
    print(f'{item:<15}', end='')
print()
for key, value in enumerate(resultado_time):
    print(f'{key: >3}', end='  ')
    for dado in value.values():
        print(f'{str(dado):<15}', end='')
    print()
print('-' * 50)
while True:
    mostrar_dados = int(input('Quer mostrar os dados de qual jogador? (999 p/ sair) '))
    if mostrar_dados == 999:
        break
    if mostrar_dados >= len(resultado_time):
        print(f'Erro! Não existe esse jogador com código {mostrar_dados}')
        print('-' * 50)
    else:
        print(f'  -- ANÁLISE DO JOGADOR {resultado_time[mostrar_dados]["nome"]}:')
    for item, value in enumerate(jogador['gols']):
        print(f' -> Na partida {item} ele fez {value} gols.')
    print(f'  Ele fez no total {jogador["total_de_gols"]} gols.')
print('-' * 50)
print('ENCERRADO: VOLTE SEMPRE!')
