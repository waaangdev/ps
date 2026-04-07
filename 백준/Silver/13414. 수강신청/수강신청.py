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

n,m=list(map(int,sys.stdin.readline().split()))
li ={}
li2 = [""]*m
for i in range(m):
    inp = sys.stdin.readline().strip()
    if(inp in li):li2[li[inp]]=""
    li2[i]=inp
    li[inp]=i
d = 0
for i in range(m):
    if(li2[i]!=""):
        print(li2[i])
        d+=1
    if(d==n):break