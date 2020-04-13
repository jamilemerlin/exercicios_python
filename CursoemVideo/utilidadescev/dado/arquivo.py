def arquivoexiste(nome):
    try:
        abrir = open(nome, 'rt')
        abrir.close()
    except:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        criar = open(nome, 'wt+') # o sinal de plus serve para criar o arquivo caso ele não exista.
        criar.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print('Arquivo criado com sucesso.')