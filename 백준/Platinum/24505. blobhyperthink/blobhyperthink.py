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

for _ in range(1):
    n = int(sys.stdin.readline())
    li = list(map(int,sys.stdin.readline().split()))

    lis = sorted([(li[i],i) for i in range(n)])
    lii = [-1]*(n+1)
    lii2 = [-1]*(n+1)
    for i in range(n):
        lii[lis[i][1]] = i
        if(lii2[lis[i][0]]==-1):lii2[lis[i][0]] = i

    dp = [[0 for i in range(n)] for i in range(11)]
    tree = [[[0 for i in range(n)] for i in range(20)] for i in range(11)]

    def seg(l,r,idx,d,tn):
        if(l>=r):return 0
        if(d==-1):
            print(0/0)
            return 0
        dum = 2**d
        mid = idx*dum+dum//2
        if(idx*dum==l and l+dum == r):
            return tree[tn][d][idx]
        
        if(r <= mid):
            return seg(l,r,idx*2,d-1,tn)
        if(l >= mid):
            return seg(l,r,idx*2+1,d-1,tn)
        return (seg(l,mid,idx*2,d-1,tn)+seg(mid,r,idx*2+1,d-1,tn))%1000000007

    def segadd(idx,num,tn):
        for i in range(20):
            tree[tn][i][idx]+=num
            tree[tn][i][idx]%=1000000007
            idx//=2
    #print(lii2)
    rr = 0
    for i in range(n):
        dp[0][i] = 1
        segadd(lii[i],1,0)
        for j in range(1,11):
            if(lii2[li[i]] < 0 or lii2[li[i]] >= n):
                print(0/0)
            dp[j][i] = seg(0,lii2[li[i]],0,19,j-1)%1000000007

            segadd(lii[i],dp[j][i],j)
        rr+=dp[10][i]
        rr%=1000000007
    print(rr%1000000007)
    #print(dp)
    #print(*[random.randrange(1,12) for i in range(1000)])