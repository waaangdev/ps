import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))


n,m,k = list(map(int,sys.stdin.readline().split()))

# def sol(n,m,k):

#     dum = n-m+1
#     sol(n-dum,1,1)+[i for i in range(n,n-dum,-1)]

#     sol(n-k,m-1,1)+[i for i in range(n,n-k,-1)]

dp = [[[0 for i in range(k+1)] for i in range(m+1)] for i in range(n+1)]

def sol(n,m,k,mm,mk):
    #print(n,m,k,mm,mk)
    if(n == 0):
        if(m == 0 and k == 0):
            return []
        else:
            return -1
    if(dp[n][m][k] == -1):
        return -1
    if(m <= n <= mm and k == 1):
        return [i for i in range(1,n+1)]
    if(k <= n <= mk and m == 1):
        return [i for i in range(1,n+1)][::-1]
    
    for i in range(min(mk+1,n+1)-1,max(k,1)-1,-1):
        dum = sol(n-i,m-1,0,mm-1,mk)
        if(dum!=-1):
            return dum+[i for i in range(n,n-i,-1)]
    dp[n][m][k] = -1
    return -1

dum = sol(n,m,k,m,k)
if(dum==-1):
    print(dum)
else:
    print(*dum)
# n = 6

# for m in range(1,n+1):
#     for k in range(1,n+1):
#         li = [0 for i in range(n)]
#         lis = [-1 for i in range(n+1)]#증가
#         lis2 = [-1 for i in range(n+1)]
#         lisc = 0
#         lis2c = 0

#         rr = ""

#         def bf(idx):
#             global lis2c,lisc,rr
#             if(idx == n):
#                 #print(lisc,lis2c)
#                 if(lisc == m and lis2c == k):
#                     return 1
#                 return 0
#             for i in range(n):
#                 if(li[i] == 0):
#                     li[i] = 1
                    
#                     l,r = 0,n
#                     while l+1!=r:
#                         mid = (l+r)//2
#                         if(lis[mid] == -1 or lis[mid] > i+1):
#                             r=mid
#                         else:
#                             l=mid
#                     dum = lis[l+1]
#                     if(lis[l+1]==-1 or lis[l+1]>i+1):
#                         lis[l+1] = i+1
#                     l2 = l
#                     dumc = lisc
#                     lisc = max(lisc,l+1)

#                     l,r = 0,n
#                     while l+1!=r:
#                         mid = (l+r)//2
#                         if(lis2[mid] == -1 or lis2[mid] < i+1):
#                             r=mid
#                         else:
#                             l=mid
#                     dum2 = lis2[l+1]
#                     if(lis2[l+1]==-1 or lis2[l+1]<i+1):
#                         lis2[l+1] = i+1
#                     dum2c=lis2c
#                     lis2c = max(lis2c,l+1)

#                     if(bf(idx+1)):
#                         rr=str(i+1)+" "+rr
#                         return 1

#                     lis2[l+1]=dum2
#                     lis[l2+1]=dum
#                     li[i] = 0
#                     lis2c=dum2c
#                     lisc=dumc
#             return 0
#         bf(0)
#         print(m,k,"=",rr)
#         if(rr==""):rr = -1
#         else:rr = list(map(int,rr.split()))
#         if(rr!=sol(n,m,k,m,k)):
#             print("f")
#             print(sol(n,m,k,m,k))
