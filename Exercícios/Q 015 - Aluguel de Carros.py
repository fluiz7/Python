# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 11:54:08 2021

@author: wwwlu
"""

dias = int(input('Há quantos dias está alugado com você? '))
km = float(input('Quantos quilômetros você percorreu? '))

preçokm = km * 0.15
preçodias = dias * 60
total = preçokm + preçodias

print('O total a pagar é de R${:.2f}'. format(total))