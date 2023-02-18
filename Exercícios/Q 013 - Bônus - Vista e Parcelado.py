# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:32:09 2021

@author: wwwlu
"""

print('Aqui na nossa loja temos desconto de 10% à vista e juros de 20% parcelado. ')
ori = float(input('Quanto custa o produto que você está interessado? R$'))
vista = ori - (ori * 10 / 100)
parcelado = ori + (ori * 20 / 100)

print('Sendo assim, o produto que custa R${:.2f}, poderá ser levado por este valor \
em 1x no cartão, R${:.2f} à vista ou R${:.2f} parcelado.' . format(ori, vista, parcelado))