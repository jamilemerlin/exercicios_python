def fatorial(a, show=False):
    """
    -> calcula o fatorial de um número.
    :param a: número a ser calculado
    :param show: opcional, mostrar ou não a conta
    :return: o valor fatorial de um número a.
    """
    f = 1
    for valor in range(a, 0, -1):
        if show:
            print(f'{valor}', end='')
            if valor > 1:
                print(f' X ', end='')
            else:
                print(f' = ', end='')
        f *= valor
    return f


print(fatorial(5, True))