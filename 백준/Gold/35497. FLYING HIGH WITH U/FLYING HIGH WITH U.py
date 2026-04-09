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
li = [0]+list(map(int,sys.stdin.readline().split()))+[0]

dum = 0
r = 0
for i in range(n+1):
    d = li[i+1]-li[i]
    if(d > 0):
        r+=d
        dum+=d
    else:
        dum+=d
print(r)