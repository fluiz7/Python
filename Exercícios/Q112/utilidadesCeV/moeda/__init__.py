def aumentar(preco, taxa, formatar=False):
    """
    -> Função para aumentar o valor de algo com o uso de uma porcentagem
    :param preco: valor que desejo manipular
    :param taxa: valor da porcentagem que desejo usar
    :param formatar: se deve mostrar ou não o valor em formato monetário
    :return:
    """
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


def resumo(preco=0, aumento=10, desconto=5):
    print('-' * 33)
    print(f'RESUMO DO VALOR'.center(33))
    print('-' * 33)
    print(f'Preço analisado: \t{moeda(preco):100}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{desconto}% de redução: \t{diminuir(preco, desconto, True)}')
    print('-' * 33)
