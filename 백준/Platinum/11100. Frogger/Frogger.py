import sys
from collections import deque
import random
import math
import heapq #minheap

input = lambda: sys.stdin.readline().rstrip()

#n = int(input())
#li = list(map(int,input().split()))

sys.setrecursionlimit(100010)

for i in range(int(input())):
    print(([1,2,4,8,20]+["frogger"]*30)[int(input())])