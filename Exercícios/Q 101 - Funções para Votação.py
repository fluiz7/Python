# from datetime import date
#
#
# def voto():
#     global idade
#     if 18 <= idade <= 64:
#         return 'OBRIGATÓRIO'
#     elif 16 <= idade <= 17 or idade >= 65:
#         return 'OPCIONAL'
#     else:
#         return 'NEGADO'
#
#
# nasc = int(input('Ano de nascimento: '))
# idade = date.today().year - nasc
# print(f'Com {idade} anos, seu voto será {voto()}!')


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'


# Programa Principal
nasc = int(input('Qual o seu ano de nascimento? '))
print(voto(nasc))