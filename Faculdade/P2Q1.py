def multimat(a, b):
    la, ca, lb, cb = len(a), len(a[0]), len(b), len(b[0])
    if ca == lb:
        s = [[0 for x in range(cb)] for y in range(la)]
        for i in range(la):
            for k in range(cb):
                for j in range(ca):
                    s[i][k] += a[i][j] * b[j][k]
    else:
        s = [[0 for x in range(lb)] for y in range(cb)]
        for i in range(cb):
            for j in range(lb):
                s[i][j] = b[j][i]
        b = s
        return multimat(a, b)
    return s


mat1 = eval(input())
mat2 = eval(input())
print(multimat(mat1, mat2))