from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Qual é o ano de nascimento da {}ª pessoa? '.format(c)))
    if atual - ano < 21:
        menor += 1
    else:
        maior += 1
print('Tivemos, ao todo, {} menor(es) de idade e {} maior(es) de idade.'.format(menor, maior))
