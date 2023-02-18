from Exercícios.Q115.arquivo import *
from time import sleep

arq = 'cadastrados.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerarquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        formatar('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        # Opção de sair do sistema.
        formatar('Saindo do sistema... Até logo!')
        break
    else:
        # Digitou uma opção errado no menu.
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
