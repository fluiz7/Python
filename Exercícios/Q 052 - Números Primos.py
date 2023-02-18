num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        cont += 1
        print('\033[1;32m{}'.format(c), end=' ')
    else:
        print('\033[1;31m{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, cont))
if cont == 2:
    print('E por isso ele \033[1;32mÉ\033[m um número primo!')
else:
    print('E por isso ele \033[1;31mNÃO É\033[m um número primo!')
