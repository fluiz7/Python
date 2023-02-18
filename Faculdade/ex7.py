n = int(input())
fib = []

ant = soma = 0
atu = pro = 1

while ant <= n:
    fib.append(ant)
    soma += ant
    ant = atu
    atu = pro
    pro = ant + atu

print(fib, soma)