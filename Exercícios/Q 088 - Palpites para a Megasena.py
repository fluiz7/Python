from random import randint
from time import sleep

# print('-'*33)
# print(f'{"JOGOS DA MEGASENA":^33}')
# print('-'*33#)
#
# jogos = int(input('Quantos jogos você quer sortear? '))
# palpites = []
# while len(palpites) < jogos:
#     palpites += [[0, 0, 0, 0, 0, 0]]
# print(f'-=-=-=-= SORTEANDO {jogos} JOGOS =-=-=-=-')
# for lis in range(0, jogos):
#     for num in range(0, 6):
#         palpites[lis][num] = randint(0, 60)
#         while True:
#             if palpites[lis][num] in palpites[lis][0:num]:
#                 palpites[lis][num] = randint(0, 60)
#             else:
#                 break
#     palpites[lis].sort()
#     print(f'Jogo {lis+1}: {palpites[lis]}')
#     sleep(0.5)
# print('-=' * 5, f'{"< BOA SORTE >"}', '=-' * 5)
#
lista = list()
jogos = list()
print('-=' * 20)
print('           JOGAR NA MEGA SENA     ')
print('-=' * 20)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '=-' * 3)
for i, l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
print('-=' * 5, f'< BOA SORTE! >', '=-' * 5)
