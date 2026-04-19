import sys
import math
from collections import deque
import heapq
#구간이 이븐하지 않아요.


n =int(input())
li = list(map(int,sys.stdin.readline().strip().split()))
li2 = list(set(li))
li3 = {}
for i in range(len(li2)):
    li3[li2[i]]=i
li = [li3[i] for i in li]
#print(li)
#print(li,li3)
r = 0
for i in range(n-1):
    dum = 0
    k = i
    l = i+1
    o = min(i+1,n-i-1)*2
    dum2 = 0
    dp = [0]*n
    while(dum2 < o):
        k2 = li[k]
        l2 = li[l]
        if(dp[k2] ==0):dum+=1
        dp[k2]+=1
        if(dp[k2] ==0):dum-=1
        if(dp[l2] ==0):dum+=1
        dp[l2]-=1
        if(dp[l2] ==0):dum-=1
        dum2+=2
        #print(k,l,dum,dum2,dp)
        if(dum == 0 and dum2 > r):r =dum2
        k-=1
        l+=1
print(r)