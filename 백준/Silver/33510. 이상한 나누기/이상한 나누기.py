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
li = sys.stdin.readline().strip()
dum = 0
r = 0

for i in range(len(li)-1,0,-1):
    if(li[i]=='0'):
        if(dum==1):
            r+=1
            dum=1
        else:
            dum=0
    else:
        if(dum==0):
            dum=1
            r+=1
print(r)
