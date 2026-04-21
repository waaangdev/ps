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

n,m,kk=list(map(int,sys.stdin.readline().split()))
li = [0]*250

li3 = set()
for i3 in range(n+1):
    for j3 in range(m+1):
        for i2 in range(n+1):
            for j2 in range(m+1):
                i=(i3-i2)
                j=(j3-j2)
                li[math.gcd(i,j)+1]+=1

print(li[kk]//2)
            