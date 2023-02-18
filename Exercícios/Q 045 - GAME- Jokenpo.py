from time import sleep
from random import choice

from pygame import mixer
mixer.init()
mixer.music.load("jokenpo.mp3")
mixer.music.play()

print('\033[1;37mJO')
sleep(0.3)
print('KEN')
sleep(0.3)
print('PO\033[m!!!')
sleep(0.3)
jog = int(input('Seus ataques são:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\nQual deles você utilizará? '))
com = choice(['PEDRA', 'PAPEL', 'TESOURA'])
vic = 'Tente de novo!'
if jog == 0:
    jog = 'PEDRA'
    mixer.music.load("pedraa.mp3")
    mixer.music.play()
    if com == 'PEDRA':
        mixer.music.queue("pedra.mp3")
        vic = 'Houve um EMPATE!!'
    elif com == 'PAPEL':
        mixer.music.queue("papel.mp3")
        vic = 'O Computador VENCEU!'
    else:
        mixer.music.queue("tesoura.mp3")
        vic = 'O Jogador VENCEU!'
elif jog == 1:
    jog = 'PAPEL'
    mixer.music.load("papell.mp3")
    mixer.music.play()
    if com == 'PEDRA':
        mixer.music.queue("pedra.mp3")
        vic = 'O Jogador VENCEU!'
    elif com == 'PAPEL':
        mixer.music.queue("papel.mp3")
        vic = 'Houve um EMPATE!!'
    else:
        mixer.music.queue("tesoura.mp3")
        vic = 'O Computador VENCEU!'
elif jog == 2:
    jog = 'TESOURA'
    mixer.music.load("tesouraa.mp3")
    mixer.music.play()
    if com == 'PEDRA':
        mixer.music.queue("pedra.mp3")
        vic = 'O Computador VENCEU!'
    elif com == 'PAPEL':
        mixer.music.queue("papel.mp3")
        vic = 'O Jogador VENCEU!'
    else:
        mixer.music.queue("tesoura.mp3")
        vic = 'Houve um EMPATE!!'

else:
    print('Digite um dos números acima!')
    exit()

print('\033[1;33m-=\033[m' * 20)
print('Jogador usou {}!'.format(jog))
sleep(0.5)
print('Computador usou {}!'.format(com))
print('\033[1;33m-=\033[m'*20)
sleep(1)
if vic == 'Houve um EMPATE!!':
    print(vic)
    mixer.music.load("peniguais.mp3")
    mixer.music.play()
elif vic == 'O Jogador VENCEU!':
    print(vic)
    mixer.music.load("parabens.mp3")
    mixer.music.play()
elif vic == 'O Computador VENCEU!':
    print(vic)
    mixer.music.load("maravilha.mp3")
    mixer.music.play()
input('Pressione qualquer tecla para encerrar!')
