def caminho_diagonal1(m):
    
    nlinhas,ncolunas = len(m),len(m[0])
    
    def cd (i,j):
        if m[i][j] != 0: return False
        if i+1 == nlinhas and j+1 == ncolunas: return [(i,j)]
        down = left = False
        if i+1 < nlinhas:
            tmp = cd(i+1,j)
            if tmp: down = [(i,j)]+tmp
        
        if j+1 < ncolunas:
            tmp = cd(i,j+1)
            if tmp: left = [(i,j)]+tmp
        return down or left
    
    return cd(0,0)

def caminho_diagonal2(m):
    
    nlinhas,ncolunas = len(m),len(m[0])
    q = [((0,0),1)]
    s = []
    achou = False
    while not q == []:
        t,l = q.pop()
        i,j = t
        if m[i][j] != 0: continue
        if len(s) >= l: s = s[:l-1]
        s += [(i,j)]
        if i+1 == nlinhas and j+1 == ncolunas: 
            achou = True
            break
        #down = left = False
        if j+1 < ncolunas:
            q.append(((i,j+1),l+1))
            #tmp = cd(i,j+1)
            #if tmp: return left = [(i,j)]+tmp
            
        if i+1 < nlinhas:
            q.append(((i+1,j),l+1))
            #tmp = cd(i+1,j)
            #if tmp:  return down = [(i,j)]+tmp
    if achou == False: return False
    return s

print (caminho_diagonal1([[0,0,1],
                         [0,1,0],
                         [0,0,0]]))
print (caminho_diagonal1([[0,0,1,1],
                         [1,0,0,0],
                         [0,1,1,0]]))
print (caminho_diagonal1([[0,0],[1,1]]))

print (caminho_diagonal2([[0,0,1],
                         [0,1,0],
                         [0,0,0]]))
print (caminho_diagonal2([[0,0,1,1],
                         [1,0,0,0],
                         [0,1,1,0]]))
print (caminho_diagonal2([[0,0],[1,1]]))