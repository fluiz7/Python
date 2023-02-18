def mat1(n):
    return n[0][0]


def mat2(n):
    dp = n[0][0] * n[1][1]
    ds = n[0][1] * n[1][0]
    det = dp - ds
    return det


def mat3(n):
    dp = n [0][0] * n[1][1] * n[2][2]
    dp += n [0][1] * n[1][2] * n[2][0]
    dp += n [0][2] * n[1][0] * n[2][1]
    ds = n [0][0] * n[1][2] * n[2][1]
    ds += n [0][1] * n[1][0] * n[2][2]
    ds += n [0][2] * n[1][1] * n[2][0]
    det = dp - ds
    return det


m = eval(input())

if len(m) == 1:
    print(mat1(m))
elif len(m) == 2:
    print(mat2(m))
else:
    print(mat3(m))
