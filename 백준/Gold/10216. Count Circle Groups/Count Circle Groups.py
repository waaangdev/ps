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

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    li = []
    ways = [[] for i in range(n)]
    for i in range(n):
        inp = list(map(int,sys.stdin.readline().split()))
        for j in range(i):
            if((inp[0]-li[j][0])**2+(inp[1]-li[j][1])**2 <= (inp[2]+li[j][2])**2):
                ways[i].append(j)
                ways[j].append(i)
        li.append(inp)
    bang = [0]*n
    rr=0
    for i in range(n):
        if(bang[i]==0):
            rr+=1
            q=deque([i])
            bang[i]=1
            while q:
                qpop=q.popleft()
                for j in ways[qpop]:
                    if(bang[j]==0):
                        bang[j]=1
                        q.append(j)
    print(rr)