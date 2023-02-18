pes = dict()
cad = list()
media = 0
while True:
    print('-=' * 15)
    pes['nome'] = str(input('Nome: ')).strip().title()
    while True:
        pes['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()[0]
        if pes['sexo'] in 'MF':
            break
        print('ERRO! Digite M ou F!')
    pes['idade'] = int(input('Idade: '))
    media += pes['idade']
    q = str(input('Quer continuar? [S/N]: ')).strip()[0]
    while q not in 'SsNn':
        q = str(input('ERRO! Digite S ou N: ')).strip()[0]
    cad.append(pes.copy())
    if q in 'Nn':
        break
print('-=-' * 20)
print(f'A) Ao todo temos um total de {len(cad)} pessoas cadastradas!')
media /= len(cad)
print(f'B) A média de idade dos cadastros é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for c in cad:
    if c['sexo'] == 'F':
        print(c['nome'], end='; ')
print()
print(f'D) Lista de pessoas que estão acima da média:')
for p in cad:
    if p['idade'] >= media:
        print('     ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end=' ')
        print()
print('-=' * 30)
print('<<< ENCERRADO >>>')
