def ordem(v):
    if len(v) >= 2:
        min = v[0]
        for i, x in enumerate(v):
            if x <= min:
                min = x
                y = i
        v[y] = v[0]; v[0] = min
        print(v)
        return v[:1] + ordem(v[1:])
    return v    


vet = eval(input())
print(ordem(vet))