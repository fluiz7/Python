# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:54:30 2021

@author: wwwlu
"""

print('Vamos descobrir as dimensões de sua parede e quanto de tinta você \
precisará para pintá-la!')

lar = float(input('Quantos metros tem a largura de sua parede? '))

alt = float(input('E a altura? '))

area = lar * alt

print('Sua parede possui as dimensões de {}m x {}m, o que dá uma área de {}m².\
Levando em consideração que um litro de tinta pinta 2m², você precisará \
de {} litros de tinta para pintar sua parede.'. format(lar, alt, area, area/2))
