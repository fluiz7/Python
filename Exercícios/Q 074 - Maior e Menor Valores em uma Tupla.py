from random import randint

aleat = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# ordem = sorted(aleat)

print('Os números sorteados foram: ', end='')
for c in aleat:
    print(c, end=' ')
# print(f'\nO maior valor sorteado foi: {ordem[4]}')
# print(f'O menor valor sorteado foi: {ordem[0]}')
print(f'\nO maior valor sorteado foi: {max(aleat)}')
print(f'O menor valor sorteado foi: {min(aleat)}')