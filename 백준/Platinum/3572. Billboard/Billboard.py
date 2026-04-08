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

for i in range(n):
    inp = int(sys.stdin.readline())

    idx = 0
    for i in range(18,-1,-1):
        if(idx*2 >= min(h,n)):
            idx*=2
            break
        if(segtree[i][idx*2] >= inp):
            idx = idx*2
        else:
            idx = idx*2+1
        
    r=idx
    
    if(idx < min(h,n)):
        print(r+1)
        dum = r
        segtree[0][dum]-=inp
        for j in range(1,19):
            dum//=2
            segtree[j][dum]=max(segtree[j-1][dum*2],segtree[j-1][dum*2+1])
    else:
        print(-1)
    #print(segtree)