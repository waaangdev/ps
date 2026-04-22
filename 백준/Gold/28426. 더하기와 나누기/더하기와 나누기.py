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


def sol(n):
    if(n==1):
        return [2]
    if(n==2):
        return [2,4]
    if(n%2==1):
        li = [999983]
        for i in range((n-1)//2):
            li.append(((n-1)//2+2+i))
            li.append(999983-((n-1)//2+2+i))
    else:
        li = [999983,333326,333328,333329]
        for i in range((n)//2-2):
            li.append((n//2+1+i))
            li.append(999983-(n//2+1+i))
        #print(sum(li),sum(li)//999983,min(li))
    return li
print(*sol(n))