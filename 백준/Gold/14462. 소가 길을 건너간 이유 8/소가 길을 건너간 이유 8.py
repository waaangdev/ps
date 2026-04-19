import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n = int(sys.stdin.readline())
li = []
idxs = [0 for i in range(1000)]
for i in range(n):
    li.append(int(sys.stdin.readline())-1)
for i in range(n):
    idxs[int(sys.stdin.readline())-1] = i

dp = [[-1 for i in range(n)] for i in range(n)]

def dps(l,r):
    if(l == n or r == n):
        return 0
    if(dp[l][r] !=-1):
        return dp[l][r]
    rr = dps(l+1,r)
    for i in range(li[l]-4,li[l]+5):
        if(i > -1 and i < n):
            if(idxs[i] >= r):
                rr = max(rr,dps(l+1,idxs[i]+1)+1)
    dp[l][r] = rr
    return rr
print(dps(0,0))
#print(dp)