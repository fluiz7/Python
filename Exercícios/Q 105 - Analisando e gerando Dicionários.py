def notas(*num, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas de alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-' * 35)
    maior = menor = media = 0
    total = len(num)
    for n in num:
        media += n
        if maior == 0 and menor == 0:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            elif n < menor:
                menor = n
    media /= total
    regis = {'total': total, 'maior': maior, 'menor': menor, 'media': media}
    if sit:
        if 7 <= media:
            regis['situação'] = 'BOA'
        elif media <= 5:
            regis['situação'] = 'RUIM'
        else:
            regis['situação'] = 'RAZOÁVEL'
    return regis


# Programa Principal
resp = notas(5.5, 9.5, 0, 6.5, sit=True)
print(resp)
