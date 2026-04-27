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
t,p = list(map(int,sys.stdin.readline().split()))

print(sum([i//t+(i%t!=0)*1 for i in li]))
print(n//p,n%p)