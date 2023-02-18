from random import randint
from time import sleep
from operator import itemgetter

jogadores = {'jogador1': randint(1, 6),
             'jogador2': randint(1, 6),
             'jogador3': randint(1, 6),
             'jogador4': randint(1, 6)}
print(f'{"VALORES SORTEADOS":-^30}')
for j, d in jogadores.items():
    print(f' O {j} tirou {d} no dado!')
    sleep(1)
print('-=-' * 10)
print(f'{"== RANKING DOS JOGADORES ==": ^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for n, v in enumerate(ranking):
    print(f'  {n+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
