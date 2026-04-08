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

h,w,n =  list(map(int,sys.stdin.readline().split()))

segtree = [[w]*(min(h,n)+1) for i in range(19)]

def seg(l,r,idx,d):
    d2 = (2**d)
    if(idx*d2==l and r==l+d2):
        return segtree[d][idx]
    mid = idx*d2+d2//2
    if(r<=mid):
        return seg(l,r,idx*2,d-1)
    elif(l>=mid):
        return seg(l,r,idx*2+1,d-1)
    else:
        return max(seg(l,mid,idx*2,d-1),seg(mid,r,idx*2+1,d-1))

for i in range(n):
    inp = int(sys.stdin.readline())

    l,r = -1,min(h,n)-1
    while l+1!=r:
        mid = (l+r)//2
        if(seg(0,mid+1,0,18)>=inp):
            r = mid
        else:
            l=mid
    if(seg(0,r+1,0,18)>=inp):
        print(r+1)
        dum = r
        segtree[0][dum]-=inp
        for j in range(1,19):
            dum//=2
            segtree[j][dum]=max(segtree[j-1][dum*2],segtree[j-1][dum*2+1])
    else:
        print(-1)
    #print(segtree)