import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

n,m = list(map(int,sys.stdin.readline().split()))
li = []
for i in range(n):
    li.append(tuple(map(int,sys.stdin.readline().split())))
li.sort()
#print(li)
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if(li[j][0] <= li[i][0] and li[j][1] <= li[i][1]):
            dp[i] = max(dp[i],dp[j])
    dp[i]+=max(0,m-li[i][0]-li[i][1])
print(max(dp))