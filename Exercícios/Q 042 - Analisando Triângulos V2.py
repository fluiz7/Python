a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))

if a + b > c and b + c > a and a + c > b:
    if a != b != c != a:
        print('As retas acima \033[4;32mPODEM FORMAR\033[m um triângulo \033[4;35mESCALENO\033[m!')
    # elif (a == b or a == c or b == c) and (a != b or a != c or b != c):
        # print('As retas acima \033[4;32mPODEM FORMAR\033[m um triângulo \033[4;33mISÓSCELES\033[m!')
    elif a == b == c:
        print('As retas acima \033[4;32mPODEM FORMAR\033[m um triângulo \033[4;34mEQUILÁTERO\033[m!')
    else:
        print('As retas acima \033[4;32mPODEM FORMAR\033[m um triângulo \033[4;33mISÓSCELES\033[m!')
else:
    print('As retas acima \033[4;31mNÃO PODEM\033[m formar um triângulo!')
