lista = list()
dado = list()
maior = menor = 0
print('-='*15)
while True:
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(float(input('Peso: ')))
    print('-=' * 15)
    if len(lista) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        elif dado[1] < menor:
            menor = dado[1]
    lista.append(dado[:])
    dado.clear()
    while True:
        q = str(input('Quer continuar? [S/N] ')).strip()[0]
        print('-=' * 15)
        if q in 'SsNn':
            break
        else:
            print('Tente de novo!', end=' ')
    if q in 'Nn':
        break
print('-'*30)
print(f'Você cadastrou um total de {len(lista)} pessoas!')
print(f'O maior peso foi de {maior}Kg e pertence a ', end='')
for c in lista:
    if c[1] == maior:
        print(f'-{c[0]}-', end=' ')
print(f'\nO menor peso foi de {menor}Kg e pertence a ', end='')
for c in lista:
    if c[1] == menor:
        print(f'-{c[0]}-', end=' ')
