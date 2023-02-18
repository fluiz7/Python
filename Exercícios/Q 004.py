# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 22:58:02 2021

@author: wwwlu
"""

print('Vamos descobrir algumas coisas!')
a = input('Digite algo: ')
print("O tipo primitivo desse valor é ", type(a))
print("Só tem espaços? ", a.isspace())
print('Só tem números? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está em maiúsculas?', a.isupper() )
print('Está em minúsculas?', a.islower())
print('Está capitalizada? ', a.istitle())