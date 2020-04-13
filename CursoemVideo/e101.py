def voto(ano):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - ano
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    if 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'


nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))