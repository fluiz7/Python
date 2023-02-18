fra = str(input('Digite uma frase: ')).strip().lower()
# totA = fra.count('a')
# priA = fra.find('a') + 1
# ultA = fra.rfind('a') + 1
# print("""A letra aparece {} vezes na frase;
# A primeira letra A apareceu na posição: {};
# A última letra A apareceu na posição: {}.""" .format(totA, priA, ultA))
print('A letra aparece {} vezes na frase;'.format(fra.count('a')))
print('A primeira letra A apareceu na posição: {};'.format(fra.find('a')+1))
print('A última letra A apareceu na posição: {}.'.format(fra.rfind('a')+1))
