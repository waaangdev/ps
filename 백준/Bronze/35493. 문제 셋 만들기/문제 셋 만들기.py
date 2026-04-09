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
li = list(map(int,sys.stdin.readline().split()))

if(n==1):
    if(li[0]%2 ==0):
        print("YES")
    else:
        print("NO")
else:
    if(sum(li)%2 ==0):
        print("YES")
    else:
        r="NO"
        for i in li:
            if(i%2==1):
                r="YES"
        print(r)