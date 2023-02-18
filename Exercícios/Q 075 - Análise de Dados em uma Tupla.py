valores = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
# cont = 0
print(f'Você digitou os valores: {valores}')
# for cada in valores:
#    if cada == 9:
#         cont += 1
print(f'O valor 9 apareceu {valores.count(9)} vezes.')
if 3 in valores:
    print(f'O valor 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print(f'O valor 3 não apareceu em nenhuma posição.')
print('Os valores pares digitados são:', end=' ')
for cada in valores:
    if cada % 2 == 0:
        print(cada, end=' ')
