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
li += [0]*(131072-len(li))
tree = [[] for i in range(18)]

for i in range(18):
    dum = 2**(i)
    for j in range(2**(18-i)):
        tree[i].append(sorted(li[j*dum:j*dum+dum]))

m = int(sys.stdin.readline())

def gets(idx,d,num):
    l,r = 0,len(tree[d][idx])
    while (l+1!=r):
        mid = (l+r)//2
        if(tree[d][idx][mid] <= num):
            l = mid
        else:
            r = mid
    
    if(tree[d][idx][0] > num):return len(tree[d][idx])
    return len(tree[d][idx])-l-1

def seg(l,r,idx,d,num):
    dum = 2**d
    mid = idx*dum+dum//2
    if(idx*dum==l and l+dum == r):
        return gets(idx,d,num)
    
    if(r <= mid):
        return seg(l,r,idx*2,d-1,num)
    if(l >= mid):
        return seg(l,r,idx*2+1,d-1,num)
    return seg(l,mid,idx*2,d-1,num)+seg(mid,r,idx*2+1,d-1,num)

for i in range(m):
    inp =  list(map(int,sys.stdin.readline().split()))
    print(seg(inp[0]-1,inp[1],0,17,inp[2]))