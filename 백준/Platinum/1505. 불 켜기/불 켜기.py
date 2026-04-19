import sys
#from collections import deque


n,m =map(int,sys.stdin.readline().split())
maps = [[2 for i in range(m+2)] for i in range(n+2)]
for i in range(n):
    inp=sys.stdin.readline()
    for j in range(m):
        maps[i+1][j+1] =((inp[j]=='.')*1)


def dp(idx):
    i,j = idx//(m+2),idx%(m+2)
    # print(idx,i,j)
    # for i2 in range(n+2):
    #     print(maps[i2])
    if(j < 2):
        if(i == 2):
            if(sum(map(lambda x:x-(x==2)*2,maps[1][1:m+1]+maps[2][1:3])) == 0):
                return 0
            else:
                return -1
        if(maps[i][j] == 1):
            return -1
        else:
            return dp(idx-1)

    rr = 100
    if(maps[i][j] != 0):
        for i2 in range(0,-3,-1):
            for j2 in range(0,-3,-1):
                maps[i+i2][j+j2] = [1,0,2][(maps[i+i2][j+j2])]
        dum = dp(idx-1)
        if(dum != -1):rr = min(rr,dum+1)
        for i2 in range(0,-3,-1):
            for j2 in range(0,-3,-1):
                maps[i+i2][j+j2] = [1,0,2][(maps[i+i2][j+j2])]
    if(maps[i][j] != 1):
        dum = dp(idx-1)
        if(dum != -1):rr = min(rr,dum)
    
    if(rr==100):rr=-1
    return rr

r = dp((n+2)*(m+2)-1)
if(r==-1):
    print(-1)
else:
    print(r)