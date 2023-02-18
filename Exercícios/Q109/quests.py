import moeda

print('-' * 30)
print(f'{"Registro de Preços":^30}')
print('-' * 30)

n = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}')
print(f'Aumentando 10% é {moeda.aumentar(n, 10, True)}')
print(f'Com desconto de 20% é {moeda.diminuir(n, 20, True)}')
