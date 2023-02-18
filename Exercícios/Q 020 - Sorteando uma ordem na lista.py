import random
print('Vamos sortear a ordem da apresentação dos trabalhos.')

a = input('Nome do primeiro aluno: ')
b = input('Nome do segundo aluno: ')
c = input('Nome do terceiro aluno: ')
d = input('Nome do quarto aluno: ')

lista = [a, b, c, d]
# random.shuffle(lista)
#
# print('Os alunos apresentarão na seguinte ordem: \n {}'. format(lista))

ass = random.sample([a, b, c, d], 4)
print(ass)
