import sys
from collections import deque
import math
import random

a = int(sys.stdin.readline())
li =[]
max_ = 0
max2 = 0
for i in range(a):
    b,c = map(int,sys.stdin.readline().split())
    li.append([b,c])
li.sort(key = lambda x: (x[0]+x[1]))
max_ =abs(li[0][1] - li[-1][1]) + abs(li[-1][0] - li[0][0])
li.sort(key = lambda x: (x[0]-x[1]))
max_ =max(abs(li[0][1] - li[-1][1]) + abs(li[-1][0] - li[0][0]),max_)
print(max_)