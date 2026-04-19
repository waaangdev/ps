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
li.sort()
li2 = []
for i in range(n-1):
    if(li[i]==li[i+1]):
        li2.append(li[i])
print(len(set(li))+len(set(li2)))