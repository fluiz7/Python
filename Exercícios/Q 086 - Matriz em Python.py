# lista = [[], [], []]
# for i, n in enumerate(lista):
#     for c in range(0, 3):
#         lista[i].append(int(input(f'Digite um valor para {[i, c]}: ')))
# print('-='*20)
# for i, n in enumerate(lista):
#     for c in range(0, 3):
#         print(f'[{lista[i][c]:^5}]', end='')
#     print()
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}: '))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5]}]', end='')
    print()
