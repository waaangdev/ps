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
n,m = list(map(int,sys.stdin.readline().split()))
li = list(map(int,sys.stdin.readline().split()))
r = 0
for i in range(n):
    for j in range(i):
        for k in range(j):
            if(li[i]+li[j]+li[k] <= m):
                r=max(r,li[i]+li[j]+li[k])
print(r)