v1 = eval(input())
v2 = eval(input())

if len(v1) > len(v2):
    m = len(v2)
else:
    m = len(v1)

for i in range(m):
    if v1[i] == v2[i]:
        log = True
        break
    else:
        log = False

print(log)
