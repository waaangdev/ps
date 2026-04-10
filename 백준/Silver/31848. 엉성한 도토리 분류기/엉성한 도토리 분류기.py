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

for i in range(1,n):
    li[i] = max(li[i-1],li[i]+i)


q = int(sys.stdin.readline())
qli = list(map(int,sys.stdin.readline().split()))
for i in range(q):
    l,r = -1,n-1
    while(l+1!=r):
        mid= (l+r)//2
        if(li[mid] < qli[i]):
            l = mid
        else:
            r = mid
    print(r+1,end=' ')