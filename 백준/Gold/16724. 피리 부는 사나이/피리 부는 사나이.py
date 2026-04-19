"피리부는 사나이"

import sys
from collections import deque

r = 0 
sero,garo = map(int,sys.stdin.readline().split())
bang = [[10000000]*garo for _ in range(sero)]
mmap = [[""] * garo for _ in range(sero)]
qwe = 0

ang =  {'U':[-1,0],'D':[1,0],'R':[0,1],'L':[0,-1]}

for i in range(sero):
    mmap[i] = list(sys.stdin.readline())

for i in range(sero):
    for j in range(garo):
        qwe += 1
        if(bang[i][j] == 10000000):
            
            qpop = [i,j]
            while 1:
                bang[qpop[0]][qpop[1]] = min(bang[qpop[0]][qpop[1]],qwe+1)
                
                aa = ang[mmap[qpop[0]][qpop[1]]]
                n1 = qpop[0]+aa[0]
                n2 = qpop[1]+aa[1]
                
                if(bang[n1][n2] != 10000000):
                    if(bang[n1][n2] == qwe+1): r += 1
                    break
                
                qpop[0] = n1
                qpop[1] = n2
                
print(r)
                    
            