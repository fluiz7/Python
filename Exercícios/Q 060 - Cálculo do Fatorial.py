# soma = n = int(input('Fatorial do número: '))
# print('Calculando {}! ='.format(n), end=' ')
# while n != 0:
#     print('{} '.format(n), end='')
#     print('='if n == 1 else 'X', end=' ')
#     if n - 1 == 0:
#         n = 0
#     else:
#         soma = soma * (n - 1)
#         n -= 1
# print(soma)

# from math import factorial
# n = int(input('Número: ))
# f = factorial(n)
# print('Fatorial de {} é {}'.format(n, f))

# c = n = int(input('Digite um número para calcular o seu fatorial'))
# f = 1
# print('Calculando {}! ='.format(n), end='')
# while c > 0:
#     print('{}'.format(c), end='')
#     print(' x ' if c > 1 else ' = ', end='')
#     f *= c
#     c -= 1
# print('{}'.format(f))

n = int(input('Número: '))
soma = 1
print('Calculando {}! ='.format(n), end=' ')
for c in range(n, 0, -1):
    print('{}'.format(c), end=' ')
    print('X' if c > 1 else '=', end=' ')
    soma *= c
print(soma)
