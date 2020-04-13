from random import randint
from time import sleep
print('-*-' *15)
print('              JOGO DA MEGA SENA')
print('-*-' *15)
lista = list()
jogo = int(input('Quantos jogos você quer que eu sorteie? '))
iniciador = 0
jogos = list()
while iniciador < jogo:
    contador = 0
    while True:
        escolhas = randint(1, 60)
        if escolhas not in lista:
            lista.append(escolhas)
            contador += 1
        if contador >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    iniciador += 1
for numero, lista in enumerate(jogos):
    print(f'Jogo {numero + 1}: {lista}')
    sleep(0.5)
print('-*-'*5, ' BOA SORTE', '-*-'*6)
