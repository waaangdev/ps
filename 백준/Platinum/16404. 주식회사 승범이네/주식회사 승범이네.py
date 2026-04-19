import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(100001)

n,m = list(map(int,sys.stdin.readline().split()))
li = list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(n)]

for i in range(1,n):
    ways[li[i]-1].append(i)

for i in range(n):
    while(len(ways[i])>2):
        ways.append([ways[i].pop(0),ways[i].pop(0)])
        ways[i].append(len(ways)-1)

pi = [-1 for i in range(len(ways))]
up = [0 for i in range(len(ways))]
v = [0 for i in range(len(ways))]
pways = [[]]
pways_up = [-1]
pi[0] = 0

def dfs(idx,c,his):
    if(c==317):
        pi[idx]=len(pways)
        pways[his].append(len(pways))
        pways.append([])
        pways_up.append(his)
        dfs(idx,0,len(pways)-1)
    else:
        for i in ways[idx]:
            up[i]=idx
            dfs(i,c+1,his)


def padd(idx,a):
    if(pi[idx]!=-1):
        pways_v[pi[idx]]+=a
        return
    for i in ways[idx]:
        padd(i,a)
#print(ways,up)
dfs(0,0,0)

pways_v = [0 for i in range(len(pways))]


for _ in range(m):
    inp = list(map(int,sys.stdin.readline().split()))
    if(inp[0]==1):
        v[inp[1]-1]+=inp[2]
        padd(inp[1]-1,inp[2])
        # dum = inp[1]-1

        # while(pi[dum]==-1):
        #     v[dum]+=inp[2]
        #     dum = up[dum]

        # pways_v[pi[dum]]+=inp[2]
    else:
        r = 0
        dum = inp[1]-1
        while(pi[dum]==-1):
            r+=v[dum]
            dum = up[dum]
        dum = pi[dum]
        while(dum!=-1):
            r+=pways_v[dum]
            dum = pways_up[dum]
        print(r)
