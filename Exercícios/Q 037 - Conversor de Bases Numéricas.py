num = int(input('Digite um número inteiro: '))
base = int(input('''Escolha uma das bases para conversão:
[ 1 ] converter para \033[4;32mBINÁRIO\033[m
[ 2 ] converter para \033[4;35mOCTAL\033[m
[ 3 ] converter para \033[4;31mHEXADECIMAL\033[m
Sua opcão: '''))
if base == 1:
    print('Em \033[4;32mBINÁRIO\033[m, o número {}, é {}'.format(num, format(num, 'b')))
elif base == 2:
    print('Em \033[4;35mOCTAL\033[m, o número {} é {}.'.format(num, format(num, 'o')))
elif base == 3:
    print('Em \033[4;31mHEXADECIMAL\033[m, o número {} é {}'.format(num, format(num, 'x')))
else:
    print('Digite um dos números citados!')
# Também podemos usar a as funções bin(b), oct(o) e hex(x). Para excluir o 0b e tals, basta fatiar [2:]!
