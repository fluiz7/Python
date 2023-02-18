def buscabin(v,x):
    i = 0
    j = len(v) - 1
    while True:
        if i > j:
            return -1
        m = int((i+j)/2)
        if v[m] < x: i = m+1
        if v[m] > x: j = m-1
        if v[m] == x:
            return m


def ordenar(l):
    v = [0]
    for x in l:
        print(v, x)
        n = buscabin(v, x)
        if x > v[n]:
            v.append(x)
        elif x < v[n]:
            for y in range(len(v)-1,-1,-1):
                if v[y] < x:
                    v.insert(y+1, x)
                    break
                if y == 0:
                    v.insert(y,x)
                    break
        else:
            v.insert(n, x)
    del v[buscabin(v, 0)]
    return v


l = [3,-1,101,7,9,0]
print(ordenar(l))

######################

def buscabin(v,x):
    i = 0
    j = len(v) - 1
    while True:
        if i > j:
            return -1
        m = int((i+j)/2)
        if v[m] < x: i = m+1
        if v[m] > x: j = m-1
        if v[m] == x:
            return m


def ordenar(l):
    v = []
    for x in l:
        n = buscabin(v,x)
        if v == [] or n != -1:
            v.insert(n,x)
        else:
            for num, y in enumerate(v):
                print(v)
                if x < y:
                    v.insert(num, x)
                    break
                elif x > v[-1]:
                    v.append(x)
                    break
    return v


l = eval(input())
print(ordenar(l))