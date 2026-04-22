import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

n,m=list(map(int,sys.stdin.readline().split()))
maps = []
for i in range(n):
    maps.append(list(sys.stdin.readline().strip()))

bang = [[0 for i in range(m)] for i in range(n)]
bang2 = [[-1 for i in range(m)] for i in range(n)]

def sol(qpop):
    if(bang2[qpop[0]][qpop[1]]!=-1):return bang2[qpop[0]][qpop[1]]
    t = 1
    qm = int(maps[qpop[0]][qpop[1]])
    for i in [[-1,0],[1,0],[0,1],[0,-1]]:
        nq = [qpop[0]+i[0]*qm,qpop[1]+i[1]*qm]
        if(-1<nq[0]<n and -1<nq[1]<m):
            if(maps[nq[0]][nq[1]]!='H'):
                if(bang[nq[0]][nq[1]]==0):
                    bang[nq[0]][nq[1]]=1
                    d = sol(nq)
                    if(d==-1):return -1
                    t=max(t,d+1)
                    bang[nq[0]][nq[1]]=0
                else:
                    return -1
    bang2[qpop[0]][qpop[1]] = t
    return t
print(sol([0,0]))