# for c in range(1, 10):
#     print(c)
# print('FIM!')

# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('FIM!')

# for c in range(1, 5):
#    n = int(input('Digite um número: '))
# print('FIM!')

# Chamamos isso de flag ou também de  ponto de parada
# c = 1
# while c != 0:
#     c = int(input('Digite um número: '))
# print('FIM!')

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um número: '))
#     r = str(input('Quer continuar? (S/N) ')).upper().strip()
# print('FIM!')

c = a = r = 0
n = 1
while n != 0:
    n = int(input('Digite um número:'))

    if n != 0:
        a += 1
        if n % 2 == 0:
            c += 1
        else:
            r += 1
print('Houve {} números, dentre eles, {} pares e {} ímpares.'.format(a, c, r))
