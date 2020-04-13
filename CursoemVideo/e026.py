frase = str(input('Digite uma frase: ')).strip()
padrao = frase.lower()
letra = padrao.count('a')
comeca = padrao.find('a')
termina = padrao.rfind('a')
print(f'A letra A aparece {letra} na frase: {frase.upper()}'
      f'\nEla aparece a primeira vez na posição {comeca + 1}'
      f'\nE aparecea ultima vez em {termina + 1}.')
