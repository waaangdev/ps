import sys
import math
from collections import deque


n,m = map(int,input().split())
li = list(map(int,sys.stdin.readline().strip().split()))
q = deque([])

for i in range(n):
    while (q and q[0][1] < i-m+1):
        q.popleft()
        if(not q):break
    while(q and q[-1][0] > li[i]):
        q.pop()
        if(not q):break
    q.append([li[i],i])
    sys.stdout.write(str(q[0][0])+" ")
    