from _datetime import date
ano = int(input('Sobre que ano você deseja saber? Digite 0 pra saber sobre o ano atual. '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))
else:
    print('O ano {} não é BISSEXTO'.format(ano))
