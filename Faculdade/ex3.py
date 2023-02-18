vet1 = eval(input())
vet2 = eval(input())
soma = 0
tam = len(vet1)
for n in range(tam):
    soma += vet1[n] * vet2[n]
print(soma)
