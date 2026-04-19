import sys
from collections import deque
import random
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100)

# def sigma(n):
#     r=0
#     for i in range(1,n+1):
#         if(n%i == 0):
#             r+=i
#     return r

# for i in range(1,10000):
#     if(sigma(i)%2!=0):
#         print(i,end="=")
#         if(round(i**(1/2))**2 == i):
#             print(round(i**(1/2)),round(i**(1/2)))
#         elif(round((i//2)**(1/2))**2 == i//2):
#             print(2,round((i/2)**(1/2)),round((i/2)**(1/2)))
#         # i2 = i
#         # dum = 0
#         # for j in range(2,i+1):
#         #     while(i2%j == 0):
#         #         i2//=j
#         #         print(j,end="*")
#         #         dum+=j
#         print()
n = int(sys.stdin.readline())
r = n
i = 1
while (i*i <= n):
    r-=1
    i+=1

i = 1
while (2*i*i <= n):
    r-=1
    i+=1
print(r)