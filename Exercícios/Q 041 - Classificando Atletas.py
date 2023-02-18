from datetime import date

nasc = int(input('Ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

print('O atleta possui {} anos em {}.'.format(idade, ano))
if idade <= 9:
    print('Classificação: \033[4;32mMIRIM\033[m')
elif 9 < idade <= 14:
    print('Classificação: \033[4;34mINFANTIL\033[m')
elif 14 < idade <= 19:
    print('Classificação: \033[4;33mJUNIOR\033[m')
elif 19 < idade <= 25:
    print('Classificação: \033[4;35mSÊNIOR\033[m')
else:
    print('Classificação: \033[4;31mMASTER\033[m')
