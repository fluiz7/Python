from random import randint
cont = vit = 0
print('-='*50)
print(f'{"VAMOS JOGAR PAR OU ÍMPAR!!":^90}')
print('-='*50)
while True:
    com = randint(0, 10)
    j1 = int(input('Joga um número: '))
    esc = ' '
    while esc not in 'PI':
        esc = str(input('Par ou Ímpar[P/I]: ')).strip().upper()[0]
    cont += 1
    tot = j1 + com
    if tot % 2 == 0:
        print('-' * 40)
        print(f'Você jogou {j1} e a máquina jogou {com}. O Total de {tot} deu PAR!')
        print('-' * 40)
        if esc == 'P':
            print('Você VENCEU!!')
            print('-><-' * 25)
            vit += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print('-' * 40)
        print(f'Você jogou {j1} e a máquina jogou {com}. O Total de {tot} deu ÍMPAR!')
        print('-' * 40)
        if esc == 'I':
            print('Você VENCEU!')
            print('-><-' * 25)
            vit += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar de novo...')
print('-=' * 35)
print(f'GAME OVER!! Você jogou {cont} vez(es) e VENCEU {vit} delas!')
print('-=' * 35)
