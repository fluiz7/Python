print('-='*28)
print("*{:^45}*".format("PROGRESSÃO ARITMÉTICA de 10 TERMOS!"))
print('-='*28)
pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
for c in range(pt, pt+10*raz, raz):
    print('{}'.format(c), end=' → ')
print('ACABOU')
