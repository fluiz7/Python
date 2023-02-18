# n = ''
# while n != 'M' and n != 'F':
#     n = str(input('Qual o sexo a ser informado? [M/F] ')).strip().upper()[0]
#     if n not in 'MF':
#         print('ERRADO! Digite uma das letras sugeridas!!')
#     else:
#         if n == 'M':
#             n = 'M'
#         elif n == 'F':
#             n = 'F'
# print('Muito bem! O sexo {} foi registrado com sucesso!!'.format(n))

n = str(input('Informe um sexo: [M/F] ')).strip().upper()[0]
while n not in 'MmFf':
    n = str(input('Dados inválidos! Digite um dos valores sugeridos: '))
print('Muito bem! Sexo {} registrado com sucesso!'.format(n))
