lista = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    while True:
        q = str(input('Quer continuar? [S/N] ')).strip()[0]
        if q in 'SsNn':
            break
        else:
            print('Digite "S" ou "N"! ', end=' ')
    if q in 'Nn':
        break
print('-=' * 30)
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente temos: {lista}')
if 5 in lista:
    print('O valor 5 foi digitado e está na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
