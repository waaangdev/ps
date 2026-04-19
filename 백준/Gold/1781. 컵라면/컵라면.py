import sys
from collections import deque
import heapq
n = list(map(int,sys.stdin.readline().strip().split()))[0]
li = [[] for i in range(n)]
for i in range(n):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    li[inp[0]-1].append(inp[1])
q = []
r = 0
for i in range(n-1,-1,-1):
    for j in range(len(li[i])):
        heapq.heappush(q,-li[i][j])
    if(q):r+=-heapq.heappop(q)
print(r)