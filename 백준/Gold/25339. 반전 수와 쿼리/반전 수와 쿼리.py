#abbc
import sys
from collections import deque

n,q = map(int,sys.stdin.readline().strip().split())

rr = 0
for i in range(q):
    a,l,r = map(int,sys.stdin.readline().strip().split())
    if(a == 1):
        rr=1-rr
    else:
        if((((r-l)+1)//2)%2 == 1):
            rr=1-rr
    print(rr)

    