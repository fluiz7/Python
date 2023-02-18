cont = soma = n = 0
while n != 999:
    n = float(input('Digite um número [999 faz parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('Você digitou {} números e a soma entre eles é {}.'.format(cont, soma))
