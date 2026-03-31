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



def sol(idx,bang):
    if(idx == n*m):return 0
    if(dp[idx][bang] !=-1):
        return dp[idx][bang]
    nbang = (bang*2)%(2**(m+2))
    if(maps[idx]!='.'):
        return sol(idx+1,nbang)
    
    r = sol(idx+1,nbang)
    dum = 0
    if(( nbang&(2**(m+2-3))==0 or idx%m == m-1) and ((nbang&(2**(m+2-1))==0 and nbang&(2**1)==0) or idx%m == 0)):
        r = max(r,sol(idx+1,nbang+1)+1)
        dum = 1
    dp[idx][bang] = r
    #print(idx,bin(nbang),r,dum)
    return dp[idx][bang]

for i in range( int(sys.stdin.readline())):
    n,m = list(map(int,sys.stdin.readline().split()))
    dum = 0
    maps = ""
    for i in range(n):
        inp = sys.stdin.readline().strip()
        maps+=(inp)
        if('.' in inp):
            dum+=1
    if(m == 1 or m == 2):
        print(dum)
    
    else:
        dp = [[-1]*16384 for i in range(100)]

        print(sol(0,0))
