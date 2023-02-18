def aumentar(preco, taxa):
    res = preco * (100 + taxa) / 100
    return res


def diminuir(preco, taxa):
    res = preco * (100 - taxa) / 100
    return res


def dobro(num):
    res = num * 2
    return res


def metade(num):
    res = num / 2
    return res


def moeda(valor, moeda='R$'):
    res = f'{moeda}{valor:.2f}'.replace('.', ',')
    return res
