print('-=-=-=-= GERADOR DE PA =-=-=-=-=-')
p1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão: '))
print('-='*17)
cont = 0
while cont < 10:
    print('{} ->'.format(p1), end=' ')
    p1 += r
    cont += 1
print('FIM!')
