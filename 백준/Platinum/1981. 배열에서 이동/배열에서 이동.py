import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
maps = []
n = int(sys.stdin.readline())
for i in range(n):
    maps.append(list(map(int,sys.stdin.readline().split())))

s,e = 0,200
m = 0
r = 1000

while(1):
    #print(s,e)
    q = deque([[0,0]])
    dp = [[1 for i in range(n)] for i in range(n)]
    if(s<=maps[0][0]<=e):
        while(q):
            qpop = q.popleft()
            for i in [[0,1],[0,-1],[1,0],[-1,0]]:
                nqpop = [qpop[0]+i[0],qpop[1]+i[1]]
                if(nqpop[0] > -1 and nqpop[0] < n and nqpop[1] > -1 and nqpop[1] < n):
                    if(dp[nqpop[0]][nqpop[1]] and s<=maps[nqpop[0]][nqpop[1]]<=e):
                        dp[nqpop[0]][nqpop[1]] = 0
                        q.append(nqpop)
    if(dp[n-1][n-1]==0):
        #print(s,e)
        r = min(r,e-s)
        if(m==0):
            s+=1
        else:
            e-=1
    else:
        if(m==0):
            s-=1
            e-=1
            m=1
        else:
            s-=1
    if(s==-1):break
print(r)
