nome = str(input('Qual é o seu nome? '))
# estrutura condicional aninhada - uma dentro da outra.
if nome == 'Luiz':
    print('Que belo nome, rapaz!')
elif nome == 'Felipe' or nome == 'Maria' or nome == 'João':
    print('Seu nome é muito famoso no Brasil!')
elif nome in 'Maria Ana Clara Jéssica':
    print('Você tem um nome feminino muito bonito!')
else:
    print('Nome mais comum, hein.')
print('Tenha um bom dia, {}!'.format(nome))
