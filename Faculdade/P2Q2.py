def menores(t):
    v, m = t; s, cont = [], 0
    while len(s) < m:
        men = v[cont]
        for x, y in enumerate(v):
            if s.count(y) < v.count(y):
                if y < men:
                    men = y
            else:
                cont = x+1
        s.append(men)
    return s
#Código tá errado e não funcionando direito
            

vet = eval(input())
print(menores(vet))