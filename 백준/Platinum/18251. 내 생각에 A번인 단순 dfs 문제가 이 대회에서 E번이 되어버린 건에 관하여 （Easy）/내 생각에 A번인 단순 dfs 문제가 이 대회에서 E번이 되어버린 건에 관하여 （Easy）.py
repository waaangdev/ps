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

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

li2 = [0 for i in range(n)]

d = int(math.log2(n+1))

c =0
for i in range(d):
    st = 2**(d-i-1)-1
    idx = st
    for j in range(2**i):
        li2[idx] = [li[c],i]
        c+=1
        idx += (st+1)*2
#print(li2)
r = li[0]
for i in range(d):
    for j in range(i,d):
        li3 = [0 for i in range(n)]
        li4 = [0 for i in range(n)]
        sums = 0
        sums2 = 0
        for k in range(n):
            if(i<=li2[k][1]<=j):
                sums2+=1
                sums += li2[k][0]
            li3[k]=sums
            li4[k]=sums2
        #print(li3)
        mins = 0
        mins2= 0
        for k in range(n):
            if(li4[k]-mins2!=0):
                r=max(r,li3[k]-mins)
            if(li3[k] < mins):
                mins =li3[k]
                mins2 = li4[k]
print(r)
