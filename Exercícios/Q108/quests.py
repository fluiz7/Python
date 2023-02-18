import moeda

print('-' * 30)
print(f'{"Registro de Preços":^30}')
print('-' * 30)

n = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}')
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}')
print(f'O valor {moeda.moeda(n)} com aumento de {10}% é {moeda.moeda(moeda.aumentar(n, 10))}')
print(f'O valor {moeda.moeda(n)} com desconto de {20}% é {moeda.moeda(moeda.diminuir(n, 20))}')
