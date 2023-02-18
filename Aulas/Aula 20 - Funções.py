def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


# Programa Principal
soma(b=4, a=5)
# Se não explicitar ele fará uma cópia dos valores na ordem digitada.


def contador(* num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')


def numerador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números!')


contador(2, 1, 7)
numerador(7, 1, 2)
contador(8, 0)
numerador(0, 8)
contador(4, 4, 7, 6, 2)
numerador(2, 6, 7, 4, 4)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [4, 7, 9, 5, 6, 3, 8]
dobra(valores)
print(valores)
