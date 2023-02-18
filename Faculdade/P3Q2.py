def caminho_diagonal(m):
    cam = []; pos = 0
    for i, x in enumerate(m):
        for j, y in enumerate(x):
            if j == pos:
                if y == 0:
                    cam.append((i, j))
                    if j == len(x)-1:
                        pos = j
                    else:
                        pos = j+1
                if y == 1:
                    if len(cam) >= 2:
                        pos = j-1
                    if m[i][j-1] == 2:
                        pos = cam[-1][-1]
                    break
                if y == 2:
                    if m[i][j-1] == 2:
                        pos = cam[-1][-1]
                        break
                    pos = j+1
                    continue
            else:
                continue
    if cam[-1] == (len(m)-1, len(m[0])-1) and cam[0] == (0, 0):
        return cam
    return False


print(caminho_diagonal([[0,0,1],[0,1,0],[0,0,0]]))
print(caminho_diagonal([[0,0,1,1],[1,0,0,0],[0,1,1,0]]))
print(caminho_diagonal([[0,0],[1,1]]))
print(caminho_diagonal([[2,0],[0,0]]))
print(caminho_diagonal([[0,0],[0,2]]))
print(caminho_diagonal([[0,2,0],[1,0,0]]))
print(caminho_diagonal([[0,2,1],[1,0,0]]))
print(caminho_diagonal([[0,1,2,0],[0,2, 2, 0]]))
print(caminho_diagonal([[0,1,2,0],[2,2, 2, 0], [0, 2, 0, 0]]))
