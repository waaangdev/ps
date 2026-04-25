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
nl = [0]*n
ml = [0]*m
for i in range(n):
    inp = sys.stdin.readline().strip()
    for j in range(m):
        nl[i]=(nl[i]+int(inp[j]))%2
        ml[j]=(ml[j]+int(inp[j]))%2

rr = n*m
for i in range(2):
    for j in range(2):
        a = nl.count(i)
        b = ml.count(j)
        if(a%2 == 1):
            b = ml.count(1-j)
        if(b%2==1-i):
            rr=min(rr,a+b)
#print(nl,ml)
print(rr)