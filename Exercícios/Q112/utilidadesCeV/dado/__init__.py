def leiadinheiro(valor):
    while True:
        money = input(valor).strip()
        if money.isnumeric():
            return float(money)
        if '.' in money:
            if money[money.index('.')+1:].isdecimal():
                return float(money)
        if ',' in money:
            if money[money.index(',')+1:].isdecimal():
                a = money.replace(',', '.')
                return float(a)
        print(f'\033[1;31mErro! O termo "{money}" não é válido!\033[m')


def leiadinheiroo(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
