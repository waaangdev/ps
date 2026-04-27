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
d = {}
rr = 0
def dadd(a):
    global rr
    if(a in d):
        d[a]+=1
    else:
        d[a]=1
    rr=max(rr, d[a])

for i in range(n):
    x,y = list(map(int,sys.stdin.readline().split()))
    if(x==0):
        if(y < 0):
            dadd((1000001,0,-1))
        else:
            dadd((1000001,0,1))
    elif(x < 0):
        dadd((y//math.gcd(y,x),x//math.gcd(y,x),-1))
    else:
        dadd((y//math.gcd(y,x),x//math.gcd(y,x),1))
print(rr)