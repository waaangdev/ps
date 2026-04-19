import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100)

def dps(idx,mod):
    if(idx == 100):
        return 0
    if(dp[idx][mod]!=-1):
        return dp[idx][mod]
    if(mod+li[idx] == n):
        dp[idx][mod]=li2[idx]
        return li2[idx]
    r = 0
    dum = (mod+li[idx])%n
    if(dps(idx+1,dum)):
        r = dps(idx+1,dum)+(li2[idx])
        dp[idx][mod] = r
        return r
    if(dps(idx+1,mod)):
        r = dps(idx+1,mod)
    dp[idx][mod] = r
    return r

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    dp = [[-1 for i in range(n)] for i in range(100)]
    li2 = [(10**i) for i in range(100)]
    li = []
    r = 0
    for i in range(100):
        li.append((10**i)%n)
        if((10**i)%n == 0):
            print(10**i)
            r = 1
            break
    
    
    if(r == 0):
        if(dps(0,0) == 0):print("BREK")
        else:print(dps(0,0))