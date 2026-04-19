import sys
n,m =list(map(int,sys.stdin.readline().strip().split()))
li2 = [[[-1,-1,-1,-1] for i in range(n)] for i in range(n)]
maps = []
bn = 0
for i in range(n):
    maps.append(sys.stdin.readline().strip())
    for j in range(n):
        if(maps[i][j] == 'L'):
            pl = [i,j]
bangs = [[1,0],[0,-1],[-1,0],[0,1]]
def dp(pos,bang,bn):

    if(li2[pos[0]][pos[1]][bn] != -1):
        return li2[pos[0]][pos[1]][bn]

    i =0
    r =0
    if(bang[0] == 0): i = 1
    if(pos[i] == (n-1)*(bang[i]==1)):
        r = 0
    else:
        pos[i]+=bang[i]
        if(maps[pos[0]][pos[1]] == 'X'):
            r = 0
        else:
            r = dp(pos,bang,bn)+1
        pos[i]-=bang[i]


    li2[pos[0]][pos[1]][bn] = r
    return r
pos = pl[:]
for i in range(m):
    inp = sys.stdin.readline().strip()
    if(inp == "L"):
        bn +=1
    else:
        bn +=-1
    bn = (bn+4)%4

    bang = bangs[bn]
    ii =0 
    if(bang[0] == 0): ii = 1
    #print(pos)
    pos[ii] += bang[ii]*dp(pos,bang,bn)
    #print(pos)

a = n
pl = pos+[bn]
m = maps
if(pl[2] == 0):
    for i in range(a):
        for j in range(a):
            if(i == pl[0] and j == pl[1]):
                print("L",end = '')
            elif(m[i][j] == "X"):
                print("X",end = '')
            else:
                print(".",end = '')
        print()
elif(pl[2] == 3):
    for j in range(a):
        for i in range(a-1,-1,-1):
            if(i == pl[0] and j == pl[1]):
                print("L",end = '')
            elif(m[i][j] == "X"):
                print("X",end = '')
            else:
                print(".",end = '')
        print()
elif(pl[2] == 2):
    for i in range(a-1,-1,-1):
        for j in range(a-1,-1,-1):
            if(i == pl[0] and j == pl[1]):
                print("L",end = '')
            elif(m[i][j] == "X"):
                print("X",end = '')
            else:
                print(".",end = '')
        print()
elif(pl[2] == 1):
    for j in range(a-1,-1,-1):
        for i in range(a):
            if(i == pl[0] and j == pl[1]):
                print("L",end = '')
            elif(m[i][j] == "X"):
                print("X",end = '')
            else:
                print(".",end = '')
        print()