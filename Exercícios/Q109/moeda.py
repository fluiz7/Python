def aumentar(preco, taxa, formatar=False):
    res = preco * (100 + taxa) / 100
    return res if formatar is False else moeda(res)


def diminuir(preco, taxa, formatar=False):
    res = preco * (100 - taxa) / 100
    return res if formatar is False else moeda(res)


def dobro(num, formatar=False):
    res = num * 2
    return res if formatar is False else moeda(res)


def metade(num, formatar=False):
    res = num / 2
    return res if formatar is False else moeda(res)


def moeda(valor, cambio='R$'):
    res = f'{cambio}{valor:.2f}'.replace('.', ',')
    return res
