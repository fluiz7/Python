from time import sleep

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
           'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenovo', 'vinte')
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros[num]}')
        while True:
            prox = str(input('Quer continuar[S/N]: ')).strip().upper()[0]
            if prox in 'SsNn':
                break
        if prox == 'N':
            break
    else:
        print('Tente novamente!', end=' ')
print('ENCERRANDO!!...')
sleep(1)
