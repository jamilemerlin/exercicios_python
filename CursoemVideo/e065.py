continuar = 1
entrada = 0
media = 0
maior = 0
menor = 0
quantidade = 0

while continuar == 1:
    entrada = int(input('Digite um número para juntar a somatória da média: '))
    continuar = int(input('Você deseja continuar?'
                          '\nSIM = 1'
                          '\nNÃO = 2'
                          '\n-> '))
    media += entrada
    quantidade += 1
    if quantidade == 1:
        menor = entrada
        maior = entrada
    else:
        if entrada < menor:
            menor = entrada
        if entrada > maior:
            maior = entrada

print(f'A média dos números é {media / 2:.1f},'
      f'\no maior número foi {maior},'
      f'\no menor número foi {menor}')
