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

dp =[ [-1 for i in range(2403)] for i in range(2403)]

def sol(b,k):
    #print(b,k)
    if(dp[b][k]==-1):
        dum = [max(0,b//2-(1-b%2)),min(b,b//2+1)]
        r = 0
        for i in range(dum[0],dum[1]+1):
            #print(i)
            if(i==k):
                r+=1
            elif(i < k):
                r+=sol(b-i-1,k-i-1)+1
            elif(i > k):
                r+=sol(i-1,k)+1
        dp[b][k]=r/(dum[1]-dum[0]+1)
    return dp[b][k]


for i in range( int(sys.stdin.readline())):
    a,b,k=list(map(int,sys.stdin.readline().split()))
    b -= a
    k-=a
    print(sol(b,k))