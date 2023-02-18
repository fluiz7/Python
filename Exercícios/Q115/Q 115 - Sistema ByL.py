from Exercícios.Q115.interface import *
from Exercícios.Q115.arquivo import maiornome
from time import sleep

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        formatar('PESSOAS CADASTRADAS')
        try:
            arquivo = open('cadastrados.txt', 'r', encoding='utf=8')
            texto = arquivo.readlines()
            for frase in texto:
                frase = frase.strip()
                idade = frase.rindex(';') + 1
                print(f'{frase[:idade-1]:{maiornome()+5}}{frase[idade:]} anos')
        except FileNotFoundError:
            arquivo = open('cadastrados.txt', 'a+')
            print('Arquivo cadastrados.txt foi criado com sucesso!')
        arquivo.close()
    elif resp == 2:
        formatar('NOVO CADASTRO')
        nome = input('Nome: ').strip().title()
        anos = leiaint('Idade: ')
        anos = str(anos)
        try:
            arquivo = open('cadastrados.txt', 'r', encoding='utf-8')
            t = arquivo.readlines()
            t.append(f'\n{nome}')
            t.append(f'; {anos}')
            arquivo = open('cadastrados.txt', 'w', encoding='utf-8')
            arquivo.writelines(t)
            arquivo.close()
        except KeyboardInterrupt:
            print('\033[33mO usuário decidiu não fornecer dados!\033[m')
    elif resp == 3:
        formatar('Saindo do Sistema... Até logo!')
        break
    else:
        print(f'{c[1]}ERRO! Digite uma opção válida!{c[0]}')
    sleep(1)
