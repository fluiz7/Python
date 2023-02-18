c = ('\033[m',  # 0 - sem cores
     '\033[0;31m',  # 1 - vermelho
     '\033[0;32m',  # 2 - verde
     '\033[0;33m',  # 3 - amarelo
     '\033[0;34m',  # 4 - azul
     '\033[0;35m',  # 5 - roxo
     '\033[7;30m'  # 6 - branco
     )


def formatar(msg):
    print(f'{c[2]}-' * 40)
    print(f'{msg:^40}')
    print(f'-' * 40, end='')
    print(c[0])


def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Você não digitou um número INTEIRO válido!\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[33mO usuário decidiu não fornecer dados!\033[m')
            return 0
        else:
            return num


def menu(lista):
    formatar(f'MENU PRINCIPAL')
    n = 1
    for item in lista:
        print(f'{c[3]}{n}{c[0]} - {c[4]}{item}{c[0]}')
        n += 1
    print(f'{c[2]}-' * 40)
    opc = leiaint(f'{c[3]}Sua opção: {c[0]}')
    return opc
