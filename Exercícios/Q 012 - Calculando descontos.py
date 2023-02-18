# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:10:14 2021

@author: wwwlu
"""

ori = float(input('Quanto custa o produto que você quer mesmo? R$'))
des = ori - (ori * 5 / 100)

print('O produto que antes custava R${:.2f}, agora com desconto de 5% custará apenas \
R${:.2f}!'. format(ori, des))