not1 = float(input('Primeira nota: '))
not2 = float(input('Segunda nota: '))
med = (not1 + not2)/2
if med < 5:
    print('Sua média é {:.1f}.\nVocê está \033[1;31mREPROVADO\033[m!'.format(med))
elif 5 <= med < 7:
    print('Sua média é {:.1f}.\nVocê está em \033[1;33mRECUPERAÇÂO\033[m!'.format(med))
elif med >= 7:
    print('Sua média é {:.1f}.\nVocê está \033[1;32mAPROVADO\033[m!'.format(med))
