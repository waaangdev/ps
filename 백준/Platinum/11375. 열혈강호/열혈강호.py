import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li1 = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(100001)

n,m =  list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(1000)]
bang = [0 for i in range(1000)]
bang2 = [-1 for i in range(1000)]

for i in range(n):
    inp =  list(map(int,sys.stdin.readline().split()))
    for j in inp[1:]:
        ways[i].append(j-1)


def dfs(idx):
    if(bang[idx]):return 0
    bang[idx]=1
    dum = 1
    for i in ways[idx]:

        if(bang2[i]==-1 or dfs(bang2[i])):
            bang2[i] = idx
            return 1
        
    return 0

rr =0
for i in range(n):
    bang = [0 for i in range(1000)]
    rr+=dfs(i)
print(rr)
