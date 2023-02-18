t = int(input("Quantos termos? "))
ant = cont = 0
atual = pro = 1
while cont < t:
    print(ant, end=' -> ')
    ant = atual
    atual = pro
    pro = atual + ant
    cont += 1
print('FIM!')
