lista = [[], []]
for num in range(1, 8):
    a = int(input(f'Digite o {num}º valor: '))
    if a % 2 == 0:
        lista[0].append(a)
    else:
        lista[1].append(a)
for n, c in enumerate(lista):
    lista[n].sort()
print('-='*20)
print(f'Os números pares digitados foram: {lista[0]}')
print(f'Os números ímpares digitados foram: {lista[1]}')
