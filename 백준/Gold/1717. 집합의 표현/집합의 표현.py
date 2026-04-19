from collections import deque
import sys


sys.setrecursionlimit(1000001)

n,m = map(int,sys.stdin.readline().split())
par = [i for i in range(n+1)]


def getpar(idx):
    if(par[idx] == idx):
        return idx
    par[idx] = getpar(par[idx])
    return par[idx]

for i in range(m):
    d1,d2,d3 = map(int,sys.stdin.readline().split())
    if(d1==0):
        if(d2!=d3):
            if(d2 > d3): d2,d3 = d3,d2
            par[getpar(d3)] = getpar(d2)
    else:
        if(getpar(d3)==getpar(d2)):
            print("YES")
        else:
            print("NO")