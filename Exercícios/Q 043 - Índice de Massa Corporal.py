pes = float(input('Seu peso (Kg): '))
alt = float(input('Sua altura (m): '))
imc = pes / (alt * alt)

print('O IMC dessa pessoa é de {:.1f}. '.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO!')
elif 18.5 <= imc < 25:
    print('Você está com o PESO IDEAL!')
elif 25 <= imc < 30:
    print('Você está com SOBREPESO!')
elif 30 <= imc < 40:
    print('Você tem OBESIDADE!')
else:
    print('Você possui OBESIDADE MÓRBIDA!')
