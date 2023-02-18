print('{:#^40}'.format(' REDE CANTANHEDE '))
valor = float(input('Valor das compras: R$'))
cond = int(input('''\033[7;38m-=-=-=-=-=-=-=FORMAS DE PAGAMENTO=-=-=-=-=-=-=-\033[m
[ 1 ] À vista no dinheiro ou cheque com 10% de desconto!
[ 2 ] À vista no cartão com 5% de desconto!
[ 3 ] Em 2x no cartão.
[ 4 ] Em 3x ou mais no cartão com juros de 20%!
Qual será o método de pagamento? '''))
if cond == 1:
    print('A compra de R${:.2f} sairá por apenas R${:.2f} COM DESCONTO!'.format(valor, valor - valor * 10/100))
elif cond == 2:
    print('A compra de R${:.2f} sairá por apenas R${:.2f} COM DESCONTO!'.format(valor, valor - valor * 5/100))
elif cond == 3:
    print('O valor de R${:.2f} das compras sairá em duas parcelas de R${:.2f}!'.format(valor, valor - valor/2))
elif cond == 4:
    parc = int(input('Deseja pagar em quantas parcelas? '))
    print('Então a compra de R${:.2f} sairá por R${:.2f}!'.format(valor, valor + valor * 20/100))
    print('Isso dividido em {} parcelas de R${:.2f} COM JUROS!'.format(parc, (valor + valor * 20/100)/parc))
else:
    print('Digite um dos números sugeridos!!')
