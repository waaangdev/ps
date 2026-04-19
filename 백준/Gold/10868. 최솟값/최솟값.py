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

n,m=list(map(int,sys.stdin.readline().split()))
tree = [[0 for j in range(2**(17-i))] for i in range(18)]
for i in range(n):
    tree[0][i] = int(sys.stdin.readline())
for i in range(1,18):
    for j in range(2**(17-i)):
        tree[i][j] = min(tree[i-1][j*2],tree[i-1][j*2+1])

def seg(l,r,d,idx):
    dum = (1<<d)*idx
    if(l==dum and l+(1<<d)==r):
        return tree[d][idx]
    dum+=(1<<(d-1))
    if(l >= dum): return seg(l,r,d-1,idx*2+1)
    elif(r <= dum): return seg(l,r,d-1,idx*2)
    else: return min(seg(l,dum,d-1,idx*2),seg(dum,r,d-1,idx*2+1))

for _ in range(m):
    a,b=list(map(int,sys.stdin.readline().split()))
    print(seg(a-1,b,17,0))