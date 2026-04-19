"용액"

import sys
from collections import deque

a = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

p1 = 0
p2 = a-1
r = 2100000000
r1 = 0
r2 = 0

while p1 < p2:
    if(r>abs(li[p1]+li[p2])):
        r = abs(li[p1]+li[p2])
        r1 = li[p1]
        r2 = li[p2]
    if(li[p1]+li[p2] < 0):
        p1 += 1
    else:
        p2-=1
print(r1,r2)