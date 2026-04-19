import sys
from collections import deque
n,m = map(int,input().split())
maps = [[0 for i in range(m)] for i in range(n)]
bang = [[2000 for i in range(m)] for i in range(n)]
st = [0,0]
ed = [0,0]
for i in range(n):
    inp = sys.stdin.readline()
    for j in range(m):
        if(inp[j] == 'S'):
            st = [i,j]
        elif(inp[j] == 'E'):
            ed = [i,j]
        elif(inp[j] == '#'):
            maps[i][j] = 2
            for k,l in zip([i-1,i+1,i,i],[j,j,j-1,j+1]):
                if(k >= 0 and k < n and l >= 0 and l < m):
                    maps[k][l] = max(maps[k][l],1)

#print(maps)
q = deque([st+[0]])
r = 2000
while (q):
    #print(q)
    qpop = q.popleft()
    for k,l in zip([qpop[0]-1,qpop[0]+1,qpop[0],qpop[0]],[qpop[1],qpop[1],qpop[1]-1,qpop[1]+1]):
        if(k >= 0 and k < n and l >= 0 and l < m):
            dum = qpop[2]+1
            if(maps[k][l] == 1 and maps[qpop[0]][qpop[1]] == 1): dum-=1
            if(bang[k][l] > dum and maps[k][l] != 2):
                bang[k][l] = dum
                if([k,l] == ed):
                    r = min(r,dum)
                if(maps[k][l] == 1 and maps[qpop[0]][qpop[1]] == 1):
                    q.appendleft([k,l,dum])
                else:
                    q.append([k,l,dum])

print(r)