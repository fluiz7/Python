lista = []
lista_ordenada = []
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    lista += [peso]
    lista_ordenada = sorted(lista)
print('O menor peso listado foi de {}Kg\nEnquanto o maior foi de {}Kg.'.format(lista_ordenada[0], lista_ordenada[-1]))
