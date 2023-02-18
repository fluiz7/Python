dist = float(input('A viagem será de quantos KMs, amigo? '))
valor = dist * 0.50 if dist <= 200 else dist * 0.45
print('O valor para a corrida de {}km, será de R${:.2f}.'.format(dist, valor))
