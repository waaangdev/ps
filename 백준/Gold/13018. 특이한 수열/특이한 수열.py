import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

sys.setrecursionlimit(100001)

# a,b  = list(map(int,sys.stdin.readline().split()))
# r = 1
# dum10,dum2,dum5 = 0,0,0

# def gcd(a,b):
#     if(a//b == 0):return b
#     return gcd(b,a%b)
n,k = list(map(int,sys.stdin.readline().split()))
# li = [0 for i in range(n)]
# r = ""
# def sol(idx,k):
#     global r
#     if(idx == n):
#         return k == 0
#     for i in range(n):
#         if(li[i] == 0 and (k!=0 or math.gcd(idx+1,i+1) == 1)):
#             li[i] = 1
#             if sol(idx+1,k-( math.gcd(idx+1,i+1) > 1)*1):
#                 r = str(i+1)+" "+r
#                 return 1
#             li[i] = 0
#     return 0
# sol(0,k)
# print(r)
# print(*range(1,n+1))

if((n-k) >= 1):

    if((n-k)%2 == 0):
        for i in range(1,n-k+1,2):
            print(i+1,i,end=' ')
        for i in range(n-k+1,n+1):
            print(i,end=" ")
    else:
        for i in range(1,k+2):
            print(i,end=' ')
        for i in range(k+2,n,2):
            print(i+1,i,end=' ')
else:
    print("Impossible")