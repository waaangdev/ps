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
    li[i] = max(li[i],li[i-1])
if(sum(li)%3==0):
    print("Delicious!")
else:
    print("Oh My God!")