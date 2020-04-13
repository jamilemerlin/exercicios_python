def notas(*valores, situacao=False):
    """
    analisar notas e situações de vários alunos
    :param valores: uma ou mais notas
    :param situacao: opcional, se é necessário mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    dadosgerais = dict()
    dadosgerais['total'] = len(valores)
    dadosgerais['maior nota'] = max(valores)
    dadosgerais['menor nota'] = min(valores)
    dadosgerais['media geral'] = sum(valores)/len(valores)
    if situacao:
        if dadosgerais['media geral'] >= 7:
            dadosgerais['situação'] = 'BOA'
        elif dadosgerais['media geral'] >= 5:
            dadosgerais['situação'] = 'RAZOÁVEL'
        else:
            dadosgerais['situação'] = 'RUIM'
    return dadosgerais


resposta = notas(5.5, 5, 2, 6.5, situacao=True)
print(resposta)

