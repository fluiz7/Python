pri = float(input('Primeiro número: '))
seg = float(input('Segundo número: '))
if pri > seg:
    print('O \033[4;32mPRIMEIRO\033[m valor é maior!')
elif seg > pri:
    print('O \033[4;31mSEGUNDO\033[m valor é maior!')
else:
    print('Os dois valores são \033[4;35mIGUAIS\033[m!')
