dados = list() # "dados" eh um nome muito generico. Busque dar mais significado com base no que esta variavel vai armazenar. Exemplo: boletins
cont = 0 # sugestao: escreva a palavra inteira - renomeie para "contador" ou "counter". "cont" pode confundir com "continuar" (ali de baixo). Como essa variavel armazena o numero do aluno, poderia tbm se chamar "numero_do_aluno"
while True:
    media = 0
    nome = str(input('Qual o nome do aluno? ')).upper() # ? nao ta faltando parenteses aqui?

    dadosDoAluno = []
    dadosDoAluno.append(nome)
     # Nao tenho certeza, mas acho que voce se perdeu nas listas. Talvez se voce criar uma lista para cada aluno primeiro e, depois de ler todas as notas, voce adiciona essa "lista do aluno" na lista "dados", talvez ajude.
    for c in range(1, 3): # "c" eh um nome bom pq poderia ser a "coluna" 1 ou 2... Mas acho que "n" ficaria melhor, pois poderia ser a "nota" 1 ou 2.
        nota = float(input(f'{c}ª nota: '))
        media += nota
        dadosDoAluno.append(nota) # atencao: toda vez que passar aqui, uma nova lista eh criada com apenas um elemento (nota). Entao, Nota 1 === [nota] e Nota 2 == [nota]. E dados[cont] vai conter: [[nome], [nota], [nota]]
    media = media / 2 # Lembre-se de "zerar" a variavel "media" no inicio do loop. (antes de ler o "nome")
    dadosDoAluno.append(media) # seguindo a logica da linha 10, aqui voce tera como resultado: dados[cont] == [ [nome], [nota], [nota], media ], certo?

    dados.append(dadosDoAluno)

    cont += 1
    continuar = str(input('Deseja continuar? [S/N] -> ')).upper().strip()
    if continuar == 'N':
        break

print('-*' *30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' *26)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[3]:>6}') # essa linha isoladamente ficou bem dificil de ler... adivinhar o que eh "i" e "a" de dados fica dificil. Acho que pode melhorar
while True:
    print('-'* 35)
    verdados = str(input('Deseja ver as notas de algum aluno? [S/N] -> ')).upper().strip()
    if verdados == 'N':
        break
    elif verdados == 'S':
        aluno = int(input('Qual aluno você deseja ver as notas? '))
        if aluno <= len(dados) - 1: # nessa linha voce pode usar o sinal de "<" e remover o "- 1".
            print(f'Aluno:{dados[aluno][0]},'
                  f'\nNota 1: {dados[aluno][1]}'
                  f'\nNota 2: {dados[aluno][2]}')

# Consideracoes finais:
# - acho que ta muito bom e vai dar certo desse jeito sim. So precisa rever as "listas dentro de listas" na linha 10
# - os outros comentarios sao soh "perfumaria" (tbm chamado de "nitpick" em code review)
