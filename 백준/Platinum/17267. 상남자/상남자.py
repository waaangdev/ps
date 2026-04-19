"상남자"

import sys
from collections import deque

my,mx = map(int,sys.stdin.readline().split())
p = list(map(int,sys.stdin.readline().split()))
m = [0 for i in range(my)]
bang = [[[p[0]+1,p[1]+1] for i in range(mx)] for i in range(my)]
ang = [[1,0],[-1,0],[0,-1],[0,1]]

for i in range(my):
    m[i] = list(map(int,list(sys.stdin.readline().strip())))
    for j in range(mx):
        if(m[i][j] == 2):
            q = deque([[i,j,0,0]])
            bang[i][j] = [0,0]
            
r = 1
while q:
    qpop = q.popleft()

    for i in range(2):
        if(qpop[2+i] != p[i]):
            dum2 = qpop[1]+ang[i+2][1]
            dum1 = qpop[0]+ang[i+2][0]
            if(dum2 < mx and dum2 > -1 and dum1 < my and dum1 > -1):
                if((bang[dum1][dum2][0] >qpop[2]+1*(i == 0) or bang[dum1][dum2][1] >qpop[3]+1*(i == 1)) and m[dum1][dum2] != 1):
                    q.append([dum1,dum2,qpop[2]+1*(i == 0),qpop[3]+1*(i == 1)])
                    if(bang[dum1][dum2] == [p[0]+1,p[1]+1]):r+=1
                    bang[dum1][dum2] = [min(bang[dum1][dum2][0],qpop[2]+1*(i == 0)),min(bang[dum1][dum2][1],qpop[3]+1*(i == 1))]
    
    for i in range(2):
        for j in range(1,my):
            dum2 = qpop[1]+ang[i][1]*j
            dum1 = qpop[0]+ang[i][0]*j
            if(dum2 < mx and dum2 > -1 and dum1 < my and dum1 > -1):
                if((bang[dum1][dum2][0] >qpop[2]+1*(i == 0) or bang[dum1][dum2][1] >qpop[3]+1*(i == 1)) and m[dum1][dum2] != 1):
                    if(bang[dum1][dum2] == [p[0]+1,p[1]+1]):r+=1
                    bang[dum1][dum2] = [min(bang[dum1][dum2][0],qpop[2]),min(bang[dum1][dum2][1],qpop[3])]
                    
                    q.append([dum1,dum2,qpop[2],qpop[3]])
                else:break
            else:break
print(r)