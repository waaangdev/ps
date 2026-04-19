import sys
import math
from collections import deque
import heapq
#흰수염과 해적들

def isqrt(n,l,r):
    #print(n,l,r)
    if(l+1 == r):
        return l+1
    dum2  =(l+r)//2
    dum = dum2*dum2
    if(n > dum):
        return isqrt(n,dum2,r)
    elif(n < dum):
        return isqrt(n,l,dum2)
    else:
        return dum2

n,l = map(int,input().split())
li = {}
r = 0
rr = 0
for i in range(n):
    inp = list(map(int,sys.stdin.readline().strip().split()))
    dum = isqrt(inp[0]*inp[0]+inp[1]*inp[1],0,1000000000*2)
    #print(dum)
    dum = l-dum #n번까진 괜찮음
    if(dum >= 0):
        if(not (dum in li)):
            li[dum] = [inp[2]]
        else:
            li[dum] += [inp[2]]
#li.sort(key=lambda x:-x[1])
likeys = sorted(li.keys())
count = 0
q = []
#print(li)
dumhis = -1
dum3 = 0
for i in likeys:
    for j in range(i-dumhis):
        dum3+=1
    for j in (li[i]):
        if(dum3!=0):
            dum3-=1
            r+=j
            heapq.heappush(q,j)
        else:
            if(q[0] < j):
                r+=abs(q[0] - j)
                heapq.heappop(q)
                heapq.heappush(q,j)

    dumhis = i


print(r)