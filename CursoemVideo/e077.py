palavras = ('AMOR', 'AMIGOS', 'NOVO ANO', 'APRENDER', 'CURSOS', 'PRATICAR', 'PYTHON', 'LINGUAGEM',
            'FUTURO', 'PROGRAMADORA')
for palavra in palavras:
    print(f'Na palavra {palavra} temos as seguintes vogais: ', end='')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra}', end='')
    print(' ')
