import sys
from collections import deque
import random
import math
import heapq
sys.setrecursionlimit(4000)
#ABCXXX - X

#n = int(sys.stdin.readline())
#li = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

pli = [1]*20000
pl=[]
for i in range(2,20000):
    if(pli[i]):
        pl.append(i)
        for j in range(i,20000,i):
            pli[j]=0
#print(pl[3:10],len(pl))
pl=pl[3:]

n,k = list(map(int,sys.stdin.readline().split()))
d = 0
li = [1]*n
# for k in range(0,n*(n-1)//2+1):
#     li = [1]*n
#     while 1:
#         li[0]+=1
#         for i in range(n-1):
#             if(li[i] == n*n):
#                 li[i]=1
#                 li[i+1]+=1
#         if(li[-1]==n*n):break
#         d=0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if(math.gcd(li[i],li[j])==1):
#                     d +=1
#         if(d==k):
#             print(f"{n} {k} : ",*li)
#             break

def sol(n,k):
    if(k == 0):
        return ([2]*n)
    elif(k < n):
        return ([6]*(n-1-k)+[3]*1+[2]*k)
    else:
        return sol(n-1,k-(n-1))+[pl[n]]
    
li = sol(n,k)
# for i in range(n):
#     for j in range(i+1,n):
#         if(math.gcd(li[i],li[j])==1):
#             d +=1
# if(d==k):
    
print(*li)