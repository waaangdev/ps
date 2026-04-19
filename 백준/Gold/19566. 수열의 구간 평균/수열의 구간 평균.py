import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

n,k = list(map(int,sys.stdin.readline().split()))
li = list(map(int,sys.stdin.readline().split()))
for i in range(n):
    li[i] -= k
#print(li)

li2 = [0 for i in range(n)]
li2[0] = li[0]
for i in range(1,n):
    li2[i] = li[i]+li2[i-1]
#print(li2)

li2 = [0]+li2

li2s = []
for i in range(len(li2)):
    li2s.append((li2[i],i))

li2s.sort()
#print(li2s)
dp = [0 for i in range(n+1)]
for i in range(1,n+1):
    l,r = 0,len(li2s)
    while(l+1!=r):
        mid = (l+r)//2
        if(li2s[mid][0] < li2[i]):
            l = mid
        elif(li2s[mid][0] > li2[i]):
            r = mid
        else:
            if(li2s[mid][1] >= i):
                r = mid
            else:
                l = mid
    #print(l)
    if(li2s[l][0] == li2[i] and li2s[l][1] < i):
        dp[i] = dp[li2s[l][1]]+1

print(sum(dp))
# rr = 0

# def sol(l,r):
#     global rr
#     if(l+1 == r):
#         if(li[l] == 0):
#             rr+=1
#         return li[l]

#     drr = 0
#     dum = l+(r-l)//2
#     ls = sol(l,dum)
#     rs = sol(dum,r)

#     sdum = 0
#     for i in range(dum,r):
#         sdum+=li[i]
#         if(sdum == -ls):
#             drr+=1

#     sdum = 0
#     for i in range(dum-1,l,-1):
#         sdum+=li[i]
#         if(sdum == -rs):
#             drr+=1

#     print(l,r,drr)

#     return ls+rs

# sol(0,n)
# print(rr)

