from random import randint
com = randint(0, 10)
jog = int(input('Vamos lá... \nTente adivinhar em que número estou pensando entre 0 e 10: '))
cont = 1
while jog != com:
    cont += 1
    if jog < com:
        jog = int(input('Tá errado, inútil! Tenta de novo, vai, mais pra cima: '))
    else:
        jog = int(input('Tá errado, inútil! Tenta de novo, vai, mais pra baixo: '))
print('Acertou, masss...\nSério que você precisou jogar {} vez(es) pra acertar??'.format(cont))
