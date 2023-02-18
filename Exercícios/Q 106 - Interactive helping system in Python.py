def ajuda():
    from time import sleep
    while True:
        a = '  SISTEMA DE AJUDA PyHELP  '
        print(f'\033[42m{"~"*len(a)}', f'\n{a}', f'\n{"~"*len(a)}')
        sleep(0.5)
        com = input('\033[mFunção ou Biblioteca > ')
        if com.upper() == 'FIM':
            break
        b = f'  Acessando o manual do comando {com}  '
        sleep(0.2)
        print(f'\033[44m{"~"*len(b)}', f'\n{b}', f'\n{"~"*len(b)}')
        sleep(0.5)
        print('\033[7;40m', end='')
        help(com)
        print('\033[m', end='')
        sleep(1)


# Programa Principal
ajuda()
