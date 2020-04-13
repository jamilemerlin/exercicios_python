lista = []
for contador in range(0, 5):
    entrada = int(input('Digite um valor: '))
    if contador == 0 or entrada > lista[-1]:
        lista.append(entrada)
        print(f'O número {entrada} foi adicionado ao final da lista.')
    else:
        for posicao, valor in enumerate(lista):
            if entrada <= valor:
                lista.insert(posicao, entrada)
                print(f'O número {entrada} foi adicionado na posicão {posicao}.')
                break
print(f'{lista}')
