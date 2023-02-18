import moeda

print('-' * 30)
print(f'{"Registro de Preços":^30}')
print('-' * 30)

n = float(input('Digite o preço: R$'))
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O valor R${n} com aumento de {10}% é R${moeda.aumentar(n, 10)}')
print(f'O valor R${n} com desconto de {20}% é R${moeda.diminuir(n, 20)}')
