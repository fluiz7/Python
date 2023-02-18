from time import sleep
pri = float(input('Primeiro número: '))
seg = float(input('Segundo número: '))
opc = True
while opc:
    sleep(0.5)
    opc = int(input('''
O que você deseja fazer com eles?
----//---------//--------//--------
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do programa
----//---------//--------//--------
Sua opção: '''))
    if opc == 1:
        print('A soma de {} + {} é igual a {}'.format(pri, seg, pri + seg))
    elif opc == 2:
        print('A multiplicação entre {} X {} é {}'.format(pri, seg, pri * seg))
    elif opc == 3:
        if pri > seg:
            print('O primeiro({}) é maior que o segundo({})!'.format(pri, seg))
        elif seg > pri:
            print('O segundo({}) é maior que o primeiro({})!'.format(seg, pri))
        else:
            print('Ambos os números são iguais!!')
    elif opc == 4:
        pri = float(input('Primeiro número: '))
        seg = float(input('Segundo número: '))
    elif opc == 5:
        opc = False
    else:
        print('Número errado! Tente uma das opcões, por favor!!')
print('Só um segundo, estamos finalizando...')
sleep(1)
