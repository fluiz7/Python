lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
# cont = 1
# for c in lista:
#     if cont == 1:
#        print(f'{c:.<15}', end='')
#         print(f'{"R$":.>28}', end=' ')
#     if cont == 2:
#         print(f'{c:>6.2f}', '\n')
#         cont = 0
#     cont += 1
# print('-'*50)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('-'*50)
