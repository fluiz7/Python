def fatorial(num, show=False):
    """
    -> Função que fará o cálculo fatorial de um número qualquer, podendo mostrar
    ou não o processo matemático.
    :param num: número que será calculado de forma fatorial.
    :param show: (opcional) decide se o cálculo deverá ser mostrado ou não.
    :return: o valor fatorial de um número n.
    Funçaõ feita por Luiz Felipe, estudante de Engenharia de Computação.
    """
    print('-' * 30)
    fat = 1
    for c in range(num, 0, -1):
        fat *= c
        if show:
            print(f'{c} x ', end='') if c > 1 else print(f'{c} = ', end='')
    return fat


# Programa Principal
print(fatorial(5, True))
