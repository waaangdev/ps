"레이저 통신"

import sys
from collections import deque
import heapq
a,b = map(int,sys.stdin.readline().split())

m = []
mbang = [[[10000000000,10000000000,10000000000,10000000000] for i in range(a)] for i in range(b)]

ang = [[0,1],[-1,0],[1,0],[0,-1]]

dum = 0
q = []
end = []

for i in range(b):
    m.append([0 for _ in range(a)])  
    inp = sys.stdin.readline()
    for j in range(a):
        if(inp[j] == '*'):
            m[i][j] = 1
        elif(inp[j] == 'C'):
            if(dum == 0):
                dum = 1
                q = [[0,i,j,-1]]
            else:    
                end = [i,j]
br = 0
while q:
    qpop = heapq.heappop(q)
    qpop = [qpop[1],qpop[2],qpop[0],qpop[3]]
    
    for j in range(4):
        nqpop = [qpop[0]+ang[j][0],qpop[1]+ang[j][1],qpop[2]+1-1*(qpop[3] == -1 or qpop[3] == j),j]
        if(-1 < nqpop[0] < b and -1 <nqpop[1] < a):
            if(m[nqpop[0]][nqpop[1]] == 0):
                if(mbang[nqpop[0]][nqpop[1]][nqpop[3]] > nqpop[2]):
                    
                    heapq.heappush(q,[nqpop[2],nqpop[0],nqpop[1],nqpop[3]])
                    mbang[nqpop[0]][nqpop[1]][nqpop[3]] =nqpop[2]

print(min(mbang[end[0]][end[1]]))