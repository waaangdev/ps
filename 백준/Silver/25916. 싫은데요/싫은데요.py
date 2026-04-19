import sys
from collections import deque
import random
import math
import heapq

n,m = list(map(int,sys.stdin.readline().split()))
li = [0]+list(map(int,sys.stdin.readline().split()))
hli = li[:]
h=li[0]
rr = 0
for i in range(1,n+1):
    h+=li[i]
    hli[i]=h
    l,r=-1,i
    while(l+1!=r):
        mid=(l+r)//2
        if(hli[i]-hli[mid] > m):
            l=mid
        else:
            r=mid
    #print(i,r,hli[i]-hli[r])
    rr=max(rr,hli[i]-hli[r])
print(rr)