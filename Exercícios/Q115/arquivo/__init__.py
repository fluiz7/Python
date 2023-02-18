from Exercícios.Q115.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo!')
    else:
        formatar('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at', encoding='utf-8')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()


def maiornome():
    tam = 0
    a = open('cadastrados.txt', 'r', encoding='utf=8')
    b = a.readlines()
    for linha in b:
        if len(linha) > tam:
            tam = len(linha)
    a.close()
    return tam


maiornome()
