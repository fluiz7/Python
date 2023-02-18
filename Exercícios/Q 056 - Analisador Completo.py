media = velho = mulher = 0
nombre = ''
for p in range(1, 5):
    print('{:-^26} '.format('{}ª PESSOA'.format(p)))
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): ')).upper().strip()
    media += idade
    if sexo == 'M' and idade >= velho:
        velho = idade
        nombre = nome
    elif sexo == 'F' and idade < 20:
        mulher += 1
print('A idade média do grupo é de {} anos!'.format(media/4))
print('O homem mais velho tem {} anos e se chama {}.'.format(velho, nombre))
print('No grupo há {} mulher(es) menor(es) que 20 anos!'.format(mulher))
