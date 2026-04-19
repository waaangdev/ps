import sys
from collections import deque
import random
import math
# n = int(sys.stdin.readline())
# li1 = list(map(int,sys.stdin.readline().split()))

#sys.setrecursionlimit(100001)

n= int(sys.stdin.readline())

L,R,Y = list(map(int,sys.stdin.readline().split()))

rl = [0 for i in range(n+1)]

li = []

for i in range(n):
    x,hi,vi = list(map(int,sys.stdin.readline().split()))
    dum = (x*hi-vi*Y)//hi+1
    li.append((dum,1))
    dum = (x*hi+vi*Y)//hi+((x*hi+vi*Y)%hi!=0)*1
    li.append((dum,-1))

li.sort()
#print(li)
xhis = L
stack = 0
for i in li:

    if(i[0] > R):
        break

    if(i[0] > xhis):
        #print(i[0],stack)
        rl[stack]+=(i[0]-xhis)
        xhis= i[0]

    if(i[1] == -1):stack-=1
    if(i[1] == 1):stack+=1

rl[stack]+=(R-xhis)+1

#print(rl)

rlr = 0
for i in rl:
    rlr+=i
    print(rlr)