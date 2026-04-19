import sys
from collections import deque

n = int(sys.stdin.readline())
r = 0
for i in range(n):
    r+=sum( list(map(int,sys.stdin.readline().split())))
print(r)