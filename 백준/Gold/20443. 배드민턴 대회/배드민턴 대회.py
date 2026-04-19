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

mod = 1000000007
def ncm(n,m):
    r = 1
    for i in range(m):
        r*=(n-i)
    
    r//=math.factorial(m)
    return r

n = int(sys.stdin.readline())
n2 = n-n%4
r = ncm(n,n2)


#print(r)


dp = [0]*101
dp[0]=1
for i in range(2,101):
    dp[i] = (dp[i-1]+dp[i-2])*(i-1) %mod
print(dp[n2]*r%mod)