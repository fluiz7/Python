# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:25:36 2021

@author: wwwlu
"""

sal = float(input('Qual é o salário do funcionário? R$'))
aum = sal + (sal * 15 / 100)

print('Um funcionário que ganhava \033[4;31mR${:.2f}\033[m, com um aumento de 15% passará a ganhar \033[4;32mR${:.2f}\033[m.'\
      . format(sal, aum))
