#catopo = float(input('Qual o comprimento do cateto oposto? '))
#catadj = float(input('Qual o comprimento do cateto adjacente? '))
#hipo = (catopo ** 2 + catadj ** 2) ** (1/2)
#
#print('A hipotenusa vai medir: {:.2f}.' .format(hipo))

import math

catopo = float(input('Qual o comprimento do cateto oposto? '))
catadj = float(input('Qual o comprimento do cateto adjacente? '))
hipo = math.hypot(catopo, catadj)
print('A hipotenusa vai medir: {:.2f}.' .format(hipo))