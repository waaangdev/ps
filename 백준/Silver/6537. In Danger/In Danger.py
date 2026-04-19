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


while(1):
    st = sys.stdin.readline().strip()
    if(st=="00e0"):break
    st= int(st[:2]+int(st[3])*'0')
    dum = 0
    li = []
    while st!=1:
        if(dum==0):
            dum = st%2
            st-=st//2
            li.append(0)
        else:
            dum = 1-st%2
            st-=st//2+st%2
            li.append(1)
    li.reverse()
    r = 0
    for i in li:
        if(i==1):
            r+=r+1
        else:
            r+=r

    print(r+1)
