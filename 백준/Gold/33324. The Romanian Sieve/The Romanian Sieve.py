import sys
from collections import deque
import random
import math
import heapq

#ABCXXX - X

#n = int(sys.stdin.readline())
#li1 = list(map(int,sys.stdin.readline().split()))
#st = sys.stdin.readline().strip()

#sys.setrecursionlimit(100001)

n = int(sys.stdin.readline())
def harm(n):
    r = 0
    for i in range(1,n+1):
        d1,d2 = ((n//i)-(n//(i+1)))*i,(n//i)
        if(d2 < i):
            break
        if(d2 == i):
            r-=d1
        r+=d1+d2
    return r
#print(harm(n))
l,r = 0,3*10**13+1
while(l+1!=r):
    mid = (l+r)//2
    m=harm(mid)
    if(m<n):
        l=mid
    elif(m>n):
        r=mid
    else:
        l=mid
        break
print(l)
