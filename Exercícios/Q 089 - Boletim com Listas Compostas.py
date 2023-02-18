from time import sleep
dados = []
alunos = []
cont = 0

print('-=' * 30)
print(f'{"CONSULTA DE BOLETIM":^60}')
print('-=' * 30)

while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    alunos.append(dados[:])
    alunos[cont].append((alunos[cont][1] + alunos[cont][2])/2)
    dados.clear()
    while True:
        q = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if q in 'SN':
            break
        else:
            print('Tente de novo! ', end='')
    if q == 'N':
        break
    cont += 1

print('-=' * 30, '\n', '=' * 20)
print(f'{"BOLETIM":^20}')
print('='*20)
print(f'{"Nº.":3}', f'{"Nome":10}', f'{"Média":3}')
for n, a in enumerate(alunos):
    print(f'{n:<3}', f'{a[0]:10}', f'{a[3]:<3}')
print('-=' * 10)

while True:
    c = int(input('Mostrar notas de qual aluno? (999 Interrompe!) '))
    if c == 999:
        break
    if c >= len(alunos):
        print('Tente de novo! ', end='')
    else:
        print(f'As notas do aluno {alunos[c][0]} são {alunos[c][1:3]}')

print('-' * 30)
print('Finalizando...')
sleep(1)
print('ENCERRADO! VOLTE SEMPRE!!')
