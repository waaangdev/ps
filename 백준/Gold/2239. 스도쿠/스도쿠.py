import sys

m = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(9)]

def sol(x,y):
    if(x==9): return sol(0,y+1)
    if(y==9): return 1
    if(m[y][x] != 0): return sol(x+1,y)
    
    sets = set(range(1,10))
    for i in range(9):
        if(m[i][x] in sets):sets.remove(m[i][x])
    for i in range(9):
        if(m[y][i] in sets):sets.remove(m[y][i])
    for i in range(3):
        for j in range(3):
            if(m[y-y%3+i][x-x%3+j] in sets):sets.remove(m[y-y%3+i][x-x%3+j])
    sets=(list(sets))
    for i in sets:
        m[y][x]=i
        if(sol(x+1,y)):
            return 1
    m[y][x]=0
    return 0
        
sol(0,0)
for i in range(9):
    print(''.join(list(map(str,m[i]))))
