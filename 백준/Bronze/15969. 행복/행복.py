import sys
from collections import deque
import math

a =  int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))
r = 0
max_ = -1
min_ = 1001

for i in range(a):
    max_ = max(max_,li[i])
    min_ = min(min_,li[i])
print(max_-min_)