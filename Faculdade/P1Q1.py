def eprimo(n):
    cont = 0
    for x in range(1, n+1):
        if n % x == 0:
            cont += 1
    if cont == 2:
        return True
    return False


def rotacoes(n):
    st = str(n)
    t = len(st)
    if t >= 2:
        for x in range(t):
            st = st[-1] + st[:-1]
            if not eprimo(int(st)):
                return False
    return True


def primoscirculares(n):
    pri = []
    for x in range(1, n+1):
        if eprimo(x):
            if rotacoes(x):
                pri.append(x)
    return pri


print(primoscirculares(int(input())))