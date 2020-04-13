campeonato = ('Grêmio', 'Chapecoense', 'Curitiba', 'Palmeiras',
              'São Paulo', 'Corinthians', 'Paraná Clube',
              'Atletico Paranaense', 'Cruzeiro', 'Flamengo')
print('-' * 40)
print(f'Os cinco primeiros são:{campeonato[:5]}')
print('-' * 40)
print(f'Os quatro últimos são:{campeonato[6:]}')
print('-' * 40)
print(f'Em ordem alfabética fica:{sorted(campeonato)}')
print('-' * 40)
print(f'A Chapecoense está em: {campeonato.index("Chapecoense")+1}ª')
