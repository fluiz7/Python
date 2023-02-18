cad = dict()
lista = list()
cad['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {cad["nome"]} jogou? '))
print('-' * 35)
for c in range(0, partidas):
    lista.append(int(input(f'Quantos gols na partida {c}? ')))
cad['gols'] = lista[:]
cad['total'] = sum(lista)
print('-=' * 25)
print(cad)
print('-=' * 25)
for k, v in cad.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 20)
print(f'O jogador {cad["nome"]} jogou {len(cad["gols"])} partidas.')
for i, v in enumerate(cad['gols']):
    print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {cad["total"]} gols!')
