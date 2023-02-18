jog = dict()
goals = list()
cadas = []
maiorn = maiorl = 0
while True:
    jog['nome'] = str(input('Nome do jogador: ')).strip().title()
    if len(jog['nome']) > maiorn:
        maiorn = len(jog['nome'])
    part = int(input(f'Quantas partidas {jog["nome"]} jogou? '))
    for c in range(1, part+1):
        goals.append(int(input(f'  Quantos gols na partida {c}? ')))
    if len(goals) > maiorl:
        maiorl = len(goals)
    jog['gols'] = goals[:]
    jog['total'] = sum(goals)
    while True:
        q = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if q in 'SN':
            break
        print('Erro! Digite S ou N!')
    cadas.append(jog.copy())
    goals.clear()
    if q == 'N':
        break
print('-=-' * 20)
print(f'{"cod":3}', f'{"nome":{maiorn+5}}', f'{"gols":{maiorl*2}}', f'{"total":>{maiorl * 3 + 3}}')
print('-' * 50)
for i, j in enumerate(cadas):
    print(f'{i:3}', f'{j["nome"]:{maiorn+5}}', f'{str(j["gols"]):{maiorl*4}}', f'{j["total"]:{maiorl}}')
print('-' * 50)
while True:
    dad = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if dad == 999:
        break
    else:
        if 0 <= dad < len(cadas):
            print(f'-- LEVANTAMENTO DO JOGADOR {cadas[dad]["nome"]}: ')
            for num, g in enumerate(cadas[dad]['gols']):
                print(f'   No jogo {num+1} fez {g} gols.')
            print('-' * 42)
        else:
            print(f'CÓDIGO INVÁLIDO! Não há jogador com código {dad}!')
print('-=' * 25)
print(' <<< VOLTE SEMPRE >>>')
