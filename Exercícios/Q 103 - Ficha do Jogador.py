def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gols no campeonato!')


# Programa Principal
j = str(input('Nome do Jogador: ')).strip()
p = str(input('Número de Gols: '))
if p.isnumeric():
    p = int(p)
else:
    p = 0
if j == '':
    ficha(gols=p)
else:
    ficha(j, p)
