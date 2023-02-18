sal = float(input('Quanto é o salário do funcionário? R$ '))
if sal <= 1250:
    aum = (sal * 15 / 100) + sal
else:
    aum = (sal * 10 / 100) + sal
print('O funcionário que ganhava R${:.2f}, agora passará a ganhar R${:.2f}!'.format(sal, aum))