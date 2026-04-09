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

for cases in range(int(sys.stdin.readline())):
    n= int(sys.stdin.readline())
    li = []
    for i in range(n):
        li.append(list(map(int,sys.stdin.readline().split())))
    r = 0
    for i in range(n):
        for j in range(i):
            gi = 0
            for k in range(n):
                if((li[k][0]-li[i][0])*(li[i][1]-li[j][1])+li[i][1]*(li[i][0]-li[j][0])==li[k][1]*(li[i][0]-li[j][0])):
                    gi+=1
            r=max(r,gi)
    print(f"Case #{cases+1}: {r}")