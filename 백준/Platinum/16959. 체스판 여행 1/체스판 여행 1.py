"체스판 여행 1"

import sys
from collections import deque

n = int(sys.stdin.readline())
point = [[] for i in range((n*n)//2)]
m = []
for i in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))
    for j in range(n):
        if(m[i][j] == 1):
            q = deque([[i,j,0,0,1],[i,j,1,0,1],[i,j,2,0,1]])

ang = [[[-1,0],[0,1],[1,0],[0,-1]],[[-1,-1],[-1,1],[1,1],[1,-1]]]
bang = [[[[-1 for i in range(n)] for i in range(n)] for i in range(3)] for i in range(n*n)]

t = 0
br= 0
while q:
    t += 1
    for i in range(len(q)):
        qpop = q.popleft()
        for j in range(4):
            for k in range(1*(qpop[2] < 2),n+1+(-(n+1)+2)*(qpop[2] == 2)):
                dum1 = qpop[0]+ang[0][j][0]+ang[1][(j+k)%4][0]
                dum2 = qpop[1]+ang[0][j][1]+ang[1][(j+k)%4][1]
                if((qpop[2] < 2)):
                    dum1 = qpop[0]+ang[qpop[2]][j][0]*k
                    dum2 = qpop[1]+ang[qpop[2]][j][1]*k
                if(dum1 > -1 and dum1 < n and dum2 > -1 and dum2 < n):
                    if(bang[qpop[3]][qpop[2]][dum1][dum2] == -1):
                        bang[qpop[3]][qpop[2]][dum1][dum2] = t
                        if(m[dum1][dum2]-1 == qpop[3]+1):
                            q.append([dum1,dum2,qpop[2],qpop[3]+1,0])
                            
                            if(qpop[3]+1 == n*n-1):
                                br= 1
                                break
                        else:
                            q.append([dum1,dum2,qpop[2],qpop[3],0])
        if(br):
            break
        if(qpop[4] == 0):
            for j in range(3):
                if(j != qpop[2]):
                    if(bang[qpop[3]][j][qpop[0]][qpop[1]] == -1):
                        q.append([qpop[0],qpop[1],j,qpop[3],1])
    if(br):
        break
print(t)