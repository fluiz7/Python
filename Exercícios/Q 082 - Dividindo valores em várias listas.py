listaori = []
listapar = []
listaimp = []
while True:
    listaori.append(int(input('Digite um valor: ')))
    while True:
        q = str(input('Quer continuar? [S/N] ')).strip()[0]
        if q in 'SsNn':
            break
        else:
            print('Digite "S" ou "N"!', end=' ')
    if q in 'Nn':
        break
print('-=' * 30)
for c in listaori:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimp.append(c)
print(f'Você digitou os seguintes valores: {listaori}')
print(f'Entre os pares, temos: {listapar}')
print(f'Já entre os ímpares: {listaimp}')
