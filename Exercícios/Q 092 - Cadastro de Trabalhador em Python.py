from datetime import datetime

cadastro = dict()
atual = datetime.today().year

cadastro['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de nascimento: '))
cadastro['idade'] = atual - nascimento
cadastro['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if cadastro['ctps'] != 0:
    cadastro['contratação'] = int(input('Ano de Contratação: '))
    cadastro['salário'] = float(input('Salário: R$'))
    cadastro['aposentadoria'] = cadastro['contratação'] - nascimento + 35
print('-=-' * 15)

for k, v in cadastro.items():
    print(f'- {k} é igual a {v}')
