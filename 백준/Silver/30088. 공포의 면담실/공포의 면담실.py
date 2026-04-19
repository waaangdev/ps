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
li = []
for i in range(n):
    li.append(sum(list(map(int,sys.stdin.readline().split()))[1:]))
li.sort()
for i in range(1,n):
    li[i]+=li[i-1]
print(sum(li))
