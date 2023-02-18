# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:44:37 2021

@author: wwwlu
"""

print('Vamos converter um valor em metros para centímetros e milímetros!')
m = float(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000

print('Convertendo, temos que {:.2f}m é igual a {:.0f}mm, {:.0f}cm, {:.0f}dm, {}dam, {}hm e {}km.' .format(m, mm, cm, dm, dam, hm, km))