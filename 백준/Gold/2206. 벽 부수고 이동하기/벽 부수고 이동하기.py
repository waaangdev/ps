import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)


n,m = map(int,input().split())
maps = []

for i in range(n):
    inp = sys.stdin.readline().strip()
    maps.append([int(i) for i in inp])

def sol():
    bang = [[[0,0] for i in range(m)] for i in range(n)]
    bang[0][0][0]=1
    q = deque([[0,0,0]])
    if(maps[0][0]==1):
        q = deque([[0,0,1]])
        bang[0][0][1]=1

    ang = [[-1,0],[0,-1],[0,1],[1,0]]

    t = 1

    while q:
        lenq = len(q)
        for _ in range(lenq):
            qpop = q.popleft()
            if(qpop[:2]==[n-1,m-1]):
                return t
            for i in ang:
                np = [qpop[0]+i[0],qpop[1]+i[1],qpop[2]]
                if(-1<np[0]<n and -1<np[1]<m):
                    if(maps[np[0]][np[1]] == 1):
                        np[2]+=1
                    if(np[2]<2):
                        if(bang[np[0]][np[1]][np[2]] == 0):
                            bang[np[0]][np[1]][np[2]]=1
                            q.append(np)
                            
        t+=1
    return -1
if(n==1 and m==1):
    print(1)
else:
    print(sol())