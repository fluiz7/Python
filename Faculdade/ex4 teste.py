m1 = eval(input())
m2 = eval(input())

if type(m1[0]) == int:
    m1 = [m1]
if type(m2[0]) == int:
    m2 = [m2]

if len(m1[0]) == len(m2):
    for i in range(len(m1)):
        for j in range(len(m2)):
            for k in range(len(m1[0])):
                print(m1[i][k], m2[k][j])

else:
    print('Erro!')