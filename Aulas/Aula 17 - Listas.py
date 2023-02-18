# num = [2, 5, 9, 1]
# um[2] = 3
# num.append(8)
# num.sort(reverse=True)
# if 5 in num:
#     num.remove(5)
# else:
#     print('Não achei o número 5')
# print(num)
# print(f'Essa lista tem {len(num)} elementos.')
# valores = list()
# for cont in range(0, 5):
#     valores.append(int(input('Digite um valor:')))
# print(valores)
# for c, v in enumerate(valores):
#     print(f'Na posição {c} encontrei o valor {v}!')
# print('Cheguei ao final da lista!')
a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
# a partir do momento que igualamos duas listas, o python cria uma ligação entre elas
# portanto qualquer alteração que fizermos em uma também será feito em outra
# para que não haja uma ligação, a cópia deverá copiar toda a fatia
b = a[:]
b[2] = 6
print(f'Lista B: {b}')
