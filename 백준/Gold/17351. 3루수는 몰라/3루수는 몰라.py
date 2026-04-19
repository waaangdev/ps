import sys
from collections import deque

n = int(input())
maps = [[] for i in range(n)]

for i in range(n):
    maps[i] = sys.stdin.readline().strip()

q = deque([[0,0,0+1*(maps[0][0]=='M')]])
dp = [[-1 for i in range(n)] for i in range(n)]
while q:
    lenq = len(q)
    for _ in range(lenq):
        qpop = q.popleft()
        for i in [[0,1],[1,0]]:
            nx = qpop[0]+i[0]
            ny = qpop[1]+i[1]
            if(nx < n and ny < n):
                nxy = nx
                if((maps[nx][ny] == "MOLA"[qpop[2]%4])):
                    dum =qpop[2]+1
                else:
                    dum =qpop[2]//4*4+1*(maps[nx][ny]=='M')

                if(dp[nx][ny] < dum):
                    dp[nx][ny ] = dum
                    q.append([nx,ny,dum])
print(max(0,dp[n-1][n-1])//4)