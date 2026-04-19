import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

n = int(sys.stdin.readline())
# dp = [0 for i in range(n+1)]
# dp[0] = 1
# dp[1] = 1
# for i in range(2,n+1):
#     r = i
#     for j in range(i-1,-1,-1):
#         if(dp[j]*(i-j) > r):
#             r = dp[j]*(i-j)
#             if(i-j > 3):
#                 print("?????",i,j,i-j)
#     dp[i] = r
# print(dp[-1]%10007)


def fastpow(a,n,mod):
    if(n == 0):
        return 1
    if(n%2 == 0):
        return fastpow(a,n//2,mod)**2%mod
    else:
        return (fastpow(a,n//2,mod)**2*a)%mod


if(n==0):
    print(0)
elif(n==1):
    print(1)
else:
    d1,d2,d3 = n%2,n//2,0
    #dr = fastpow(2,d2,10007)
    #rr = dr
    while d2:
        if(d1 and d2):
            d3+=1
            d1-=1
            d2-=1
        elif(d2>=3):
            d2-=3
            d3+=2
        else:
            break
    print(fastpow(2,d2,10007)*fastpow(3,d3,10007)%10007)
