def escreva(texto):
    comprimento = len(texto)+4
    print('~'*(comprimento))
    print(f'  {texto}')
    print('~'*(comprimento))


texto1 = 'Jamile Merlin'
texto2 = 'Desenvolvedora back-end'
texto3 = 'Desenvolvedora mobile'
escreva(texto1)
escreva(texto2)
escreva(texto3)
