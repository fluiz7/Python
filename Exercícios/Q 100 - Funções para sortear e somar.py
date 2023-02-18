from random import randint
from time import sleep


def sorteia(num):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        num.append(randint(1, 10))
        print(num[c], end=' ')
        sleep(0.3)
    print('PRONTO!')
    sleep(0.5)


def somapar(num):
    par = 0
    for c in num:
        if c % 2 == 0:
            par += c
    print(f'Somando os valores pares de {numeros}, temos {par}.')


# Programa Principal
numeros = list()
sorteia(numeros)
somapar(numeros)
