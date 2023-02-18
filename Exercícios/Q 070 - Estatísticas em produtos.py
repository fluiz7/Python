totG = prodM = prodB = 0
nB = ' '
print('-='*14)
print('  MONITORADOR DE COMPRAS!')
while True:
    print('-'*28)
    nome = str(input('Nome do produto: ')).strip().capitalize()
    prec = float(input('Preço: R$'))
    if prodB == 0 or prec < prodB:
        prodB = prec
        nB = nome
    if prec >= 1000:
        prodM += 1
    q = ' '
    totG += prec
    while q not in 'SsNn':
        print('-'*28)
        q = str(input('Quer continuar? [S/N] '))
    if q in 'Nn':
        break
print(f'{"ENCERRANDO":-^30}')
print(f'Total Gasto: R${totG:.2f}\nProdutos acima de R$1000,00: {prodM}')
print(f'Produto mais barato: {nB}; Custa: R${prodB:.2f}')
