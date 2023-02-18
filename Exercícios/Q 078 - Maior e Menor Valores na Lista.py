num = list()
maior = menor = 0
for n in range(0, 5):
    num.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = menor = num[n]
    else:
        if num[n] >= maior:
            maior = num[n]
        if num[n] <= menor:
            menor = num[n]
print(f'Você digitou os valores: {num}')
print(f'O maior valor digitado foi {maior} nas posições:', end=' ')
for pos, valor in enumerate(num):
    if valor == maior:
        print(pos, end='... ')
print(f'\nO menor valor digitado foi {menor} nas posições:', end=' ')
for pos, valor in enumerate(num):
    if valor == menor:
        print(pos, end='... ')
