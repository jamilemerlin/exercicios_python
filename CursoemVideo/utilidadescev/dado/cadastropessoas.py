from utilidadescev.dado import dado


def cabecalho(texto):
    print('-' * 30)
    print(texto.center(30))
    print('-' * 30)

def novocadastro(arquivo, nome='Desconhecido', idade=0):
    try:
        abrir = open(arquivo, 'at')
    except:
        print('Erro ao adicionar informações no arquivo.')
    else:
        abrir.write(f'{nome};{idade}\n')
        print(f'Novo registro de {nome} adicionado')
        print('-' * 30)
    finally:
        abrir.close()



def pessoascadastradas(lista):
    try:
        abrir = open(lista, 'rt')
    except:
        print('Houve um erro na leitura.')
    else:
        for linha in abrir:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<20} {dado[1]:>4} anos')
    finally:
        abrir.close()
    print('-' * 30)


def menuprincipal():
    print('\033[34m1 - Ver pessoas cadastradas\033[m')
    print('\033[34m2 - Cadastrar nova pessoa\033[m')
    print('\033[34m3 - Sair do sistema\033[m')
    print('-' * 30)
    escolha = dado.leiaInt('\033[32mSua opção: \033[m')
    return escolha
