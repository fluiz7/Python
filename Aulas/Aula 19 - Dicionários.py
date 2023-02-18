# pessoas = {'nome': 'Luiz', 'sexo': 'M', 'idade': 20}
# print(f'O {pessoas["nome"]}, do sexo {pessoas["sexo"]}, tem {pessoas["idade"]} anos!')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# print(pessoas)
# del pessoas['idade']
# pessoas['nome'] = 'Lord F.'
# pessoas['anos'] = '21'
# for k, v in pessoas.items():
#     print(f'Chaves {k}')
#     print(f'valores {v}')
#     print(f'{k} = {v}')
# brasil = []
# estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
# brasil.append(estado1)
# brasil.append(estado2)
#
# print(brasil[1]['sigla'])
estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k}: {v}')
