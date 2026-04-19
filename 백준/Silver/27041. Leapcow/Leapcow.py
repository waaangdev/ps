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

n,m,c = list(map(int,sys.stdin.readline().split()))
li = [0]*(n+1)
for i in range(c):
    li[int(sys.stdin.readline())]=1
dp = [40001]*(n+1)

dp[0]=0
for i in range(1,(n+1)):
    if(li[i]==0):
        mins = 40001
        for j in range(max(0,i-m),i):
            if(li[j]==0):mins = min(mins,dp[j])
        dp[i]=mins+1
#print(dp)
print(dp[-1])