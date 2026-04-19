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
a,b = tuple(map(int,sys.stdin.readline().split()))
li = {}
li2 = set()
for i in range(n):
    inp = tuple(map(int,sys.stdin.readline().split()))
    li2.add(inp)
    if(inp in li):
        li[inp]+=1
    else:
        li[inp]=1
r = 0
for i in li2:
    q,w = list(i)
    dum =1
    for j in [i,(q,w+b),(q+a,w),(q+a,w+b)]:
        if(j in li):
            dum*=li[j]
        else:
            dum=0
    r+=dum
print(r)