# lista = []
# while True:
#     lista.append(int(input('Digite um valor: ')))
#     if lista[-1] in lista[:-1]:
#         print('Valor duplicado! Tente outro!!')
#         lista.pop()
#     else:
#         print('Valor adicionado com sucesso!')
#     a = ' '
#     while a != 'N':
#         a = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
#         if a in 'SN':
#             break
#         else:
#             print('Digite "S" ou "N"!', end=' ')
#     if a == 'N':
#         lista.sort()
#         break
# print(f'Você digitou os valores: {lista}')
numeros = list()
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionador com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
    elif r not in 'Ss':
        print('Tente de novo!', end=' ')
numeros.sort()
print(f'Você digitou os valores {numeros}')
