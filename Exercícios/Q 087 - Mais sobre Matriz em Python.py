matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = terceira = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 20)

print(f'A soma de todos os números pares é igual a: {par}')
for l in range(0, 3):
    terceira += matriz[l][2]
print(f'Já na soma da terceira coluna obtemos: {terceira}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[c][1]
    elif matriz[c][1] > maior:
        maior = matriz[c][1]
print(f'Enquanto que o maior valor da segunda coluna é: {maior}')
