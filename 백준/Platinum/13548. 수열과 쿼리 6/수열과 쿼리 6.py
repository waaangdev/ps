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

#nsqrt(n) = 3천만

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))


m = int(sys.stdin.readline())
ql = []
rl = [0]*m
for i in range(m):
    inp = list(map(int,sys.stdin.readline().split()))
    inp[0]-=1
    ql.append((inp,i))
ql.sort(key = lambda x:(x[0][0]//317)*1000000+x[0][1])

ncl = [0]*(100001)
ncll = [0]*(100002)
ncl_max = 0

sqhis = -1
sqhis_r = 0
for i2 in range(m):
    l,r = ql[i2][0]

    if(l//317 != sqhis//317):
        ncl = [0]*(100001)
        ncll = [0]*(100002)
        ncl_max = 0
        for i in range(l,r):
            ncl[li[i]]+=1
        for i in range(100001):
            ncll[ncl[i]]+=1
        ncl_max = max(ncl)
    else:
        if(l > sqhis):
            for i in range(sqhis,l):
                ncll[ncl[li[i]]] -=1
                ncl[li[i]]-=1
                ncll[ncl[li[i]]] +=1

                if(ncll[ncl_max+1] != 0):
                    ncl_max+=1
                if(ncll[ncl_max]==0):
                    ncl_max-=1
        else:
            for i in range(l,sqhis):
                ncll[ncl[li[i]]] -=1
                ncl[li[i]]+=1
                ncll[ncl[li[i]]] +=1

                if(ncll[ncl_max+1] != 0):
                    ncl_max+=1
                if(ncll[ncl_max]==0):
                    ncl_max-=1

        for i in range(sqhis_r,r):
            ncll[ncl[li[i]]] -=1
            ncl[li[i]]+=1
            ncll[ncl[li[i]]] +=1

            if(ncll[ncl_max+1] != 0):
                ncl_max+=1
            if(ncll[ncl_max]==0):
                ncl_max-=1
    rl[ql[i2][1]] = str(ncl_max)
    sqhis = l
    sqhis_r = r
print('\n'.join(rl))