import sys
from collections import deque
import random
import math
import heapq
sys.setrecursionlimit(1000001)
#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

def getpar(idx):#https://www.acmicpc.net/source/96604645
    if(uf[idx] == idx):
        return idx
    uf[idx] = getpar(uf[idx])
    return uf[idx]


n,m = list(map(int,sys.stdin.readline().split()))
count = [0]*n
uf = [i for i in range(n)]
q=[]
for i in range(m):
    a,b,v = list(map(int,sys.stdin.readline().split()))
    heapq.heappush(q,(-v,a-1,b-1))

r =0
for i in range(m):
    qpop = heapq.heappop(q)
    v,a,b=qpop
    if(a > b): a,b = b,a
    a=getpar(a)
    b=getpar(b)
    if(a==b):
        if(count[a]==0):
            count[a]+=1
            r+=-v
        else:
            pass
    else:
        if(count[a] == 1 and count[b]==1):
            pass
        else:
            r+=-v
            count[a]+=count[b]
            uf[b] = a
print(r)


