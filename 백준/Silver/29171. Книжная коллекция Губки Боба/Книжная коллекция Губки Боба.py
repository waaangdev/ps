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

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
li = [set(list(range(1,n+1))),set(list(range(n+1,n*2+1)))]
rr= n

for _ in range(k):
    inp = list(map(int,sys.stdin.readline().split()))
    x = [0,0]
    for i in range(2):
        if(inp[i] in li[1]):
            x[i]=1
    if(x[0]!=x[1]):
        for i in range(2):
            if(x[i]==0 and inp[i]<n+1):rr-=1
            li[x[i]].remove(inp[i])
        for i in range(2):
            if(x[1-i]==0 and inp[i]<n+1):rr+=1
            li[x[1-i]].add(inp[i])
    print(rr)