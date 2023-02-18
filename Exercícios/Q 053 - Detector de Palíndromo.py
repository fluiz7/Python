# fra = str(input('Escreva uma frase: ')).strip().upper().replace(' ', '')
# print('A frase {} ao contrário é {}'.format(fra, fra[-1::-1]))
# if fra == fra[::-1]:
#     print('Então temos um palíndromo!')
# else:
#     print('Logo, não temos um palíndromo!')
fra = str(input('Escreva uma frase: ').strip().upper())
pala = fra.split()
junto = ''.join(pala)
contrario = ''
for letra in range(len(junto) - 1, -1, -1):
    contrario += junto[letra]
print('A frase {} invertida é {}.'.format(junto, contrario))
if junto == contrario:
    print('Temos um palíndromo!')
else:
    print('Isso não é um palíndromo!')
