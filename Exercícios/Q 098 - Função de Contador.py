from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 15)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo * -1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}.')
    if inicio > fim:
        passo = -passo
        fim -= 1
    else:
        fim += 1
    for c in range(inicio, fim, passo):
        print(c, end=' ')
        sleep(0.5)
    print('FIM!')


# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 15)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
