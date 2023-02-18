from Módulos.uteis import numeros

num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat} e seu dobro é {numeros.dobro(num)}')
