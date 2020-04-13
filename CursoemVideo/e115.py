from utilidadescev.dado import cadastropessoas
from utilidadescev.dado import arquivo

nome_arquivo = 'cursoemvideo.txt'

if arquivo.arquivoexiste(nome_arquivo):
    print('Arquivo encontrado!')
else:
    arquivo.criararquivo(nome_arquivo)

while True:
    cadastropessoas.cabecalho('MENU PRINCIPAL')
    escolha = cadastropessoas.menuprincipal()
    if escolha == 1:
        cadastropessoas.cabecalho('PESSOAS CADASTRADAS')
        cadastropessoas.pessoascadastradas(nome_arquivo)
    elif escolha == 2:
        cadastropessoas.cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastropessoas.novocadastro(nome_arquivo, nome, idade)
    elif escolha == 3:
        break
    else:
        print('\033[31mERRO! Por favor digite um número válido.\033[m')
print('Saindo do sistema... Até logo!')
