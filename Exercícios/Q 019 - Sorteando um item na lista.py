from random import choice
#print('Vamos sortear quem vai apagar o quadro!')
#
#a = input('Primeiro aluno: ')
#b = input('Segundo aluno: ')
#c = input('Terceiro aluno: ')
#d = input('Quarto aluno: ')
#
#print('O aluno escolhido para apagar o quadro foi: {}'. format(choice([a, b, c, d])))

print('Vamos sortear quem vai apagar o quadro!')

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')
lista = [a,b,c,d]
print('O aluno escolhido para apagar o quadro foi: {}'. format(choice(lista)))