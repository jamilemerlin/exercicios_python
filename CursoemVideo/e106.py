cor = ('\033[m',        # sem cor
       '\033[0;30;41m', # vermelho
       '\033[0;30;42m', # verde
       '\033[0;30;43m', # amarelo
       '\033[0;30;44m', # azul
       '\033[0;30;45m', # roxo
       '\033[7;30m'     # negativo
       );


def ajuda(mensagem):
    titulo(f'Acessando o manual do comando \'{mensagem}\'', 4)
    print(cor[6], end='')
    help(mensagem)
    print(cor[0], end='')


def titulo(msg, cores=0):
    tamanho = len(msg) + 4
    print(cor[cores], end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(cor[0], end='')


comando = ''
while True:
    titulo('Sistema de Ajuda PyHelp', 2)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)
