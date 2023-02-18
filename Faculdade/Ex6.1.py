def divid(i):
    d = set()
    for x in range(1,i+1):   
        if i % x == 0:
            d.add(x)
    return d


def comum(n):
    while len(n) >= 2:
        a = divid(n[0])
        b = a.intersection(divid(n[1]))
        n = n[1:]
    return b


n = (100,120,50)
print(comum(n))