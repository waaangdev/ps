import sys
from collections import deque

# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline())
m = []
for i in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))
m2 = [[[0,0] for i in range(n)] for i in range(n)]
dum = 1
for i in range(n):
    for j in range(n):
        if(m[i][j]==1):
            q=deque([[i,j]])
            dum+=1
            m[i][j] = dum
            while(q):
                qpop=q.popleft()
                for k in [[0,1],[1,0],[0,-1],[-1,0]]:
                    qpop2 = [qpop[0]+k[0],qpop[1]+k[1]]
                    if(qpop2[0]>=0 and qpop2[0] < n and qpop2[1]>=0 and qpop2[1] < n):
                        if(m[qpop2[0]][qpop2[1]]==1):
                            m[qpop2[0]][qpop2[1]] = dum
                            q.append(qpop2)
#print(m)
q = deque([])
for i in range(n):
    for j in range(n):
        if(m[i][j]>=2):
            m2[i][j]=[m[i][j],0]
            q.append([i,j])
r = 1000
while (q):
    #print(q)
    qpop=q.popleft()
    for k in [[0,1],[1,0],[0,-1],[-1,0]]:
        qpop2 = [qpop[0]+k[0],qpop[1]+k[1]]
        if(qpop2[0]>=0 and qpop2[0] < n and qpop2[1]>=0 and qpop2[1] < n):
            if(m2[qpop2[0]][qpop2[1]][0] == 0):
                m2[qpop2[0]][qpop2[1]] = m2[qpop[0]][qpop[1]][:]
                m2[qpop2[0]][qpop2[1]][1]+=1
                q.append(qpop2)
            elif(m2[qpop2[0]][qpop2[1]][0]!=m2[qpop[0]][qpop[1]][0]):
                r = min(r,m2[qpop2[0]][qpop2[1]][1]+m2[qpop[0]][qpop[1]][1])
                
print(r)