import datetime
gen = input('Qual o seu gênero? (M/F) ').upper().strip()
if gen != 'F' and gen != 'M':
    print('Digite M ou F, por favor!')
elif gen == 'F':
    print('Mulheres não fazem o alistamento obrigatório!')
elif gen == 'M':
    nascimento = int(input('Ano de nascimento, amigo: '))
    ano = datetime.date.today().year
    idade = ano - nascimento
    print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
    if idade == 18:
        print('Cara! Você já tem 18 ANOS! Precisa se alistar IMEDIATAMENTE!!')
    elif idade < 18:
        print('Ainda lhe falta {} ano(s) para se alistar.\n'
              'Seu alistamento será em {}!'.format(18-idade, nascimento+18))
    else:
        print('Você deveria ter se alistado há {} ano(s)!\n'
              'Seu alistamento foi em {}!'.format(idade-18, nascimento+18))
