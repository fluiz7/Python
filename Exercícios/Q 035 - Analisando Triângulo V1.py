a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a + b > c and a + c > b and b + c > a:
    print('As retas acima PODEM FORMAR um triângulo!')
else:
    print('As retas acima NÂO PODEM FORMAR um triângulo!')
