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


m = int(sys.stdin.readline())
ql = []
rl = [0]*m
for i in range(m):
    ql.append((list(map(int,sys.stdin.readline().split())),i))
ql.sort()

lis = sorted(list(set(li)))
lis = {lis[i]:i for i in range(len(lis))}

listi = [deque() for i in range(n)]

for i in range(n):
    li[i] = lis[li[i]]
    listi[li[i]].append(i)

tree = [[0 for i in range(2**(20-j))] for j in range(21)]

def seg(l,r,idx,d):
    dum = 2**d
    mid = idx*dum+dum//2
    if(idx*dum==l and l+dum == r):
        return tree[d][idx]
    
    if(r <= mid):
        return seg(l,r,idx*2,d-1)
    if(l >= mid):
        return seg(l,r,idx*2+1,d-1)
    return seg(l,mid,idx*2,d-1)+seg(mid,r,idx*2+1,d-1)

def segadd(idx):
    for i in range(21):
        tree[i][idx]+=1
        idx//=2

for i in range(n):
    if(listi[i]):
        segadd(listi[i].popleft())

qlidx = 0
for i in range(n):
    while (qlidx<m):
        if(ql[qlidx][0][0]-1==i):
            rl[ql[qlidx][1]] = str(seg(i,ql[qlidx][0][1],0,20))
            qlidx+=1

        else:
            break
    if(listi[li[i]]):
        segadd(listi[li[i]].popleft())
print('\n'.join(rl))