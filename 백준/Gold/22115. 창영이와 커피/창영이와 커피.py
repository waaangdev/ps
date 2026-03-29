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

n,k=list(map(int,sys.stdin.readline().split()))
li=list(map(int,sys.stdin.readline().split()))
li.sort()
dp = [[-2]*100000 for i in range(100)]
def sol(idx,k2):
    if(k2==k):return 0
    if(idx==n):return -1
    if(dp[idx][k2] != -2):
        return dp[idx][k2]
    

    if(k2+li[idx] > k):
        return -1
    
    a = sol(idx+1,k2+li[idx])
    b = sol(idx+1,k2)
    if(a==-1):
        dp[idx][k2]=b
        return b
    if(b==-1):
        dp[idx][k2]=a+1
        return a+1
    dp[idx][k2]=min(a+1,b)
    return min(a+1,b)
print(sol(0,0))