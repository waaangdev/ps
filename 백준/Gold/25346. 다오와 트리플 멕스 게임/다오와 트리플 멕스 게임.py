import sys
from collections import deque
import random
import math
import heapq #minheap

input = lambda: sys.stdin.readline().rstrip()
print = lambda *a,end='\n': sys.stdout.write(' '.join(map(str,a))+end)

#n = int(input())
#li = list(map(int,input().split()))

sys.setrecursionlimit(100010)

n = int(input())
li = list(map(int,input().split()))
li = sorted(li)

if(max(li)==0):
    print(1)
else:
    if(min(li)==0):
        li.append(max(li)+100)
        mex =1
        for i in range(n):
            if(li[i]+1 < li[i+1]):
                mex = li[i]+1
                break

        print(mex+2)
    else:
        print(0)

