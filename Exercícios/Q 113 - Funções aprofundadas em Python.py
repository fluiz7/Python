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


def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Você não digitou um número REAL válido!\033[m')
        except KeyboardInterrupt:
            print('\033[33mO usuário decidiu encerrar o programa!\033[m')
            return 0
        else:
            return num


n = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um número real: ')
print(f'Você digitou os números:'
      f'Inteiro: {n}'
      f'Real: {f}')
