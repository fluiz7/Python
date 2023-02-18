maior = homem = mulher = 0
print('-='*13)
print('  ANALISADOR DE GRUPOS')
while True:
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = q = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo[M/F]: ')).strip()[0]
    while q not in 'SsNn':
        print('-'*25)
        q = str(input('Quer continuar[S/N]: ')).strip()[0]
    if idade >= 18:
        maior += 1
    elif sexo in 'Mm':
        homem += 1
    elif sexo in 'Ff' and idade < 20:
        mulher += 1
    if q in 'Nn':
        break
print(f'\033[1;31mENCERRANDO A ANÁLISE!!\033[m Ao total tivemos:\n{maior} pessoas maiores de 18 anos;\n{homem} Homens'
      f' cadastrados;\n{mulher} Mulher(es) com menos de 20 anos. ')
