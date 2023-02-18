from random import randint
from time import sleep
import playsound
print('--='*30)
print('  Olá, humano! Vamos jogar um jogo... Advinhe em que número estou pensando entre 0 e 5.')
print('--='*30)
com = randint(0, 5)
jog = int(input('Então... em que número estou pensando? '))
print('Processando...')
sleep(2)
if jog == com:
    print('Muito bem. Você venceu. Acho que merece meus parabéns!')
    playsound.playsound('euganhei.mp3')
else:
    print('ERRADO, escória! Eu pensei no número {}, não no {}, HAHAHA!!'.format(com, jog))
