def computador_escolhe_jogada(n, m):
    nova = n % (m + 1)
    if nova > 1:
        print("O computador tirou", nova, "peças.\n")
    elif nova == 0:
        return m
    else:
        print("O computador tirou 1 peça.\n")
    return nova


def usuario_escolhe_jogada(n, m):
    novom = -1
    while novom <= 0 or novom > m:
        novom = int(input("Quantas peças você vai tirar? "))
        if novom > m:
            print("Oops! Jogada inválida! Tente de novo.\n")

    if novom > 1:
        print("Você tirou", novom, "peças.\n")
    else:
        print("Você tirou 1 peça.\n")
    return novom


def campeonato():
    rodada = 1
    while rodada <= 3:
        print("\n **** Rodada", rodada, "**** \n")
        partida()
        rodada += 1


def partida():
    n = 0
    while n <= 0:
        n = int(input("Com quantas peças o jogo começa? "))
        if n < 0:
            print("Digite um número maior que 0.")

    m = n + 1
    while m <= 0 or m >= n:
        m = int(input("Qual o limite de peças retiradas por jogada? "))
        if m <= 0:
            print("Digite um número maior que 0.")

    if n % (m + 1) == 0:
        jogada = 1
        print("\nVocê começa \n")
    else:
        jogada = 0
        print("\nComputador começa \n")

    while n > 0:
        if jogada == 0:
            n -= computador_escolhe_jogada(n, m)
            jogada = 1
        else:
            n -= usuario_escolhe_jogada(n, m)
            jogada = 0

        if n > 1:
            print("Agora restam", n, "peças no tabuleiro.")

    if jogada == 1:
        print("Fim de jogo! O computador ganhou.")
    else:
        print("Fim de jogo! Você ganhou.")


print("Bem vindo ao jogo NIM!")
x = int(input("Escolha:\n 1 - para uma única partida \n 2 - para um campeonato \n "))
if x == 1:
    print("\n Você escolheu uma única partida! \n")
    partida()
else:
    print("\nVocê escolheu um campeonato!\n")
    campeonato()
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você", 0, "X", 3, "Computador\n")
