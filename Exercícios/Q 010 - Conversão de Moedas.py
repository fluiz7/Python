# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 11:51:41 2021

@author: wwwlu
"""

saldo = float(input('Diga quanto dinheiro você tem na carteira? R$'))
conversao = saldo / 5.53
print('Com R${:.2f}, você consegue comprar US${:.2f}.'. format(saldo, conversao))