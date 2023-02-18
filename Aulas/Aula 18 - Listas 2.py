# teste = list()
# teste.append('Luiz')
# teste.append(20)
# galera = []
# galera.append(teste[:])
# teste[0] = 'Larissa'
# teste[1] = '19'
# galera.append(teste[:])
# print(galera)
#
# galera = [['Luiz', 20], ['Larissa', 19], ['Felipe', 24], ['Jõao', 22]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade!')
#
galera = []
dados = []
maior = menor = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade!')
        menor += 1

print(f'Temos {maior} maiores de idade e {menor} menores.')
