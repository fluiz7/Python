while True:
    print('-' * 35)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont:2} = {n*cont}')
print('Encerrando a TABUADA V3.0! Obrigado por usar nossos serviços!!')
