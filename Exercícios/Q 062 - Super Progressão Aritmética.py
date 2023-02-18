print('-=-=-=-= GERADOR DE PA =-=-=-=-=-')
p1 = int(input('Primeiro termo da PA: '))
r = int(input('Razão: '))
print('-='*17)
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} ->'.format(p1), end=' ')
        p1 += r
        cont += 1
    print('PAUSA')
    mais = int(input('Mais quantos termos? '))
print('FIM! Progressão finalizada com {} termos!'.format(cont))

# print('-=-=-=-= GERADOR DE PA =-=-=-=-=-')
# p1 = int(input('Primeiro termo da PA: '))
# r = int(input('Razão: '))
# print('-='*17)
# cont = mais = 0
# while cont < 10 + mais:
#     print('{} ->'.format(p1), end=' ')
#     p1 += r
#     cont += 1
#     if cont == 10 + mais:
#         print('PAUSA')
#         mais += int(input('Quer ver mais quantos termos? '))
#     elif mais == 0:
#         cont += mais
# print('FIM! Progressão finalizada com {} termos!'.format(cont))
