def leiaint(num):
    print('-' * 35)
    while True:
        saida = input(num)
        if saida.isnumeric():
            saida = int(saida)
            break
        else:
            print('\033[1;31mErro! Digite um número inteiro válido!\033[m')
    return saida


# Programa Principal
n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
