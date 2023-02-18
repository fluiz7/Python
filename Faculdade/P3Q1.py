def arctan(x, n):
    arc = x
    for i in range(1, n+1):
        p = 2*i+1
        if i % 2 == 0:
            arc += x**p/p
        else:
            arc -= x**p/p
    return arc


num = float(input())
ter = int(input())
print(arctan(num, ter))