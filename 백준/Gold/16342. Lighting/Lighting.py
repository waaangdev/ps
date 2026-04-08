import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

sys.setrecursionlimit(100001)


n,k = list(map(int,sys.stdin.readline().split()))
st = sys.stdin.readline().strip()
mst = bin(int("0b"+st,2)+int('0b'+'1'*n,2))[2:]
if(len(mst)!=n):st='0'+st
#print(st,mst)
dp = [[[[-1]*2 for i in range(1001)] for i in range(1001)] for i in range(2)]
def ddp(fit,fit2,idx,c):
    if(c>k):return 0
    if(idx==len(mst)):return c==k
    if(dp[fit2][c][idx][fit] !=-1):return dp[fit2][c][idx][fit]
    l = 0
    rs=1
    if(fit and st[idx]=='1'):l=1
    if(fit2 and mst[idx]=='0'):rs=0
    r = 0
    for i in range(l,rs+1):
        r+=ddp(fit and (i==l),fit2 and (i==rs),idx+1,c+i)
    r%=10**9+7
    dp[fit2][c][idx][fit] = r
    return r
print(ddp(1,1,0,0))