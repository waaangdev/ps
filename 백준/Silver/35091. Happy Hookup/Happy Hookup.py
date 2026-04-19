import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

n,m = list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(n)]

for i in range(m):
    dum = list(map(int,sys.stdin.readline().split()))
    ways[dum[0]-1].append(dum[1]-1)

p = list(map(int,sys.stdin.readline().split()))

bang = [[0 for i in range(n)] for j in range(2)]

for i in range(2):
    q = deque([p[i]-1])
    bang[i][p[i]-1] = 1
    while q:
        qpop = q.popleft()
        for j in ways[qpop]:
            if(bang[i][j] == 0):
                q.append(j)
                bang[i][j] = 1


r = -1
for i in range(n):
    if(bang[0][i] + bang[1][i] == 2):
        r = i+1
#print(bang)
if(r!=-1):
    print("yes")
    print(r)
else:
    print("no")