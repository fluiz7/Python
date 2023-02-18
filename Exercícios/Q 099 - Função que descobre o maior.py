def maior(*num):
    print('-=' * 25)
    print('Analisando os valores passados...')
    mai = 0
    for i, c in enumerate(num):
        if i == 0:
            mai = c
        if c >= mai:
            mai = c
        print(c, end=' ')
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {mai}.')


# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
maior(-7, -2, -5, -4, -10)
