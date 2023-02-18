print('Oi, tudo bem? Vamos precisar de algumas informações, ok?')
valor = float(input('Qual é o valor da casa que você pretende comprar? R$'))
sal = float(input('E quanto você recebe de salário por mês? R$'))
ano = int(input('Entendi, entendi, e você pretende pagar em quantos anos? '))
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f} por mês.'
      .format(valor, ano, valor/(ano*12)))
mes = sal*30/100
if valor/(ano*12) <= sal*30/100:
    print('Empréstimo \033[1;32mAPROVADO\033[m!')
else:
    print('Empréstimo \033[1;31mNEGADO\033[m!')
