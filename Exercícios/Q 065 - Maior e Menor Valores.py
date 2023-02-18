n = float(input('Digite um número: '))
cont = 1
media = 0
maior = menor = n
opc = ''
while opc != 'N':
    media += n
    opc = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if opc in 'Ss':
        n = float(input('Digite um número: '))
        cont += 1
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    elif opc in 'Nn':
        opc = 'N'
    else:
        print('Digite uma das letras solicitadas!')
print('Você digitou {} números e a média entre eles é de {}.'.format(cont, media/cont))
print('O maior valor é {}, enquanto o menor é {}.'.format(maior, menor))

# resp = 'S'
# soma = quant = media = maior = menor = 0
# while resp in 'Ss':
#     num = int(input('Digite um número: '))
#     soma += num
#     quant += 1
#     if quant == 1:
#         maior = menor = num
#     else:
#         if num > maior:
#             maior = num
#         if num < menor:
#             menor = num
#     resp = str(input('Quer continuar: [S/N] ')).upper().strip()[0]
# print('Você digitou {} números e a média foi {}'.format(quant, media))
# print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
