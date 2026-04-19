#카드 정리 1
import sys
from collections import deque

n,m = (map(int,sys.stdin.readline().strip().split()))
box=[0]*n
col = [0]*m
for i in range(n): 
    dum= list(map(int,sys.stdin.readline().strip().split()))
    if(sum(dum)==max(dum)):
        if(max(dum) == 0):
            box[i] = 1
        else:
            if(col[dum.index(max(dum))]==0):
                box[i] = 1
                col[dum.index(max(dum))] = 1

r = n+1
for i in range(n): 
    r = min(r,n-(sum(box)-box[i])-1)

print(r)