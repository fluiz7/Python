def pares(n):
    t = []; cont = 0
    while len(n) >= 2 and cont < len(n)-1:
        for x in range(len(n)):
            if n[cont] < n[x] and str((n[cont], n[x])) not in str(t):
                t.append((n[cont], n[x]))
        cont += 1
    return tuple(t)


print(pares(eval(input())))