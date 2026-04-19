import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(200001)

n,m = list(map(int,sys.stdin.readline().split()))
ways2 = [[] for i in range(n)]

for i in range(n-1):
    inp = list(map(int,sys.stdin.readline().split()))
    ways2[inp[0]-1].append(inp[1]-1)
    ways2[inp[1]-1].append(inp[0]-1)
ways = [[] for i in range(n)]
lens = [-1]*n
lens[m-1]=0
q=deque([m-1])
t = 0
while q:
    t+=1
    lenq = len(q)
    for i in range(lenq):
        qpop = q.popleft()
        for j in ways2[qpop]:
            if(lens[j]==-1):
                ways[qpop].append(j)
                lens[j]=t
                q.append(j)

ways2 = []

up = [0 for i in range(n)]
v =  [0 for i in range(n)]
nways = [[] for i in range(n)]

def dfs(idx,hiss):
    two = -1
    if(lens[idx] !=0):
        for i in range(19):
            if(lens[idx]%(2**i)==0):
                two = i

    up[idx]=hiss[two+1]

    for i in range(two):
        nways[hiss[i]].append(idx)
    for i in range(19):
        if(lens[idx]%(2**i)==0):
            hiss[i] = idx


    for i in ways[idx]:
        dfs(i,hiss[:])
    

def gets(idx):
    
    r = v[idx]
    for i in nways[idx]:
        r+=gets(i)

    return r

dfs(m-1,[-1]*20)

ways = []

#print(pi2)
q = int(sys.stdin.readline())
for _ in range(q):
    inp = list(map(int,sys.stdin.readline().split()))
    if(inp[0]==1):
        dum = inp[1]-1
        while (dum !=-1):
            v[dum]+=1
            dum = up[dum]
        
    else:
        r = gets(inp[1]-1)

        print((r)*(lens[inp[1]-1]+1))
    # print(v)
    # print(up)
    # print(nways)
