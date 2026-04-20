import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(10001)

m,n = list(map(int,sys.stdin.readline().split()))
k = int(sys.stdin.readline())
li = []
for i in range(k):
    li.append(list(map(int,sys.stdin.readline().split())))

diss = []
for i in range(k):
    diss.append([li[i][1],i,k])#위
    diss.append([n-li[i][1],i,k+1])#아래
    for j in range(i+1,k):
        diss.append([math.sqrt((li[i][0]-li[j][0])**2+(li[i][1]-li[j][1])**2),i,j])
diss.append([n,k,k+1])

diss.sort()

par = [i for i in range(k+2)]
upd = [0 for i in range(k+2)]
upd[k]=1
upd[k+1]=2

def getpar(a):
    if(par[a]==a):return a
    par[a]=getpar(par[a])
    return par[a]

def union(a,b):
    a=getpar(a)
    b=getpar(b)
    if(a>b):a,b=b,a
    if(upd[a] and upd[b]):
        if(upd[a]!=upd[b]):
            return 1
    else:
        upd[a] = max(upd[a],upd[b])
    par[b]=a
    return 0

for dis in diss:
    if(union(dis[1],dis[2])):
        print('{0:.8f}'.format(dis[0]/2))
        break
