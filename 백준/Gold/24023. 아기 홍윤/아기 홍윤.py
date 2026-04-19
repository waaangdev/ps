import sys
from collections import deque
import math

b,c = map(int,sys.stdin.readline().split())
li =  list(map(int,sys.stdin.readline().split()))

p1 = 0
p2 = 1
p = li[0]

while 1:
    if (p == c):
        break
    if((~c & p) != 0):
        if(p2 == b):
            break
        p1 = p2
        p2 = p1+1
        p = li[p1]
    else:
        p2 += 1
        if(p2 > b):
            break
        p |= li[p2-1]
if (p == c):
    print(p1+1,p2)
else:
    print(-1)