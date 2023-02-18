km = float(input('A quantos Km/h está o carro? '))
if km > 80:
    multa = (km - 80) * 7
    print('Você foi multado!! Você ultrapassou o limite permitido de 80km/h! \n'
          'Seu carro estava há {}km/h e deverá pagar uma multa de R${:.2f}'.format(km, multa))
print('Tenha um bom dia! Se for dirigir, não beba. Dirija com segurança sempre!')
