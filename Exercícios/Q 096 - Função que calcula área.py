def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno de {larg}m x {comp}m é igual a {a}m²')


# PROGRAMA PRINCIPAL
print('Controle de Terrenos')
print('-' * 20)
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)
