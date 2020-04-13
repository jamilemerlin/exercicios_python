import re
import math
import sys


def le_assinatura():
    # A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    # A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    # A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
    return re.split(r"[,:;]+", sentenca)


def separa_palavras(frase):
    # A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
    return frase.split()


def n_palavras_unicas(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    # Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def calcula_assinatura(texto):
    # IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
    lista_sentenca = separa_sentencas(texto)
    tamanho_total_palavra = 0
    total_caracteres = 0
    total_caracteres_limpo = 0
    total_frases = 0
    total_palavras = 0
    todas_palavras = []
    for sentenca in lista_sentenca:
        frases = separa_frases(sentenca)
        total_caracteres += len(sentenca)
        total_frases += len(frases)
        for frase in frases:
            total_caracteres_limpo += len(frase)
            palavras = separa_palavras(frase)
            total_palavras += len(palavras)
            todas_palavras += palavras
            for palavra in palavras:
                tamanho_total_palavra += len(palavra)

    palavras_diferentes = n_palavras_diferentes(todas_palavras)
    palavras_unicas = n_palavras_unicas(todas_palavras)

    a = (
        tamanho_total_palavra / total_palavras
    )  # Tamanho médio de palavra: Média simples do número de caracteres por palavra.

    b = (
        palavras_diferentes / total_palavras
    )  # Relação Type-Token: Número de palavras diferentes divididas pelo total de palavras.

    c = (
        palavras_unicas / total_palavras
    )  # Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.

    d = total_caracteres / len(
        lista_sentenca
    )  # Tamanho médio de sentença: Média simples do número de caracteres por sentença.

    e = total_frases / len(
        lista_sentenca
    )  # Complexidade de sentença: Média simples do número de frases por sentença.

    f = (
        total_caracteres_limpo / total_frases
    )  # Tamanho médio de frase: Média simples do número de caracteres por frase.

    return a, b, c, d, e, f


def compara_assinatura(as_a, as_b):
    resultado = 0
    for i in range(6):
        resultado += abs(as_a[i] - as_b[i])
    return resultado / 6


def avalia_textos(textos, ass_cp):
    #  """IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH."""
    menor_comparacao = sys.maxsize
    contador = 1
    menor_indice = 1
    for texto in textos:
        ass_texto = calcula_assinatura(texto)
        assinatura_comparada = compara_assinatura(ass_texto, ass_cp)
        if assinatura_comparada < menor_comparacao:
            menor_comparacao = assinatura_comparada
            menor_indice = contador
        contador += 1

    print("O autor do texto", menor_indice, "está infectado com COH-PIAH")
    exit()


parametros = le_assinatura()
texto = le_textos()
avalia_textos(texto, parametros)


# ass1 = [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]
# ass2 = [4.33, 0.23, 0.14, 13.28, 1.86, 0.0]
# resultado = compara_assinatura(ass1, ass2)

# print(resultado)

# texto_1 =  "Navegadores antigos tinham uma frase gloriosa:\"Navegar é preciso; viver não é preciso\". Quero para mim o espírito [d]esta frase, transformada a forma para a casar como eu sou: Viver não é necessário; o que é necessário é criar. Não conto gozar a minha vida; nem em gozá-la penso. Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo. Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha. Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça."

# texto_2 = "Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres."

