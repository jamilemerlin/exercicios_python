frase = str(input('Digite uma frase qualquer: ')).strip().lower()
dividindo = frase.split()
juntando = ''.join(dividindo)
inverso = ''
# poderia ser ainda:
# inverso = juntando[::-1]
# vai gerar o mesmo resultado em menos linhas
for letra in range(len(juntando) -1, -1,-1):
    inverso += juntando[letra]
if inverso == juntando:
    print(f'A frase {juntando} invertida é {inverso}')
    print(f'E \033[7;30m{frase}\033[m é um palindromo')
else:
    print(f'A frase {juntando} invertida é {inverso}')
    print(f'E \033[7;30m{frase}\033[m não é um palindromo')