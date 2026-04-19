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

n,d=list(map(int,sys.stdin.readline().split()))
ways = [[] for i in range(10001)]
dp=[10001]*10001
for i in range(n):
    inp=list(map(int,sys.stdin.readline().split()))
    ways[inp[0]].append(inp[1:])
dp[0]=0

for i in range(0,d):
    dp[i+1]=min(dp[i+1],dp[i]+1)
    for j in ways[i]:
        dp[j[0]]=min(dp[j[0]],dp[i]+j[1])
print(dp[d])