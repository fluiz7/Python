num = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print('Analisando o número: {}'.format(num))
print('''Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}'''. format(num[3], num[2], num[1], num[0]))
