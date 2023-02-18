# cont = 1
# while True:
#     print(cont, '-> ', end='')
#     cont += 1
# print('Acabou!')
#
# n = s = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     s += n
# print('A soma vale {}'.format(s))
# f strings - atualização
# print(f'A soma vale {s}')
nome = 'José'
idade = 33
#print(f'O {nome} tem {idade} anos!')
# print('O {} tem {} anos!'.format(nome, idade))
salario = 1001.8
print(f'O {nome:-^20} tem {idade:->5} anos e recebe R${salario:.2f}')
